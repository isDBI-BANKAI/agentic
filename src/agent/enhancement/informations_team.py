from agno.agent import Agent
from agno.team.team import Team
from agno.models.google import Gemini
from textwrap import dedent
from src.models.output import InformationGatheringTeamOutput
from agno.tools.duckduckgo import DuckDuckGoTools
from src.tools.retrieval import get_outline, retrieve
from src.config.keys import OPENAI_API_KEY,GEMINI_API_KEY
from src.config.config import OPENAI_LLM_MODEL,GEMINI_MODEL_NAME

# Create document analysis agents
document_agent_1 = Agent(
    name="Document_Agent_1",
    role="FAS Analysis Specialist",
    model=Gemini(
        id=GEMINI_MODEL_NAME,
        api_key=GEMINI_API_KEY
    ),
    tools=[retrieve],
    instructions=dedent("""
        You are a specialist in identifying potential areas for improvement in FAS sections as assigned by the team leader.

        - Only analyze the sections specified by the leader using the provided tags.
        - Use the retrieve tool to focus solely on these sections, targeting unclear, inconsistent, or outdated content.
        - Highlight potential areas for improvement without providing recommendations or solutions.

        Style Guide:
        - Structure findings under 'Identified Areas for Improvement'.
        - Use concise, direct language.
        - Include relevant quotes where applicable.
    """),
    show_tool_calls=True,
    markdown=True,
)

document_agent_2 = Agent(
    name="Document_Agent_2",
    role="FAS Analysis Specialist",
    model=Gemini(
        id=GEMINI_MODEL_NAME,
        api_key=GEMINI_API_KEY
    ),
    tools=[retrieve],
    instructions=dedent("""
        You are a specialist in identifying potential areas for improvement in FAS sections as assigned by the team leader.

        - Only analyze the sections specified by the leader using the provided tags.
        - Use the retrieve tool to focus solely on these sections, targeting unclear, inconsistent, or outdated content.
        - Highlight potential areas for improvement without providing recommendations or solutions.

        Style Guide:
        - Structure findings under 'Identified Areas for Improvement'.
        - Use concise, direct language.
        - Include relevant quotes where applicable.
    """),
    show_tool_calls=True,
    markdown=True,
)

# Create web research agent
research_agent = Agent(
    name="Research_Agent",
    role="External Research Specialist",
    model=Gemini(
        id=GEMINI_MODEL_NAME,
        api_key=GEMINI_API_KEY
    ),
    tools=[DuckDuckGoTools()],
    instructions=dedent("""
        You are responsible for identifying external evidence of potential gaps or issues in the specified FAS as assigned by the team leader.

        - Focus on finding external content that highlights ambiguities, inconsistencies, or challenges in implementing the FAS.
        - Include notable industry discussions, case studies, or regulatory feedback related to the assigned sections.
        - Do NOT suggest solutions or improvements, only identify areas where issues are evident.

        Style Guide:
        - Organize findings under 'External Issues and Gaps'.
        - Include source links for all major claims.
        - Highlight particularly relevant case studies or expert opinions.
    """),
    show_tool_calls=True,
    markdown=True,
)

# Create team leader to coordinate
fas_research_team = Team(
    name="FAS_Research_Team",
    members=[document_agent_1, document_agent_2, research_agent], 
    model=Gemini(
        id=GEMINI_MODEL_NAME,
        api_key=GEMINI_API_KEY
    ),
    mode="coordinate",
    tools=[get_outline, retrieve],
    instructions=dedent("""
        You are the team lead for FAS analysis. 📊

        Your tasks:
        1. Use the get_outline tool to extract the structure of the FAS document for the specified operation.
        2. Identify specific sections with potential issues based on content areas that are unclear, inconsistent, or outdated.
        3. Assign targeted tags from the outline to each Document Agent, specifying the exact sections they should analyze for potential issues.
        4. Task the Research Agent with identifying external discussions, criticisms, or feedback relevant to the assigned sections.
        5. Synthesize findings into a report focused solely on identifying areas for improvement. Do not provide solutions or recommendations.

        When using the get_outline tool:
        - Only identify sections that are likely to contain gaps or ambiguities, not the entire document structure.
        - Ensure that the agents work only on the assigned tags as specified.
    """),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
    enable_agentic_context=True,
    show_members_responses=True,
    response_model=InformationGatheringTeamOutput,
    success_criteria="A targeted analysis report identifying potential areas for improvement in the FAS based solely on assigned sections and external content."
)

fas_research_team.print_response(message="Please analyze the FAS 28 standard for Murabaha operations. Focus solely on identifying areas where the standard could be improved.", stream=True)