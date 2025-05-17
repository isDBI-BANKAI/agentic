from agno.agent import Agent
from agno.team.team import Team
from textwrap import dedent
from src.llm.llm import OpenAILLM

from examples.product_design import prompt

requirements_agent_1 = Agent(
    name="Requirements Agent 1",
    role="Fianncial Accouting Expert Consultant",
    model=OpenAILLM.get_openai_chat(),
    # tools=[retrieve],
    instructions=dedent("""
    Collect, question and refine the company's needs until you can fill every field of the Requirement Sheet:
    - Company profile: legal type, sector (NAICS), years active, governance notes  
    - Financing need: object(s) to purchase/build, CAPEX vs OPEX split, budget ceiling  
    - Timing: delivery schedule & tolerance, milestone payments preferred  
    - Cash-flow preference: grace periods, seasonal patterns, ROI target  
    """),
    show_tool_calls=True,
    markdown=True,
)

requirements_agent_2 = Agent(
    name="Requirements Agent 2",
    role="Fianncial Accouting Expert Consultant",
    model=OpenAILLM.get_openai_chat(),
    # tools=[retrieve],
    instructions=dedent("""
    Collect, question and refine the company's needs until you can fill every field of the Requirement Sheet:
    - Company profile: legal type, sector (NAICS), years active, governance notes  
    - Financing need: object(s) to purchase/build, CAPEX vs OPEX split, budget ceiling  
    - Timing: delivery schedule & tolerance, milestone payments preferred  
    - Cash-flow preference: grace periods, seasonal patterns, ROI target  
    """),
    show_tool_calls=True,
    markdown=True,
)

# team leader
requirements_team = Team(
    name="Requirement Clarification",
    members=[requirements_agent_1, requirements_agent_2], 
    model=OpenAILLM.get_openai_chat(),
    mode="coordinate",
    # tools=[get_outline, retrieve],
    instructions=dedent("""
You are the Requirement Clarification Leader for Stage 1 of the Islamic-finance product-design flow.  

Mission
Transform the raw prompt into a complete, internally-consistent Requirements Sheet that will feed later stages.

Workflow
1. Task splitting among agents to extract and structure:
    - Company profile (legal type, NAICS sector, years active, governance notes)  
    - Financing need (asset(s) to purchase/build, CAPEX vs OPEX, budget ceiling).  
    - Timing (delivery schedule, tolerance, milestone payments)  
    - Cash-flow preference (grace periods, seasonality, ROI target).  

2- Account for missing requirements and risk considerations

Finally provide a clear requirements instructions to the next stage (Team of agents to map the requirements to Isamic Financial Accounting Standards (FAS))
    """),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
    enable_agentic_context=True,
    show_members_responses=True,
    success_criteria="Clear, comprehensive, and complete requirement sheet"
)

if __name__ == "__main__":
    requirements_team.print_response(prompt, stream=True)
