import numpy as np
import torch.nn.functional as F

import torchvision.transforms as transforms

from .motion_detector import MotionDetector
from .models import Frame

from typing import List

from PIL import Image


convert_to_tensor = transforms.ToTensor()

def predict(model: MotionDetector, frame: Frame) -> str:
    frame = frame.frame

    frame = np.array(frame)
    frame = np.uint8(frame)

    image = Image.fromarray(np.array(frame))
    image = convert_to_tensor(image).transpose(1, 2).unsqueeze(0)

    print(image.shape)

    output = model(image)
    output = F.softmax(output, dim=-1)

    print(output)

    return output.argmax(dim=-1)[0].item()