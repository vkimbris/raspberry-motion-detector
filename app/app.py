from fastapi import FastAPI, Request
from pydantic import BaseModel

from typing import List


app = FastAPI()


class DataInput(BaseModel):
    datetime: int
    frame: List[List[List[int]]]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/receiveImage")
def receive_image(data: DataInput):
    return {"status": "ok"}
