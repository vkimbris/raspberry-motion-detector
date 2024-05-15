import torch
import torch.nn as nn


class MotionDetector(nn.Module):

    def __init__(self, 
                 num_classes: int = 3,
                 in_channels: int = 3,
                 kernel_size: int = 5) -> None:
        
        super().__init__()

        self.conv = nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=10, kernel_size=kernel_size),
            nn.MaxPool2d(kernel_size=5),

            nn.Conv2d(in_channels=10, out_channels=3, kernel_size=3),
            nn.MaxPool2d(kernel_size=3),

            nn.Conv2d(in_channels=3, out_channels=1, kernel_size=3),
            nn.MaxPool2d(kernel_size=3)
        )

        self.linear = nn.Sequential(
            nn.Linear(117, 64),
            nn.ReLU(),
            nn.Linear(64, num_classes)
        )

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)

        return self.linear(x)
