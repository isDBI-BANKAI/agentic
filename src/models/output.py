from typing import List
from pydantic import BaseModel

class ScenarioAgentOutput(BaseModel):
    reasoning: str
    references: List[str]
    calculations: List[str]
    journal: str
