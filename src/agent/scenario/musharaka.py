from agno.agent import Agent, RunResponse

from agno.tools.calculator import CalculatorTools
from agno.tools.reasoning import ReasoningTools
from src.tools.retrieval import get_outline, retrieve

from src.llm.llm import OpenAILLM

from src.prompt.scenario.ijara import get_system_prompt
from src.models.output import ScenarioAgentOutput

agent = Agent(
    name="Musharaka Auditing Agent",
    model=OpenAILLM().get_openai_chat(),
    instructions=get_system_prompt(),
    tools=[
        ReasoningTools(),
        get_outline,
        retrieve,
        CalculatorTools(),
    ],
    response_model=ScenarioAgentOutput,
    show_tool_calls=True,
    markdown=True,
)