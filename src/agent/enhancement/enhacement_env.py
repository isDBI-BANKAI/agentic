from informations_team import fas_research_team 
from reasonning_team import reasoning_team_leader
from compliance_team import compliance_team_leader
from pydantic import BaseModel

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


gathered_info = fas_research_team.run("Please analyze the FAS 28 standard for Murabaha operations. Focus solely on identifying areas where the standard could be improved.")
gathered_info_dict = print_and_save_team_run_response(result=gathered_info)
gathered_info_messages = extract_relevant_messages(gathered_info_dict)

suggestions = reasoning_team_leader.run(gathered_info.content)
suggestions_dict = print_and_save_team_run_response(result=suggestions)
suggestions_messages = extract_relevant_messages(suggestions_dict)

compliance = compliance_team_leader.run(suggestions.content)
compliance_info_dict = print_and_save_team_run_response(result=compliance)
compliance_info_messages = extract_relevant_messages(compliance_info_dict)

print(compliance_info_messages)