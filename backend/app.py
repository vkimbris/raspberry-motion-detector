import torch

from fastapi import FastAPI, Request, UploadFile, File, Response

from src.tools import *

from PIL import Image
from io import BytesIO

app = FastAPI()


object_detector = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/receiveFrame")
def receive_image(file: UploadFile = File(...)):    
    global CURRENT_FRAME_IN_BYTES

    frame_in_bytes = file.file.read()
    
    CURRENT_FRAME_IN_BYTES = frame_in_bytes
    
    return {"status": "ok"}


@app.get("/frame")
def get_image():
    label = predict(object_detector, CURRENT_FRAME_IN_BYTES)
    
    frame = Response(content=CURRENT_FRAME_IN_BYTES, media_type="image/png", headers={"label": str(label)})
   
    return frame