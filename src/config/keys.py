import os
import dotenv

dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_HOST = os.getenv("PINECONE_INDEX_HOST")