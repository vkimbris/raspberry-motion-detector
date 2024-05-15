from pydantic import BaseModel
from typing import List


class Frame(BaseModel):
    datetime: int
    frame: List[List[List[int]]]