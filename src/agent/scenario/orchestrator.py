from textwrap import dedent

from typing import Iterator
from agno.team.team import Team, RunResponse
from agno.utils.pprint import pprint_run_response
from pprint import pprint

from src.llm.llm import OpenAILLM, GeminiLLM

from src.agent.scenario.ijara import agent as ijara_agent
from src.agent.scenario.istisnaa import agent as istisnaa_agent
from src.agent.scenario.murabaha import agent as murabaha_agent
from src.agent.scenario.musharaka import agent as musharaka_agent
from src.agent.scenario.salam import agent as salam_agent

from src.models.output import ScenarioAgentOutput
from src.utils.parse import parse_json

from examples.scenario import ijara_1, ijara_2, istisnaa, musharaka

orchestrator = Team(
    members=[ijara_agent, istisnaa_agent, musharaka_agent, murabaha_agent, salam_agent],
    model=OpenAILLM.get_openai_chat(),
    # model = GeminiLLM.get_gemini_chat(),
    mode="route",
    success_criteria=dedent("""\
        A comprehensive, authentic and accurate islamic financial journaling.
    """),
    instructions=dedent("""\
        Route accurately to the correct Islamic Financial Operation agent. Do not include any specific instructions, each agent system prompt is enough.\
    """),
    response_model=ScenarioAgentOutput,
    show_tool_calls=True,
    markdown=True,
    enable_agentic_context=True,
    show_members_responses=True,
)

def create_journal(scenario: str, verbose: bool = False) -> str:
    if verbose:
        journal = orchestrator.run(scenario, stream=True, stream_intermediate_steps=True)
    else:
        journal = orchestrator.run(scenario, stream=False)
    # return journal.content
    # return ScenarioAgentOutput(**journal)
    return journal.content

if __name__ == "__main__":
    scenario = istisnaa
    
    # journal = create_journal(scenario, verbose=True)
    
    # # pprint(journal.model_dump())
    # print(journal)
    
    # pprint_run_response(journal)
    
    
    # pprint(journal)
    
    # orchestrator.run(
    #     scenario, stream=True
    # )
    
    orchestrator.print_response(scenario, stream=True)
    # print("Final Response:")
    # print(responses.content)

    # pprint(response)
    # print(response.content.model_dump())