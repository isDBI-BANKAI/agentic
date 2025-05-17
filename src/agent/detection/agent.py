from agno.agent import Agent, RunResponse

from agno.knowledge.website import WebsiteKnowledgeBase
from agno.tools.reasoning import ReasoningTools
from src.tools.retrieval import get_outline, retrieve

from src.llm.llm import OpenAILLM, GeminiLLM

from src.prompt.detection.prompt import get_system_prompt, get_system_prompt_online
from src.models.output import FASDetectionOutput
from examples.detection import journal_1, journal_2, journal_3, journal_4

from pprint import pprint

# knowledge_base = WebsiteKnowledgeBase(
#     urls=["https://aaoifi.com/accounting-standards-2/?lang=en"],
#     max_links=3,
#     vector_db=None
# )

agent = Agent(
    name="Reverse Transactions Agent",
    model=OpenAILLM().get_openai_chat(),
    # model = GeminiLLM.get_gemini_chat(),
    instructions=get_system_prompt(),
    tools=[
        ReasoningTools(),
        # get_outline,
        retrieve,
    ],
    response_model=FASDetectionOutput,
    show_tool_calls=True,
    markdown=True,
)
# agent.knowledge.load(recreate=False)

def detect_fas(journal: str, verbose: bool = False) -> FASDetectionOutput:
    if verbose:
        detection = agent.run(journal, stream=True, stream_intermediate_steps=True)
    else:
        detection = agent.run(journal, stream=False)
    return detection.content

if __name__ == "__main__":
    # for i, journal in enumerate([journal_1, journal_2, journal_3, journal_4], start=1):
    for i, journal in enumerate([journal_4], start=4):
        print(f"Journal {i}: {journal}")
        detection = detect_fas(journal)
        pprint(detection.model_dump())
        print("\n" + "="*50 + "\n")