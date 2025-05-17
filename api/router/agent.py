from fastapi import APIRouter

router = APIRouter()

from src.models.input import ScenarioJournalingInput, FASDetectionInput
from src.models.output import ScenarioAgentOutput, FASDetectionOutput

from src.agent.scenario.orchestrator import create_journal
from src.agent.detection.agent import detect_fas

from examples.scenario import ijara_1
from examples.detection import journal_1, journal_2, journal_3, journal_4

@router.post("/scenario-journaling", response_model=ScenarioAgentOutput)
def create_journal_service(scenario: ScenarioJournalingInput = ScenarioJournalingInput(scenario=ijara_1)) -> ScenarioAgentOutput:
    return create_journal(scenario=scenario.scenario)

@router.post("/fas-detection", response_model=FASDetectionOutput)
def detect_fas_service(journal: FASDetectionInput = FASDetectionInput(journal=journal_2)) -> FASDetectionOutput:
    return detect_fas(journal=journal.journal)