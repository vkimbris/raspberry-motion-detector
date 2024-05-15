import json
import requests
import numpy as np

from PIL import Image

from typing import List


def get_frame_from_server(endpoint: str):
    response = requests.get(url=endpoint)

    return json.loads(response.text)


def convert_frame_to_image(frame: List[List[int]]):
    image_array = np.array(frame, dtype=np.uint8)

    return Image.fromarray(image_array)