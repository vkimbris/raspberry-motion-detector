import torch
import torch.nn as nn


class MotionDetector(nn.Module):

    def __init__(self) -> None:
        super().__init__()

        self.resnet = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)

        self.linear = nn.Sequential(
            nn.Linear(1000, 200),
            nn.ReLU(),
            nn.Linear(200, 3)
        )

    def forward(self, x):
        return self.linear(self.resnet(x))
