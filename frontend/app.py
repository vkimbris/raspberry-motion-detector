import streamlit as st
import time
import requests
import json
import numpy as np

from io import BytesIO

from src.tools import *

st.title('Ниже будет детектирована бабка')

FRAME_ENDPOINT = "http://backend:8000/frame"
DETECT_ENDPOINT = "http://backend:8000/detect"


image_placeholder = st.empty()
text_placeholder = st.empty()


def render():
    frame, label = get_frame_from_backend(FRAME_ENDPOINT)

    image_placeholder.image(frame)
    text_placeholder.text("Есть" if label == 1 else "Отсутствует")


while True:
    render()
