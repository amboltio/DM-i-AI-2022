from typing import List, IO
from pydantic import BaseModel
from fastapi import UploadFile


class PigletPredictRequestDto(UploadFile):
    def __init__(self, filename: str, file: IO = None, content_type: str = "") -> None:
        super().__init__(filename, file=file, content_type=content_type)


class PigletPredictResponseDto(BaseModel):
    boxes: List[List[int]]
    isPiglet: List[bool]
