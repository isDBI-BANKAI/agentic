from agno.agent import Agent
from agno.team.team import Team
from agno.models.openai import OpenAIChat
from textwrap import dedent
from src.models.output import ReasonningAndSuggestionsTeamOutput

from src.config.keys import OPENAI_API_KEY
from src.config.config import OPENAI_LLM_MODEL


# Agent 1: Gatherer 1
gatherer_1 = Agent(
    name="Gatherer_1",
    role="Improvement Ideas Analyst",
    model=OpenAIChat(id=OPENAI_LLM_MODEL, api_key=OPENAI_API_KEY),
    instructions=dedent("""
        You are responsible for analyzing the assigned improvement areas and compiling a list of potential improvement suggestions. 
        - Focus only on identifying potential areas for improvement. 
        - Do NOT provide specific recommendations or compliance assessments. 
        - Collaborate with Gatherer_2 to consolidate findings and refine the list.
    """),
    show_tool_calls=True,
    markdown=True
)

# Agent 2: Gatherer 2
gatherer_2 = Agent(
    name="Gatherer_2",
    role="Improvement Ideas Analyst",
    model=OpenAIChat(id=OPENAI_LLM_MODEL, api_key=OPENAI_API_KEY),
    instructions=dedent("""
        You are responsible for analyzing the assigned improvement areas and compiling a list of potential improvement suggestions. 
        - Focus only on identifying potential areas for improvement. 
        - Do NOT provide specific recommendations or compliance assessments. 
        - Collaborate with Gatherer_1 to consolidate findings and refine the list.
    """),
    show_tool_calls=True,
    markdown=True
)

# Team Leader
reasoning_team_leader = Team(
    name="Reasoning_And_Suggestions_Team",
    members=[gatherer_1, gatherer_2],
    model=OpenAIChat(id=OPENAI_LLM_MODEL, api_key=OPENAI_API_KEY),
    mode="coordinate",
    instructions=dedent("""
        You are the lead coordinator for gathering and refining improvement suggestions. 
        1. Assign each gatherer a subset of improvement areas to analyze.
        2. Ensure the gatherers communicate and consolidate their findings into a single, refined list.
        3. Return the consolidated list in the specified format, focusing only on potential improvement areas without recommendations or compliance analysis.
    """),
    response_model=ReasonningAndSuggestionsTeamOutput,
    show_tool_calls=True,
    markdown=True
)
