from pydantic import BaseModel

class ScenarioJournalingInput(BaseModel):
    scenario: str
    
class FASDetectionInput(BaseModel):
    journal: str
    
class FASEnhancementInput(BaseModel):
    fas_to_enhance: str