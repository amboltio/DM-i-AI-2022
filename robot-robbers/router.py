import numpy as np
from fastapi import APIRouter
from models.dtos import RobotRobbersPredictResponseDto, RobotRobbersPredictRequestDto

router = APIRouter()


@router.post('/predict', response_model=RobotRobbersPredictResponseDto)
def predict(request: RobotRobbersPredictRequestDto):
    # robots = [x for x in request.state[0] if x[0] != -1]
    # scrooges = [x for x in request.state[1] if x[0] != -1]
    # cashbags = [x for x in request.state[2] if x[0] != -1]
    # dropspots = [x for x in request.state[3] if x[0] != -1]
    # obstacles = request.state[4]

    # Your moves go here!
    n_robbers = 5
    moves = [np.random.randint(-1, 2) for _ in range(n_robbers * 2)]

    return RobotRobbersPredictResponseDto(
        moves=moves
    )
