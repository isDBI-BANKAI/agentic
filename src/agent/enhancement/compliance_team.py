from agno.agent import Agent
from agno.team.team import Team
from agno.models.openai import OpenAIChat
from textwrap import dedent
from pydantic import BaseModel

from src.config.keys import OPENAI_API_KEY
from src.config.config import OPENAI_LLM_MODEL

# Output Model for Compliance Check
class ComplianceCheckTeamOutput(BaseModel):
    final_verdict: str
    final_improvements: str

# Agent 1: Compliance Checker 1
checker_1 = Agent(
    name="Compliance_Checker_1",
    role="Compliance Analyst",
    model=OpenAIChat(id=OPENAI_LLM_MODEL, api_key=OPENAI_API_KEY),
    instructions=dedent("""
        You are responsible for assessing whether the given suggestions are compliant with the relevant FAS standards.
        - Focus on identifying any non-compliant elements or areas that may require modification.
        - Provide reasoned arguments for each suggestion regarding its compliance status.
        - Communicate with Compliance_Checker_2 to reach a consensus.
    """),
    show_tool_calls=True,
    markdown=True
)

# Agent 2: Compliance Checker 2
checker_2 = Agent(
    name="Compliance_Checker_2",
    role="Compliance Analyst",
    model=OpenAIChat(id=OPENAI_LLM_MODEL, api_key=OPENAI_API_KEY),
    instructions=dedent("""
        You are responsible for assessing whether the given suggestions are compliant with the relevant FAS standards.
        - Focus on identifying any non-compliant elements or areas that may require modification.
        - Provide reasoned arguments for each suggestion regarding its compliance status.
        - Communicate with Compliance_Checker_1 to reach a consensus.
    """),
    show_tool_calls=True,
    markdown=True
)

# Team Leader / Judge
compliance_team_leader = Team(
    name="Compliance_Check_Team",
    members=[checker_1, checker_2],
    model=OpenAIChat(id=OPENAI_LLM_MODEL, api_key=OPENAI_API_KEY),
    mode="coordinate",
    instructions=dedent("""
        You are the final judge responsible for consolidating the compliance assessment.
        1. Assign each compliance checker a subset of suggestions to review.
        2. Facilitate a brief conversation between the two checkers to resolve any differences in opinion.
        3. Once consensus is reached, formalize the final verdict and the compliant suggestions.
        4. Return the consolidated output in the specified format, focusing solely on compliance analysis.
    """),
    response_model=ComplianceCheckTeamOutput,
    show_tool_calls=True,
    markdown=True
)
