from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH")