from agno.agent import Agent
from agno.team.team import Team
from textwrap import dedent
from src.tools.retrieval import get_outline, retrieve
from src.llm.llm import GeminiLLM, OpenAILLM

from examples.product_design import prompt, design

validation_agent_1 = Agent(
    name="Shariaah Validation Agent 1",
    role="Islamic Financial Shariaah Standards Expert",
    model=OpenAILLM.get_openai_chat(),
    tools=[retrieve],
    instructions=dedent("""
    Given a design for a financial product design, validate its compliance with islamic Shariaah Standards (FAS)
    
    - retrieve: A tool to fetch authoritative text from the SS documents, to assist you for accurate retrieval. You have to get all needed context before you start your calculations and journal entries.
    
    be concise and straight to the point.
    """),
    show_tool_calls=True,
    markdown=True,
)

validation_agent_2 = Agent(
    name="Shariaah Validation Agent 2",
    role="Islamic Financial Shariaah Standards Expert",
    model=OpenAILLM.get_openai_chat(),
    tools=[retrieve],
    instructions=dedent("""
    Given a design for a financial product design, validate its compliance with islamic Shariaah Standards (FAS)
    
    - retrieve: A tool to fetch authoritative text from the SS documents, to assist you for accurate retrieval. You have to get all needed context before you start your calculations and journal entries.
    
    be concise and straight to the point.
    """),
    show_tool_calls=True,
    markdown=True,
)

# team leader
validation_team = Team(
    name="Shariaah Validation",
    members=[validation_agent_1, validation_agent_2], 
    model=OpenAILLM.get_openai_chat(),
    mode="coordinate",
    tools=[get_outline, retrieve],
    instructions=dedent("""
You are the Shariaah Validation Team leader, the previous stage of a Financial Product Design yielded a design of a fiancial product, your mission is to validate its Shariaah Compliance.

You are provided with the following tools:
- get_outline: A tool to view SHariaah Standards (SS) document structure, to assist you for accurate retrieval. You always need to call this first to know the outline, as it contains the sections and filtering tags for the retriever. That's a must to ensure compliance with the standards and 100% integrity. The tags are to be identified between [].
- retrieve: A tool to fetch authoritative text from the SS documents, to assist you for accurate retrieval. You have to get all needed context before you start your calculations and journal entries. Tags are found in the ouline written between []

Make sure to also inform the tasked agents of some useful tags to use in their queries based on the outline you observe. but do not output the whole outline, it's a lot!

be concise and straight to the point. Identify the key SS to investigate.

You can delegate certain terms/conditions to the team.
    """),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
    enable_agentic_context=True,
    show_members_responses=True,
    success_criteria="Clear validation of the design compliance with Shariaah Standards (SS)"
)

if __name__ == "__main__":
    validation_team.print_response(f"NEEDS: \n{prompt} \nFinancial Product Design: \n {design}", stream=True)