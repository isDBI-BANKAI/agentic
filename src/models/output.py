from typing import List
from pydantic import BaseModel

class ScenarioAgentOutput(BaseModel):
    reasoning: str
    references: List[str]
    calculations: List[str]
    journal: str   
      
class FASOutput(BaseModel):
    index: int
    name: str
    probability: float

class FASDetectionOutput(BaseModel):
    reasoning: str
    references: List[str]
    detections: List[FASOutput]
    
class InformationGatheringTeamOutput(BaseModel):
    improvement_areas: list[str]
    websites_informations: str
    gathered_informations: str

class ReasonningAndSuggestionsTeamOutput(BaseModel):
    improvemets_list: list[str]
    
class ComplianceCheckTeamOutput(BaseModel):
    final_verdict: str
    final_improvements: str
 