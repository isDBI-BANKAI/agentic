from typing import Iterator
from textwrap import dedent

from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response

from src.config.keys import OPENAI_API_KEY
from src.config.config import OPENAI_LLM_MODEL

agent = Agent(
    model=OpenAIChat(id=OPENAI_LLM_MODEL, api_key=OPENAI_API_KEY),
    instructions=dedent("""\
        You are an enthusiastic news reporter with a flair for storytelling! 🗽
        Think of yourself as a mix between a witty comedian and a sharp journalist.

        Your style guide:
        - Start with an attention-grabbing headline using emoji
        - Share news with enthusiasm and NYC attitude
        - Keep your responses concise but entertaining
        - Throw in local references and NYC slang when appropriate
        - End with a catchy sign-off like 'Back to you in the studio!' or 'Reporting live from the Big Apple!'

        Remember to verify all facts while keeping that NYC energy high!\
    """),
    markdown=True,
)

# show response in markdown
# agent.print_response(
#     "Tell me about a breaking news story happening in Times Square.", stream=True
# )

response_stream: Iterator[RunResponse] = agent.run(
    "Tell me about a breaking news story happening in Times Square.", stream=True
)

pprint_run_response(response_stream, markdown=True)
