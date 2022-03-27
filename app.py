import streamlit as st

import cv2
import numpy as np

import pickle


st.title("Hello World !")

img = cv2.imread('original_png.png') # 画像の読み出し

dic_color = np.load('dic_color.npy', allow_pickle='TRUE')
dic_color=dic_color.item()


img_result = np.copy(img)

cl_num_list=list(dic_color.keys())
# selectbox
#face
face_num = st.selectbox(
    'select box:',cl_num_list)
st.write('You selected: ', face_num)
# ear
l_e_num = st.selectbox(
    'select box:',cl_num_list)
st.write('You selected: ', l_e_num)
r_e_num=l_e_num
# body
l_e_num = st.selectbox(
    'select box:',cl_num_list)
st.write('You selected: ', body_num)
# hand
l_e_num = st.selectbox(
    'select box:',cl_num_list)
st.write('You selected: ', l_h_num)
r_h_num=l_h_num
# leg
l_e_num = st.selectbox(
    'select box:',cl_num_list)
st.write('You selected: ', l_l_num)
r_l_num=l_l_num

# button
button_state = st.button('クマちゃん出力！')
if button_state:

  # 特定の色を別の色に置換する
  # お顔
  before_color=img[250, 250, :]
  after_color = dic_color[str(face_num)]
  img_result[np.where((img_result == before_color).all(axis=2))] = after_color
  # 左耳
  before_color=img[100, 100, :]
  after_color = dic_color[str(l_e_num)]
  img_result[np.where((img_result == before_color).all(axis=2))] = after_color
  # 右耳
  before_color=img[100, 400, :]
  after_color = dic_color[str(r_e_num)]
  img_result[np.where((img_result == before_color).all(axis=2))] = after_color
  # 体
  before_color=img[400, 250, :]
  after_color = dic_color[str(body_num)]
  img_result[np.where((img_result == before_color).all(axis=2))] = after_color
  # 左手
  before_color=img[350, 100, :]
  after_color = dic_color[str(l_h_num)]
  img_result[np.where((img_result == before_color).all(axis=2))] = after_color
  # 右手
  before_color=img[350, 400, :]
  after_color = dic_color[str(r_h_num)]
  img_result[np.where((img_result == before_color).all(axis=2))] = after_color
  # 左足
  before_color=img[500, 200, :]
  after_color = dic_color[str(l_l_num)]
  img_result[np.where((img_result == before_color).all(axis=2))] = after_color
  # 右足
  before_color=img[500, 350, :]
  after_color = dic_color[str(r_l_num)]
  img_result[np.where((img_result == before_color).all(axis=2))] = after_color


  st.image(img_result)
