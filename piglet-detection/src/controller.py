import cv2
import random
import base64
import numpy as np
from typing import List
from loguru import logger
from fastapi import APIRouter
from src.dtos import PredictRequestDto, PredictResponseDto, BoundingBoxClassification


router = APIRouter()


@router.post('/predict', response_model=PredictResponseDto)
def predict_endpoint(request: PredictRequestDto):
    img: np.ndarray = decode_request(request)

    dummy_bounding_boxes = predict(img)
    response = PredictResponseDto(
        boxes=dummy_bounding_boxes
    )

    return response


def decode_request(request: PredictRequestDto) -> np.ndarray:
    encoded_img: str = request.img
    np_img = np.fromstring(base64.b64decode(encoded_img), np.uint8)
    return cv2.imdecode(np_img, cv2.IMREAD_ANYCOLOR)


def predict(img: np.ndarray) -> List[BoundingBoxClassification]:
    logger.info(f'Recieved image: {img.shape}')
    bounding_boxes: List[BoundingBoxClassification] = []
    for _ in range(random.randint(0, 9)):
        bounding_box: BoundingBoxClassification = get_dummy_box()
        bounding_boxes.append(bounding_box)
        logger.info(bounding_box)
    return bounding_boxes


def get_dummy_box() -> BoundingBoxClassification:
    random_class = random.randint(0, 1)  # 0 = PIG, 1 = PIGLET
    random_min_x = random.uniform(0, .9)
    random_min_y = random.uniform(0, .9)
    random_max_x = random.uniform(random_min_x + .05, 1)
    random_max_y = random.uniform(random_min_y + .05, 1)
    return BoundingBoxClassification(
        class_id=random_class,
        min_x=random_min_x,
        min_y=random_min_y,
        max_x=random_max_x,
        max_y=random_max_y,
        confidence=random.uniform(0, 1)
    )
