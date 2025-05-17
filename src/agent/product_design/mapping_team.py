from agno.agent import Agent
from agno.team.team import Team
from textwrap import dedent
from src.tools.retrieval import get_outline, retrieve
from src.llm.llm import GeminiLLM, OpenAILLM

from examples.product_design import requirements

mapping_agent_1 = Agent(
    name="FAS Mapping Agent 1",
    role="Islamic Financial Accouting Expert",
    model=OpenAILLM.get_openai_chat(),
    tools=[retrieve],
    instructions=dedent("""
    Given a sheet of requirement for a financial product design, identify and map the suitable islamic Financial Accounting Standards (FAS)
    
    - retrieve: A tool to fetch authoritative text from the FAS or SS documents, to assist you for accurate retrieval. You have to get all needed context before you start your calculations and journal entries.
    
    be concise and straight to the point.
    """),
    show_tool_calls=True,
    markdown=True,
)

mapping_agent_2 = Agent(
    name="FAS Mapping Agent 2",
    role="Islamic Financial Accouting Expert",
    model=OpenAILLM.get_openai_chat(),
    tools=[retrieve],
    instructions=dedent("""
    Given a sheet of requirement for a financial product design, identify and map the suitable islamic Financial Accounting Standards (FAS).
    
    - retrieve: A tool to fetch authoritative text from the FAS or SS documents, to assist you for accurate retrieval. You have to get all needed context before you start your calculations and journal entries.
    
    be concise and straight to the point.

    """),
    show_tool_calls=True,
    markdown=True,
)

# team leader
mapping_team = Team(
    name="FAS Mapping",
    members=[mapping_agent_1, mapping_agent_2], 
    model=OpenAILLM.get_openai_chat(),
    mode="coordinate",
    tools=[get_outline, retrieve],
    instructions=dedent("""
You are the Mapping Team leader, the previous stage of a Financial Product Design yielded a requirement sheet out of raw details, your mission is to map these requirements into islamic Financial Accounting Standards (FAS) that can serve designing the Financial product.

You are provided with the following tools:
- get_outline: A tool to view Financial Accounting Standards (FAS) document structure, to assist you for accurate retrieval. You always need to call this first to know the outline, as it contains the sections and filtering tags for the retriever. That's a must to ensure compliance with the standards and 100% integrity. The tags are to be identified between [].
- retrieve: A tool to fetch authoritative text from the FAS or SS documents, to assist you for accurate retrieval. You have to get all needed context before you start your calculations and journal entries. Tags are found in the ouline written between []

Make sure to also inform the tasked agents of some useful tags to use in their queries based on the outline you observe. but do not output the whole outline, it's a lot!

be concise and straight to the point. Identify the key FAS to investigate.

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