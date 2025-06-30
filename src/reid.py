# src/reid.py

import torch
import torchvision.transforms as T
from torchvision.models import resnet18
from torch.nn.functional import normalize

import cv2

class ReIDModel:
    def __init__(self, device='cpu'):
        self.device = device
        self.model = resnet18(pretrained=True)
        self.model.fc = torch.nn.Identity()  # Remove final classifier
        self.model.eval().to(device)

        self.transform = T.Compose([
            T.ToPILImage(),
            T.Resize((128, 64)),
            T.ToTensor(),
            T.Normalize(mean=[0.485, 0.456, 0.406],
                        std=[0.229, 0.224, 0.225]),
        ])

    def extract_embedding(self, image):
        img = self.transform(image).unsqueeze(0).to(self.device)
        with torch.no_grad():
            feat = self.model(img)
        return normalize(feat, dim=1).cpu().numpy()[0]
