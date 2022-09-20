import random
from fastapi import APIRouter
from models.dtos import SentimentAnalysisRequestDto, SentimentAnalysisResponseDto


router = APIRouter()


@router.post('/predict', response_model=SentimentAnalysisResponseDto)
def predict_endpoint(request: SentimentAnalysisRequestDto):

    predicted_scores = [random.randint(1,5) for _ in request.reviews]

    response = SentimentAnalysisResponseDto(
        scores=predicted_scores
    )

    return response
