from pydantic import BaseModel

class ScenarioJournalingInput(BaseModel):
    scenario: str
    
class FASDetectionInput(BaseModel):
    journal: str