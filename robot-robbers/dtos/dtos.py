from typing import List
from pydantic import BaseModel


class RobotRobbersPredictRequestDto(BaseModel):
    state: List[List[List[int]]]
    reward: float
    is_terminal: bool
    total_reward: float
    game_ticks: int


class RobotRobbersPredictResponseDto(BaseModel):
    moves: List[int]
