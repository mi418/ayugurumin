import streamlit as st

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

import pickle

# from google.colab import drive
# drive.mount('/content/drive')

st.title("Hello World !")

img = cv2.imread('/content/drive/MyDrive/あみぐるみ/original_png.png') # 画像の読み出し
cv2_imshow(img)

f = open('/content/drive/MyDrive/あみぐるみ/dmc色/dic_color.txt',"rb")
dic_color = pickle.load(f)
