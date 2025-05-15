OPENAI_KEY = ""


from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from textwrap import dedent

 # MOST BASIC AGENT

agent = Agent(
    model=OpenAIChat(id="gpt-4o",api_key=OPENAI_KEY),
    markdown=True
)
agent.print_response("Share a 2 sentence horror story.")