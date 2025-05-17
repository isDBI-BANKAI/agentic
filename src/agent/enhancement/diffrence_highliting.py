from agno.agent import Agent
from agno.team.team import Team
from typing import List, Dict, Any
from textwrap import dedent
from src.models.output import ImplementationTrackingTeamOutput
from agno.tools.duckduckgo import DuckDuckGoTools
from src.tools.retrieval import get_outline, retrieve
from agno.models.google import Gemini
from src.config.keys import OPENAI_API_KEY, GEMINI_API_KEY
from src.config.config import OPENAI_LLM_MODEL, GEMINI_MODEL_NAME

# Define new tools for tracking changes
from agno.tools import tool
from src.tools.log import logger_hook

@tool(
    name="get_suggestions",
    description="Get Shariah-compliant suggestions for specific FAS sections",
    show_result=True,
    stop_after_tool_call=False,
    tool_hooks=[logger_hook],
    cache_results=False
)
def get_suggestions(section_tag: str = None) -> list[dict]:
    """
    Get Shariah-compliant suggestions for FAS sections.
    
    Args:
        section_tag: Optional tag to filter suggestions for a specific section
        
    Returns:
        list[dict]: List of suggestions with section_tag, original_text, and suggested_change
    """
    # This function would retrieve suggestions from your database
    # Placeholder implementation
    return [{"section_tag": section_tag, "original_text": "Sample text", "suggested_change": "Improved text"}]

@tool(
    name="get_original_content",
    description="Get original content of FAS sections before changes",
    show_result=True,
    stop_after_tool_call=False,
    tool_hooks=[logger_hook],
    cache_results=False
)
def get_original_content(section_tag: str) -> str:
    """
    Get original content of FAS sections before changes.
    
    Args:
        section_tag: Tag of the section to retrieve
        
    Returns:
        str: Original content of the section
    """
    # This function would retrieve original content from your database
    # Placeholder implementation
    return "Original content for section " + section_tag

# Create change tracking agents
change_tracker_1 = Agent(
    name="Change_Tracker_1",
    role="Shariah Compliance Tracker",
    model=Gemini(
        id=GEMINI_MODEL_NAME,
        api_key=GEMINI_API_KEY
    ),
    tools=[retrieve, get_original_content, get_suggestions],
    instructions=dedent("""
        Track Shariah-compliant changes in assigned FAS sections.
        
        Tasks:
        - Use retrieve to get current content via tags from the outline
        - Compare with original content
        - Match changes to Shariah-compliance suggestions
        - Note implementation status [FULL/PARTIAL/MODIFIED]
        
        Format:
        - "Section [X]: Changes" with before/after quotes
        - Use bullet points for changes
    """),
    show_tool_calls=True,
    markdown=True,
)

change_tracker_2 = Agent(
    name="Change_Tracker_2",
    role="Shariah Compliance Tracker",
    model=Gemini(
        id=GEMINI_MODEL_NAME,
        api_key=GEMINI_API_KEY
    ),
    tools=[retrieve, get_original_content, get_suggestions],
    instructions=dedent("""
        Track Shariah-compliant changes in assigned FAS sections.
        
        Tasks:
        - Use retrieve to get current content via tags from the outline
        - Compare with original content
        - Match changes to Shariah-compliance suggestions
        - Note implementation status [FULL/PARTIAL/MODIFIED]
        
        Format:
        - "Section [X]: Changes" with before/after quotes
        - Use bullet points for changes
    """),
    show_tool_calls=True,
    markdown=True,
)

# Create Shariah compliance verification agent
compliance_verifier = Agent(
    name="Compliance_Verifier",
    role="Shariah Compliance Expert",
    model=Gemini(
        id=GEMINI_MODEL_NAME,
        api_key=GEMINI_API_KEY
    ),
    tools=[retrieve, get_suggestions],
    instructions=dedent("""
        Verify that implemented changes maintain Shariah compliance.
        
        Tasks:
        - Check that implemented changes match Shariah committee suggestions
        - Verify that concepts in updated FAS match original Shariah intent
        - Track implementation rates by section
        
        Format:
        - "Compliance Summary" with implementation statistics
        - "Concept Preservation" analysis by section
    """),
    show_tool_calls=True,
    markdown=True,
)

# Create team leader to coordinate
implementation_tracking_team = Team(
    name="Shariah_Implementation_Team",
    members=[change_tracker_1, change_tracker_2, compliance_verifier], 
    model=Gemini(
        id=GEMINI_MODEL_NAME,
        api_key=GEMINI_API_KEY
    ),
    mode="coordinate",
    tools=[get_outline, retrieve, get_suggestions],
    instructions=dedent("""
        Track Shariah-compliant changes in FAS documents.
        
        Tasks:
        1. Get FAS document structure using get_outline
        2. Retrieve Shariah committee suggestions
        3. Assign sections to change trackers
        4. Direct compliance verifier to analyze concept preservation
        5. Create report with:
           - Implementation summary
           - Section-by-section changes
           - Concept preservation analysis
        
        Focus only on identifying changes, not making new suggestions.
    """),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
    enable_agentic_context=True,
    show_members_responses=True,
    success_criteria="A report identifying where Shariah-compliant changes were implemented, preserving original concepts."
)


if __name__ == "__main__":
    
    implementation_tracking_team.print_response("Analyze implemented changes to FAS 28 for Murabaha operations. Identify where changes were made based on Shariah compliance suggestions.")
