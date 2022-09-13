from pydantic import BaseModel, ValidationError, validator
from typing import List

class PigPredictRequestDto(BaseModel):
    img: str

class BoundingBoxClassification(BaseModel):
    class_id: int
    min_x: float
    min_y: float
    max_x: float
    max_y: float
    confidence: float

    @validator('class_id')
    def class_id_should_be_between_0_and_1(cls, v):
        if v not in [0, 1]:
            raise ValueError('not a valid class id. Must be 0 or 1')
        return v

    @validator('confidence')
    def confidence_should_be_between_0_and_1(conf, v):
        if v < 0 or v > 1:
            raise ValueError('not a valid confidence. Must be between 0 and 1')
        return v

class PigPredictResponseDto(BaseModel):
    boxes: List[BoundingBoxClassification]
