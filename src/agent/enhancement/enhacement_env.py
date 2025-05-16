from informations_team import fas_research_team 
from reasonning_team import reasoning_team_leader
from compliance_team import compliance_team_leader
from pydantic import BaseModel

gathered_info = fas_research_team.run("Please analyze the FAS 28 standard for Murabaha operations. Focus solely on identifying areas where the standard could be improved.")

suggestions = reasoning_team_leader.run(gathered_info)

compliance_output = compliance_team_leader.run(suggestions)

# Final Output
print("Final Verdict:", compliance_output.final_verdict)
print("Final Improvements:", compliance_output.final_improvements)