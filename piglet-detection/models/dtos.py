from typing import List
from pydantic import BaseModel, validator


class BoundingBoxClassification(BaseModel):
    class_id: int
    min_x: float
    min_y: float
    max_x: float
    max_y: float
    confidence: float

    @validator('min_x', 'min_y', 'max_x', 'max_y', 'confidence')
    def must_be_between_zero_one(cls, v):
        if v < 0.0 or v > 1.0:
            raise ValueError(
                f'Value must be between 0 or 1 ({v} given).')
        return v

    @validator('class_id')
    def must_be_binary(cls, v):
        if v not in [0, 1]:
            raise ValueError(
                f'Value must be either 0 or 1 ({v} given).')
        return v

    def __str__(self):
        class_str = 'pig   ' if self.class_id == 0 else 'piglet'
        class_confidence = f'{self.confidence*100:.5f}%'
        x = f'{self.min_x:.2f} - {self.max_x:.2f}'
        y = f'{self.min_y:.2f} - {self.max_y:.2f}'
        return f'Class: {class_str} ({class_confidence}), X: {x}, Y: {y}.'


class PredictRequestDto(BaseModel):
    img: str


class PredictResponseDto(BaseModel):
    boxes: List[BoundingBoxClassification]
