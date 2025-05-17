from typing import List
from pydantic import BaseModel

class ScenarioAgentOutput(BaseModel):
    reasoning: str
    references: List[str]
    calculations: List[str]
    journal: str
# challenge 3 diffrent teams output
# Team1     
class InformationGatheringTeamOutput(BaseModel):
    improvement_areas: list[str]
    websites_informations: str
    gathered_informations: str
# Team2
class ReasonningAndSuggestionsTeamOutput(BaseModel):
    improvemets_list: list[str]
# Team3
class ComplianceCheckTeamOutput(BaseModel):
    final_verdict: str
    final_improvements: str
    