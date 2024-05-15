import json

from .models import Frame


def save_frame_to_json(frame: Frame) -> None:
    with open("data/last_frame.json", "w") as f:
        json.dump(frame.dict(), f)


def load_frame_from_json() -> dict:
    with open("data/last_frame.json", "r") as f:
        frame = json.load(f)

    return frame
