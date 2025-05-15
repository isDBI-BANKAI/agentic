from openai import OpenAI

from src.config.keys import OPENAI_API_KEY
from src.config.config import OPENAI_EMBEDDING_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def get_embeddings(texts: list[str]):
    response = client.embeddings.create(model=OPENAI_EMBEDDING_MODEL,
    input=texts)
    return [d.embedding for d in response.data]