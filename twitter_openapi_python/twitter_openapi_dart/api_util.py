import twitter_openapi_python_generated.models as models
from typing import List


def instructionToEntry(
    item: List[models.InstructionUnion],
) -> List[models.TimelineAddEntry]:
    entry: List[models.TimelineAddEntry] = []
    for i in item:
        pass
    return entry
