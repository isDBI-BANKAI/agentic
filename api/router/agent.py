from fastapi import APIRouter

router = APIRouter()

from src.models.input import ScenarioJournalingInput, FASDetectionInput, FASEnhancementInput
from src.models.output import ScenarioAgentOutput, FASDetectionOutput, FASEnhancementOutput

from src.agent.scenario.orchestrator import create_journal
from src.agent.detection.agent import detect_fas
from src.agent.enhancement.enhacement_env import enhance_fas

from examples.scenario import ijara_1
from examples.detection import journal_1, journal_2, journal_3, journal_4
from examples.enhancement import fas_28_to_enhance

@router.post("/scenario-journaling", response_model=ScenarioAgentOutput)
def create_journal_service(scenario: ScenarioJournalingInput = ScenarioJournalingInput(scenario=ijara_1)) -> ScenarioAgentOutput:
    return create_journal(scenario=scenario.scenario)

@router.post("/fas-detection", response_model=FASDetectionOutput)
def detect_fas_service(journal: FASDetectionInput = FASDetectionInput(journal=journal_2)) -> FASDetectionOutput:
    return detect_fas(journal=journal.journal)

@router.post("/fas-enhancement", response_model=FASEnhancementOutput)
def detect_fas_service(fas_to_enhance: FASEnhancementInput = FASEnhancementInput(instruction=fas_28_to_enhance)) -> FASEnhancementOutput:
    return enhance_fas(fas_to_enhance=fas_to_enhance)