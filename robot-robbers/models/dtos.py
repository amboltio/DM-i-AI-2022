from pydantic import BaseModel
from typing import List


class RobotRobbersPredictRequestDto(BaseModel):
    state: List[List[List[int]]]
    reward: float
    is_terminal: bool
    total_reward: float
    game_ticks: int


class RobotRobbersPredictResponseDto(BaseModel):
    moves: List[int]
