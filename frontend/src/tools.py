import json
import requests
import numpy as np

from PIL import Image
from io import BytesIO

from typing import Tuple


def get_frame_from_backend(endpoint: str):
    response = requests.get(url=endpoint)

    frame_bytes = response.content
    label = response.headers["label"]

    return Image.open(BytesIO(frame_bytes)), int(label)

