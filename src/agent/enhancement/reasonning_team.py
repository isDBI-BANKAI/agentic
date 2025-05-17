from agno.agent import Agent
from agno.team.team import Team
from agno.models.openai import OpenAIChat
from textwrap import dedent
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
    model=Gemini(
        id=GEMINI_MODEL_NAME,
        api_key=GEMINI_API_KEY
    ),
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
    model=Gemini(
        id=GEMINI_MODEL_NAME,
        api_key=GEMINI_API_KEY
    ),
    mode="coordinate",
    instructions=dedent("""
        You are the lead coordinator for gathering and refining improvement suggestions. 
        1. Assign each gatherer a subset of improvement areas to analyze.
        2. Ensure the gatherers communicate and consolidate their findings into a single, refined list.
        3. Return the consolidated list in the specified format, focusing only on potential improvement areas without recommendations or compliance analysis.
    """),
    show_tool_calls=True,
    markdown=True
)

def print_and_save_team_run_response(result):
        print("\n--- Member Responses ---")
        all_member_dicts = []

        if result.member_responses:
            for i, member in enumerate(result.member_responses):
                member_dict = member.to_dict()
                all_member_dicts.append(member_dict)

            return all_member_dicts
        else:
            return None
def extract_relevant_messages(all_member_dicts):
    data = all_member_dicts
    relevant_messages = []
    for entry in data:
        if 'messages' in entry:
            for message in entry['messages']:
                # Extract content from assistant, teamlead, and user roles
                role = message.get('role')
                content = message.get('content', '')
                agent_id = entry.get('agent_id', 'Unknown')

                # Handle content as a list or a string
                if isinstance(content, list):
                    content = "\n".join([str(item).strip() for item in content if item.strip()])
                elif isinstance(content, str):
                    content = content.strip()

                # Capture relevant roles
                if content and not content.startswith('<'):
                    if role in ['assistant', 'teamlead', 'user']:
                        relevant_messages.append({
                            'agent_id': agent_id,
                            'role': role,
                            'content': content
                        })

    return relevant_messages

if __name__ == "__main__":
    result = reasoning_team_leader.run("Please analyze the FAS 28 standard for Murabaha operations. Focus solely on identifying areas where the standard could be improved")
    members_dict = print_and_save_team_run_response(result=result)
    messages = extract_relevant_messages(members_dict)
    for msg in messages:
        print('------------')
        print(msg)
        print('------------')
    print(result.content)