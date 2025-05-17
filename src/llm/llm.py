from abc import ABC, abstractmethod

from src.config.keys import GEMINI_API_KEY, OPENAI_API_KEY
from src.config.config import GEMINI_MODEL_NAME, OPENAI_LLM_MODEL, OPENAI_LLM_TEMPERATURE

import google.generativeai as genai
from agno.models.openai import OpenAIChat
from agno.models.google import Gemini
from openai import OpenAI

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

    @staticmethod
    def get_gemini_chat():
        return Gemini(
            id=GEMINI_MODEL_NAME,
            api_key=GEMINI_API_KEY
        )

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text
    
class OpenAILLM():
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        
    @staticmethod
    def get_openai_chat():
        return OpenAIChat(
            id=OPENAI_LLM_MODEL,
            api_key=OPENAI_API_KEY,
        )
        
    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=OPENAI_LLM_MODEL,
            temperature=OPENAI_LLM_TEMPERATURE,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content

if __name__ == "__main__":
    llm = OpenAILLM()
    prompt = "What is the capital of France?"
    response = llm.generate(prompt)
    print(response)
    
    llm = GeminiLLM()
    response = llm.generate(prompt)
    print(response)