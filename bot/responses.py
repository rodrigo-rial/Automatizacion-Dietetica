import json
from config import GROQ_API_KEY
from groq import Groq
from .bot_instance import dataset

# Usamos el cliente oficial (más robusto que requests manual)
client = Groq(api_key=GROQ_API_KEY)

def buscar_en_dataset(pregunta, dataset):
    pregunta_limpia = pregunta.strip().lower()
    for item in dataset:
        if item['pregunta'].strip().lower() == pregunta_limpia:
            return item['respuesta']
    return None

def respuesta_groq(mensaje):
    if not GROQ_API_KEY:
        return "[Error: API KEY no configurada]"

    # 1. Asegurarnos de que 'mensaje' sea texto plano y no un objeto
    # Si 'mensaje' viene de otro chat, extraemos solo el texto
    contenido_usuario = mensaje.content if hasattr(mensaje, 'content') else str(mensaje)

    # 2. Convertimos el dataset a una cadena de texto legible para el Prompt
    contexto_dataset = json.dumps(dataset, ensure_ascii=False)

    system_prompt = f"""
        Eres el asistente virtual amable y servicial del emprendimiento 'Al Naturalmente'. NO TE LLAMAS "Al naturalmente"
        Tu tarea es responder preguntas de los clientes basándote ÚNICAMENTE en la siguiente información oficial:
        {contexto_dataset}

        Instrucciones:
        - Responde de forma natural, breve y cordial.
        - Si no sabes algo, sugiere contactar a las dueñas.
        - No inventes información. Usa emojis 🌿.
    """

    try:
        # 3. Usamos el cliente oficial en lugar de requests.post
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": contenido_usuario},
            ],
            model="llama-3.1-8b-instant",
        )
        
        return chat_completion.choices[0].message.content.strip()

    except Exception as e:
        # Esto capturará si algún objeto sigue sin ser serializable o hay error de red
        return f"[Error de conexión a Groq: {str(e)}]"