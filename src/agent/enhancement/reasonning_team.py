from agno.agent import Agent
from agno.team.team import Team
from agno.models.openai import OpenAIChat
from textwrap import dedent
from src.llm.llm import OpenAILLM
from src.models.output import ReasonningAndSuggestionsTeamOutput
from agno.models.google import Gemini
from src.config.keys import GEMINI_API_KEY
from src.config.config import GEMINI_MODEL_NAME
from src.config.keys import OPENAI_API_KEY
from src.config.config import OPENAI_LLM_MODEL


# Agent 1: Gatherer 1
gatherer_1 = Agent(
    name="Gatherer_1",
    role="Improvement Ideas Analyst",
    model=Gemini(
        id=GEMINI_MODEL_NAME,
        api_key=GEMINI_API_KEY
    ),
    instructions=dedent("""
        You are a meticulous analyst specializing in identifying areas of potential improvement in financial accounting standards.
        - Scrutinize the assigned content methodically, identifying gaps, ambiguities, or areas lacking clarity.
        - Ensure that identified areas are communicated clearly to the team lead and Gatherer_2 for consolidation.
        - Maintain ongoing communication to align on findings and refine outputs collaboratively.
        - Await further instructions from the team lead to confirm when consolidation is required and how to proceed.
    """),
    show_tool_calls=True,
    markdown=True
)

# Agent 2: Gatherer 2
gatherer_2 = Agent(
    name="Gatherer_2",
    role="Improvement Ideas Analyst",
    model=Gemini(
        id=GEMINI_MODEL_NAME,
        api_key=GEMINI_API_KEY
    ),
    instructions=dedent("""
        You are a focused analyst tasked with identifying potential gaps and areas for refinement in financial accounting standards.
        - Analyze the assigned sections with precision, identifying inconsistencies, unclear guidance, or gaps.
        - Communicate findings clearly to the team lead and Gatherer_1 to facilitate effective consolidation.
        - Stay aligned with team directives, awaiting confirmation from the team lead before proceeding with further actions.
        - Maintain open channels with Gatherer_1 to ensure findings are consistently structured and aligned.
    """),
    show_tool_calls=True,
    markdown=True
)

# Team Leader
reasoning_team_leader = Team(
    name="Reasoning_And_Suggestions_Team",
    members=[gatherer_1, gatherer_2],
    model=Gemini(
        id=GEMINI_MODEL_NAME,
        api_key=GEMINI_API_KEY
    ),
    mode="coordinate",
    instructions=dedent("""
        As the lead coordinator for improvement analysis, your role is to effectively distribute and consolidate improvement suggestions.
        1. Analyze the initial list of suggestions and divide them into distinct sections, assigning each section to a specific gatherer.
        2. Communicate assignments clearly to each gatherer, specifying the areas they are responsible for analyzing.
        3. Receive and evaluate the suggestions from both gatherers, ensuring consistency and clarity in structure.
        4. Classify the gathered suggestions into structured categories, removing redundancies and refining the language for clarity.
        5. Deliver a final, consolidated list of categorized suggestions, maintaining a logical flow and ensuring all sections are covered comprehensively.
    """),
    show_tool_calls=True,
    success_criteria=dedent("""
        - Division of Work: Suggestions are effectively divided and assigned to the appropriate gatherer based on content relevance.
        - Completeness: All sections are thoroughly analyzed, with no overlooked suggestions.
        - Classification: Suggestions are categorized systematically, facilitating easier review and application.
        - Consistency: The tone and structure of suggestions align across both gatherers, ensuring uniformity.
        - Clarity: The final output is clearly structured, with suggestions presented in a concise and organized manner.
    """),
    markdown=True
)


if __name__ == "__main__":
    fas_enhancement_suggestions_example = """
        Consolidated Areas for Improvement in FAS 28 – Murabaha Operations

        1. Definitions
        - Fair Value:
        - Determining fair value is difficult in Islamic financial contexts due to illiquid markets.
        - IFRS 13's use for fair value raises debates over its suitability for Islamic finance.
        - Accurate, Shari'ah-compliant fair value measurement remains a challenge.

        2. Revenue and Profit Recognition
        - Effective Profit Rate Method & Straight Line Allocation:
        - These concepts are insufficiently explained, leading to inconsistent application.
        - More examples are needed to clarify how these methods work in practice.

        - General Revenue Recognition:
        - Challenges arise when applying IFRS 15 principles to Islamic financial contracts.
        - IFRS 9 is applied instead of IFRS 15 in trade-based Islamic contracts, which may require justification or clearer alignment.

        3. Accounting for Defaults
        - The standard lacks a robust framework for default scenarios.
        - Islamic banks cannot charge late fees, making loss recovery more difficult.
        - More detailed and practical guidance is needed on recognizing and handling defaults.

        4. Hamish Jiddiyyah and Arboun
        - The distinction between these two concepts is not sufficiently clear in seller and buyer contexts.
        - Practical examples are missing.
        - The accounting treatments may lead to inconsistencies without further clarification.

        5. NRV (Net Realisable Value)
        - While no major issues were noted, further exploration is recommended to ensure consistent application in Islamic finance.

        6. Scoping Out – Tawarruq and Commodity Murabaha
        - Though no specific external criticisms were found, this area warrants more detailed justification and research due to its unique Shari'ah considerations.
    """
    fas_reasoned_enhancement = reasoning_team_leader.print_response(fas_enhancement_suggestions_example)
