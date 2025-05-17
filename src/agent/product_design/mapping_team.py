from agno.agent import Agent
from agno.team.team import Team
from textwrap import dedent
from src.tools.retrieval import get_outline, retrieve
from src.llm.llm import GeminiLLM

from examples.product_design import requirements

mapping_agent_1 = Agent(
    name="FAS Mapping Agent 1",
    role="Islamic Financial Accouting Expert",
    model=GeminiLLM.get_gemini_chat(),
    tools=[retrieve],
    instructions=dedent("""
    Given a sheet of requirement for a financial product design, identify and map the suitable islamic Financial Accounting Standards (FAS)
    """),
    show_tool_calls=True,
    markdown=True,
)

mapping_agent_2 = Agent(
    name="FAS Mapping Agent 2",
    role="Islamic Financial Accouting Expert",
    model=GeminiLLM.get_gemini_chat(),
    tools=[retrieve],
    instructions=dedent("""
    Given a sheet of requirement for a financial product design, identify and map the suitable islamic Financial Accounting Standards (FAS)
    """),
    show_tool_calls=True,
    markdown=True,
)

# team leader
mapping_team = Team(
    name="FAS Mapping",
    members=[mapping_agent_1, mapping_agent_2], 
    model=GeminiLLM.get_gemini_chat(),
    mode="coordinate",
    tools=[get_outline, retrieve],
    instructions=dedent("""
You are the Mapping Team leader, the previous stage of a Financial Product Design yielded a requirement sheet out of raw details, your mission is to map these requirements into islamic Financial Accounting Standards (FAS) that can serve designing the Financial product.

- Referene the outlines of the FAS using the tools:
    - get_outline: to get an idea of the available FAS to study
    - retrieve: to get specific content guided by the FAS content and tags

You can delegate certain strategies or analysis directions to the team.
    """),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
    enable_agentic_context=True,
    show_members_responses=True,
    success_criteria="Identify the suitable FAS for the requirement sheet"
)

if __name__ == "__main__":
    mapping_team.print_response(requirements, stream=True)