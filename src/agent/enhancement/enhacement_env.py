from informations_team import fas_research_team 
from reasonning_team import reasoning_team_leader
from compliance_team import compliance_team_leader
from src.models.input import FASEnhancementInput
from src.models.output import FASEnhancementOutput
from examples.enhancement import fas_28_to_enhance
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

def enhance_fas(fas_to_enhance: FASEnhancementInput):
    enhancement_instructions = fas_to_enhance.instruction
    gathered_info = fas_research_team.run(enhancement_instructions)
    gathered_info_dict = print_and_save_team_run_response(result=gathered_info)
    gathered_info_messages = extract_relevant_messages(gathered_info_dict)
    suggestions = reasoning_team_leader.run(gathered_info.content)
    suggestions_dict = print_and_save_team_run_response(result=suggestions)
    suggestions_messages = extract_relevant_messages(suggestions_dict)
    compliance = compliance_team_leader.run(suggestions.content)
    compliance_info_dict = print_and_save_team_run_response(result=compliance)
    compliance_info_messages = extract_relevant_messages(compliance_info_dict)
    
    result = FASEnhancementOutput(
        info_gathering_team_output= gathered_info.content,
        info_gathering_team_messages= gathered_info_messages,
        
        suggestions_team_output= suggestions.content, 
        suggestions_team_messages= suggestions_messages,
        
        compliance_team_output= compliance.content, 
        compliance_team_messages= compliance_info_messages 
    )
    
    return result


if __name__ == "__main__":
    enhance_fas(fas_to_enhance=FASEnhancementInput(instruction=fas_28_to_enhance))