from dotenv import load_dotenv
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DATASET_PATH = "data/dataset_pyme.json"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"