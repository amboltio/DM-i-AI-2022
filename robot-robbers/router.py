import numpy as np
from fastapi import APIRouter
from models.dtos import RobotRobbersPredictResponseDto, RobotRobbersPredictRequestDto


router = APIRouter()


@router.post('/predict', response_model=RobotRobbersPredictResponseDto)
def predict(request: RobotRobbersPredictRequestDto):
    # robots = [(x, y, w, h) for (x, y, w, h) in request.state[0] if x >= 0 and y >= 0]
    # scrooges = [(x, y, w, h) for (x, y, w, h) in request.state[1] if x >= 0 and y >= 0]
    # cashbags = [(x, y, w, h) for (x, y, w, h) in request.state[2] if x >= 0 and y >= 0]
    # dropspots = [(x, y, w, h) for (x, y, w, h) in request.state[3] if x >= 0 and y >= 0]
    # obstacles = request.state[4]

    # Your moves go here!
    n_robbers = 5
    moves = [np.random.randint(-1, 2) for _ in range(n_robbers * 2)]

    return RobotRobbersPredictResponseDto(
        moves=moves
    )
