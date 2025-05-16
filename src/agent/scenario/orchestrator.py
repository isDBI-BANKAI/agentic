from textwrap import dedent

from typing import Iterator
from agno.team.team import Team, RunResponse
from agno.utils.pprint import pprint_run_response

from src.llm.llm import OpenAILLM

from src.agent.scenario.ijara import agent as ijara_agent
from src.agent.scenario.istisnaa import agent as istisnaa_agent
from src.agent.scenario.murabaha import agent as murabaha_agent
from src.agent.scenario.musharaka import agent as musharaka_agent
from src.agent.scenario.salam import agent as salam_agent
    
from examples.scenario import ijara
    
orchestrator = Team(
    members=[ijara_agent, istisnaa_agent, musharaka_agent, murabaha_agent, salam_agent],
    model=OpenAILLM.get_openai_chat(),
    mode="route",
    success_criteria=dedent("""\
        A comprehensive and accurate islamic financial journaling.
    """),
    instructions=dedent("""\
        Route accurately to the correct Islamic Financial Operation agent\
    """),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
    enable_agentic_context=True,
    show_members_responses=True,
)

if __name__ == "__main__":
    prompt = ijara
    
    response_stream: Iterator[RunResponse] = orchestrator.run(
        prompt, stream=True
    )

    pprint_run_response(response_stream, markdown=True)