import cv2
import numpy as np
from tensorflow import keras
from keras.models import load_model
import imutils
from model import *

classes = np.arange(0, 10)

model = load_model('model-OCR.h5')
# print(model.summary())
input_size = 48