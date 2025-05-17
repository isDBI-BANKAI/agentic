from agno.agent import Agent
from agno.team.team import Team
from agno.models.openai import OpenAIChat
from textwrap import dedent
from pydantic import BaseModel
from src.llm.llm import OpenAILLM
from agno.models.google import Gemini
from src.config.keys import GEMINI_API_KEY
from src.config.config import GEMINI_MODEL_NAME
from src.config.keys import OPENAI_API_KEY
from src.config.config import OPENAI_LLM_MODEL
from src.tools.retrieval import get_outline, retrieve  # Assuming same tools work for SS

# Agent 1: Compliance Checker 1
checker_1 = Agent(
    name="Compliance_Checker_1",
    role="Compliance Analyst",
    model=OpenAILLM().get_openai_chat(),
    tools=[retrieve],
    instructions=dedent("""
        You are tasked with analyzing specific suggestions for FAS improvement in accordance with SS (Islamic Standards).
        - Use the retrieve tool to extract relevant sections from the SS document.
        - Assess each suggestion for compliance, identifying potential inconsistencies or areas requiring clarification.
        - Provide a clear and concise justification for each determination.
        - Coordinate with Compliance_Checker_2 to achieve consensus where necessary.
    """),
    show_tool_calls=True,
    markdown=True
)

# Agent 2: Compliance Checker 2
checker_2 = Agent(
    name="Compliance_Checker_2",
    role="Compliance Analyst",
    model=OpenAILLM().get_openai_chat(),
    tools=[retrieve],
    instructions=dedent("""
        You are tasked with analyzing specific suggestions for FAS improvement in accordance with SS (Islamic Standards).
        - Use the retrieve tool to extract relevant sections from the SS document.
        - Assess each suggestion for compliance, identifying potential inconsistencies or areas requiring clarification.
        - Provide a clear and concise justification for each determination.
        - Coordinate with Compliance_Checker_1 to achieve consensus where necessary.
    """),
    show_tool_calls=True,
    markdown=True
)

# Team Leader / Judge
compliance_team_leader = Team(
    name="Compliance_Check_Team",
    members=[checker_1, checker_2],
    model=OpenAILLM().get_openai_chat(),
    mode="coordinate",
    tools=[get_outline, retrieve],
    instructions=dedent("""
        You are the Team Leader responsible for coordinating a comprehensive compliance assessment of FAS suggestions against SS (Islamic Standards). 📜

        Workflow:
        1. Scrape the SS outline using the get_outline tool to understand the structure and key sections.
        2. Assign relevant sections to each Compliance Checker based on the nature of the suggestions.
        3. Monitor and consolidate responses from the Checkers, ensuring consistency in compliance assessment.
        4. Resolve discrepancies through consensus-driven discussion and clarification requests as needed.
        5. Produce a final compliance report that includes:
            - A summary of compliant suggestions with rationale.
            - A list of flagged suggestions requiring further review or clarification.

        Focus solely on compliance evaluation based on SS sections. Refrain from suggesting amendments or editorial changes to the content.
    """),
    show_tool_calls=True,
    markdown=True,
    enable_agentic_context=True,
    success_criteria="A consolidated compliance report derived from SS sections, backed by consensus among the agents."
)


if __name__ == "__main__":
    fas_28_issues = """
    ## FAS 28: Areas for Potential Improvement

    This report identifies potential areas for improvement in AAOIFI Financial Accounting Standard 28 (FAS 28) based on the analysis of specific sections and external research. It focuses solely on highlighting potential issues and does not offer solutions or recommendations.

    ### 1. Definitions

    * **Lack of Specificity in "Control":** The definition of "Control" lacks specific conditions, making it vague. The phrase "duly meeting certain conditions" requires further clarification to ensure consistent application.
    * **Context for "Hamish Jiddiyyah":** The definition of "Hamish Jiddiyyah" may need additional context to fully understand its purpose and application within Murabaha transactions.
    * **Inconsistencies in Islamic Finance Terms:** The analysis reveals discussions on inconsistencies in interpreting Islamic finance terms across different jurisdictions, which, while not specific to FAS 28, suggests a potential area of ambiguity when applying the standard internationally.

    ### 2. Revenue and Profit Recognition

    * **Unclear Connection Between Paragraphs:** Paragraph 21's reference to paragraph 8 is unclear, hindering the understanding of revenue and receivables recognition.
    * **Missing Rationale for Profit Deferral:** Paragraph 23 lacks a clear rationale for deferring profit in deferred payment Murabaha, potentially leading to inconsistent application.
    * **Implications of Contra-Asset Presentation:** Paragraph 24 doesn't fully elaborate on the implications of presenting the deferred profit account as a contra-asset, potentially causing confusion in financial statement presentation.   
    * **Clarity on "Time Proportion Basis":** Paragraph 25 could benefit from clarifying what constitutes a "time proportion basis" for amortizing deferred profit.
    * **Missing FAS Reference During Defaults:** Paragraph 28 lacks a specific FAS reference for the treatment of deferred profit during defaults, creating uncertainty in such scenarios.
    * **Challenges in Profit Allocation:** External research reveals concerns about the complexities of determining profit allocation, especially when dealing with variable costs or delayed payments.

    ### 3. Presentation and Disclosures

    * **Assumed Knowledge of FAS 1:** Paragraph 39 and 50 assume prior knowledge of FAS 1, potentially limiting the accessibility of FAS 28 for users unfamiliar with that standard.
    * **Adequacy of Disclosures:** There are concerns about the adequacy of current disclosure practices in conveying the specific risks and characteristics of Islamic financial transactions to investors unfamiliar with Shariah-compliant finance.
    * **Ensuring Sufficient Information:** Ensuring that disclosures under FAS 28 are sufficiently informative for a general audience can present a challenge for practitioners. The level of detail required for disclosures might not be clear, potentially leading to inconsistencies in reporting across different entities and the terminology used in the presentation requirements may be open to interpretation, causing confusion. It might be challenging to consistently apply the presentation requirements across different types of Islamic financial transactions and the standard could lack specific guidance on how to present information when multiple types of Islamic financial transactions are involved. The cost of gathering and presenting the required disclosures may outweigh the benefits for smaller institutions or simpler transactions and The format and structure of required disclosures may not align well with existing reporting systems, leading to implementation challenges.

    ### 4. Scoping out – Tawarruq and commodity Murabaha

    * **Lack of Clarity on Exclusion Rationale:** The reasons for excluding Tawarruq and commodity Murabaha transactions are not clearly defined. The terms "substantial economic activity" and deviations from Shari'ah standards require further explanation.
    * **Context for Tawarruq Discouragement:** The statement about the Shari’ah standard discouraging Tawarruq's common use requires more context to understand its implications for accounting treatment.
    * **Legitimacy and Acceptance:** The debate around whether Tawarruq truly adheres to the spirit of Islamic finance and its potential use for regulatory arbitrage might indirectly impact the perceived legitimacy and acceptance of accounting treatments for Tawarruq, creating challenges for practitioners. The criteria for "scoping out" Tawarruq and commodity Murabaha transactions might be ambiguous, leading to inconsistent application and the definition of "genuine" versus "artificial" transactions in this context may be unclear. There may be inconsistencies in how similar transactions are treated based on subtle differences in their structure, potentially leading to "form over substance" issues and determining whether a Tawarruq or commodity Murabaha transaction falls within the scope of FAS 28 might require significant judgment and resources, potentially hindering its practical application. The lack of clear examples or illustrations could add to the difficulty.

    ### 5. Accounting for the buyer – profit element in the asset value

    * **Lack of Specific Examples:** The discussion around "mirror accounting" and "over-pricing" lacks specific examples or scenarios to illustrate the concepts.
    * **Elaboration on Justifications:** The justifications for deferring profit in the seller's hand need to be elaborated on to explain why they are not applicable to the buyer.
    * **Asset Valuation and Recognition:** The main issue for the buyer revolves around determining the fair value of the asset acquired and ensuring proper asset recognition, which underscores the need for clear guidance on asset valuation and recognition in the context of Murabaha transactions. The guidance on determining the appropriate profit element to be included in the asset value may not be sufficiently clear, particularly in complex transactions. The standard's treatment of profit elements that are contingent on future events could lack clarity and different interpretations of the "profit element" could lead to inconsistencies in asset valuation across different entities. The interaction between the profit element and other accounting principles (e.g., impairment) might not be consistently applied. Calculating and allocating the profit element to the asset value might be complex and time-consuming, especially for transactions with multiple components or extended payment terms and the practical application of these rules in situations with fluctuating commodity prices or market conditions could be challenging.

    These identified areas represent potential weaknesses or gaps within FAS 28 that could benefit from further review and clarification to enhance the standard's clarity, consistency, and practical applicability.
    """
    compliance_team_leader.print_response(fas_28_issues)