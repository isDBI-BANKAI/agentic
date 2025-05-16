from typing import Iterator
from textwrap import dedent

from agno.agent import Agent, RunResponse
from agno.utils.pprint import pprint_run_response

from src.llm.llm import OpenAILLM

from agno.tools.reasoning import ReasoningTools
from src.tools.retrieval import get_outline, retrieve

agent = Agent(
    model=OpenAILLM().get_openai_chat(),
    instructions=dedent("""\
        You are an expert islamic finance accountant.
        
        Instructions:
        - You must ensure complete integrity and accuracy in your responses. For that, you are highly guided by the internal documentation using the outline and retrieving tools.
    """),
    tools=[ReasoningTools(), get_outline, retrieve],
    show_tool_calls=True,
    markdown=True,
)

prompt = "What is Musharakah?"

response_stream: Iterator[RunResponse] = agent.run(
    prompt, stream=True
)

pprint_run_response(response_stream, markdown=True)
