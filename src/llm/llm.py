from abc import ABC, abstractmethod

from src.config.keys import GEMINI_API_KEY, OPENAI_API_KEY
from src.config.config import GEMINI_MODEL_NAME, OPENAI_LLM_MODEL

import google.generativeai as genai
from agno.models.openai import OpenAIChat
from agno.models.google import Gemini

class LLM(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
    
class GeminiLLM(LLM):
    def __init__(self):
        super().__init__()
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(GEMINI_MODEL_NAME)

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text
    
class OpenAILLM():
    def __init__(self):
        pass
        
    @staticmethod
    def get_openai_chat():
        return OpenAIChat(
            id=OPENAI_LLM_MODEL,
            api_key=OPENAI_API_KEY,
        )
