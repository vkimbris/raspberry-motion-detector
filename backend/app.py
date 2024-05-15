import torch

from fastapi import FastAPI, Request

from src.models import Frame
from src.tools import *
from src.motion_detector import MotionDetector

app = FastAPI()


motion_detector = MotionDetector()
motion_detector.load_state_dict(torch.load("trained_models/motion_detector_v1"))

label2id = {0: 'Cидит', 1: 'Лежит', 2: 'Отсутствует'}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/receiveImage")
def receive_image(frame: Frame):
    global CURRENT_FRAME
    
    CURRENT_FRAME = frame
    
    return {"status": "ok"}


@app.get("/classify")
def classification():
    prediction = predict(motion_detector, CURRENT_FRAME)
    
    return {"label": label2id[prediction]}


@app.get("/image")
def get_image():
    return CURRENT_FRAME if CURRENT_FRAME is not None else {"frame": []}
