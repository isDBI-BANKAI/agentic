from agno.agent import Agent
from agno.team.team import Team
from textwrap import dedent
from src.tools.retrieval import get_outline, retrieve
from src.llm.llm import GeminiLLM, OpenAILLM

from examples.product_design import prompt, requirements, mapping

design_agent_1 = Agent(
    name="Financial Product Design Agent 1",
    role="Islamic Financial Product Design Expert",
    model=OpenAILLM.get_openai_chat(),
    instructions=dedent("""
    Brainstorm and suggest a financial product designt that satisfies the needs, and aligns with the islamic financial accounting standards mapping.
    
    be concise and straight to the point.
    """),
    show_tool_calls=True,
    markdown=True,
)

design_agent_2 = Agent(
    name="Financial Product Design Agent 2",
    role="Islamic Financial Product Design Expert",
    model=OpenAILLM.get_openai_chat(),
    instructions=dedent("""
    Brainstorm and suggest a financial product designt that satisfies the needs, and aligns with the islamic financial accounting standards mapping.
    
    be concise and straight to the point.
    """),
    show_tool_calls=True,
    markdown=True,
)

# team leader
design_team = Team(
    name="Financial Product Design",
    members=[design_agent_1, design_agent_2], 
    model=OpenAILLM.get_openai_chat(),
    mode="coordinate",
    instructions=dedent("""
You are the Financial Product Design leader, the previous stage of a Financial Product Design yielded a Financial Accounting Standards (FAS) mapping of given company needs, your mission is to design a financial product design.

Make sure to also inform the tasked agents of some useful tags to use in their queries based on the outline you observe. but do not output the whole outline, it's a lot!

be concise and straight to the point.
    """),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
    enable_agentic_context=True,
    show_members_responses=True,
    success_criteria="Design a financial product that satisfies the needs and aligns with the FAS mapping"
)

if __name__ == "__main__":
    design_team.print_response(f"NEEDS: \n{prompt} \nFAS Mapping: \n {mapping}", stream=True)