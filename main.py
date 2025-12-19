import os
from dotenv import load_dotenv
load_dotenv()
from bot.bot_instance import bot
from bot import handlers

#Punto de entrada
if __name__ == "__main__":
    print("Bot de Dietética iniciado. Esperando mensajes...")
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Error gatal en el polling: {e}")