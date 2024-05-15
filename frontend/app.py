import streamlit as st
import time
import requests
import json
import numpy as np

from src.tools import *

st.title('Ниже будет детектирована бабка')

IMAGE_ENDPOINT = "http://backend:8000/image"
CLASSIFY_ENDPOINT = "http://backend:8000/classify"


image_placeholder = st.empty()
text_placeholder = st.empty()


def render():
    frame = get_request_to_backend(IMAGE_ENDPOINT)
    label = get_request_to_backend(CLASSIFY_ENDPOINT)["label"]

    if len(frame["frame"]) > 0:
        image = convert_frame_to_image(frame["frame"])

        image_placeholder.image(image)
        text_placeholder.text(f"Бабка {label}")


while True:
    render()
