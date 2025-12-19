from bot.bot_instance import bot
import json
from bot.responses import respuesta_groq

#Mensaje bienvenida
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    #Responde con un mensaje de bienvenidas
    bot.reply_to(message, "Hola! Soy el asistente virtual de al_naturalmente, que es lo que necesitas?")

#Handler para cualquier otro mensaje de texto
@bot.message_handler(func=lambda message: True)
def responder(message):
    if message.text is None:
        bot.reply_to(message, "Por favor, enviame tu consulta como un mensaje de texto")
    respuesta_ia = respuesta_groq(message)
    bot.reply_to(message, respuesta_ia)