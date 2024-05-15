from fastapi import FastAPI, Request

from src.models import Frame
from src.tools import save_frame_to_json, load_frame_from_json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/receiveImage")
def receive_image(frame: Frame):
    save_frame_to_json(frame)
    
    return {"status": "ok"}


@app.get("/image")
def get_image():
    frame = load_frame_from_json()

    print(frame)

    return frame
