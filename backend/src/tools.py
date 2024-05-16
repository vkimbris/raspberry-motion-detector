from PIL import Image
from io import BytesIO


def predict(object_detector, frame_in_bytes) -> int:
    frame = Image.open(BytesIO(frame_in_bytes))

    results = object_detector(frame).pandas().xyxy[0]

    return int("person" in results.name.values)
