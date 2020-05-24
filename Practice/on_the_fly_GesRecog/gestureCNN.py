from __future__ import print_function, division

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
from PIL import Image

import torch.nn as nn
import torch.nn.functional as F

# class Net(nn.Module):
#     def __init__(self):
#         super(Net, self).__init__()
#         self.conv1 = nn.Conv2d(1, 32, 3)
#         self.pool = nn.MaxPool2d(2, 2)
#         self.conv2 = nn.Conv2d(32, 32, 3)
#         self.conv3 = nn.Conv2d(32, 128, 3)
#         # self.conv4 = nn.Conv2d(128, 3, 3)
#         self.fc1 = nn.Linear(128*23*23, 256)
#         self.fc2 = nn.Linear(256, 64)
#         self.fc3 = nn.Linear(64, 5)
    
#     def forward(self, x):
#         x = self.pool(F.relu(self.conv1(x)))
#         x = self.pool(F.relu(self.conv2(x)))
#         x = self.pool(F.relu(self.conv3(x)))
#         # x = self.pool(F.relu(self.conv4(x)))
#         x = x.view(-1, 128*23*23)
#         x = F.relu(self.fc1(x))
#         x = F.relu(self.fc2(x))
#         x = F.softmax(self.fc3(x), dim=1)
        
#         return x

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, 3)
        # self.conv3 = nn.Conv2d(32, 128, 3)
        # self.conv4 = nn.Conv2d(128, 3, 3)
        self.fc1 = nn.Linear(64*98*98, 128)
        # self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(128, 5)
    
    def forward(self, x):
        x = self.conv1(x)
        x = self.pool(F.relu(self.conv2(x)))
        # x = self.pool(F.relu(self.conv2(x)))
        # x = self.pool(F.relu(self.conv3(x)))
        # x = self.pool(F.relu(self.conv4(x)))
        x = x.view(-1, 64*98*98)
        x = F.relu(self.fc1(x))
        # x = F.relu(self.fc2(x))
        x = F.softmax(self.fc3(x), dim=1)
        
        return x
    
import json
import cv2 as cv


jsonarray = {}
classes = ['nothing', 'ok', 'palm', 'peace', 'punch']

def update(plot):
    global jsonarray
    h, y, w = 450, 30, 45
    font = cv.FONT_HERSHEY_COMPLEX
    
    for items in jsonarray:
        mul = (jsonarray[items])/100
        cv.line(plot, (0,y), (int(h*mul), y), (255,0,0), w)
        cv.putText(plot, items, (0,y+5), font, 0.7, (0,255,0), 2,1)
        y += w+30
        
    return plot

import numpy as np

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
# device = 'cpu'

def loadCNN():
    model = Net()
    model.load_state_dict(torch.load('optimal_params.pt'))
    return model


def guessGesture(model, img):
    global jsonarray, classes
    
    tfms = transforms.Compose([
        transforms.Grayscale(num_output_channels=1),
        transforms.ToTensor(),
        transforms.Normalize([0.5], [0.25])
    ])
    
    rimage = tfms(Image.fromarray(img)).to(device)
    rimage = torch.reshape(rimage, (1, 1, 200, 200))
    
    model.to(device)
    model.eval()
    
    preds = model(rimage)[0]
    
    d = {}
    i = 0 
    for items in classes:
        d[items] = preds[i]*100
        i += 1
        
    _, pred = torch.max(preds, 0)
    guess= classes[pred.item()]
    
    if d[guess] > 60.0:
        jsonarray = d
        
        return classes.index(guess)
    else:
        return 0
    
    