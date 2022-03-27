import streamlit as st

import cv2
import numpy as np

import openpyxl
import datetime

#提案ボタンの動的処理のために挿入
if 'count' not in st.session_state: 
    st.session_state.count = 'NotProp' #countがsession_stateに追加されていない場合，0で初期化
st.write(st.session_state.count)
    
    
befor_after_png = cv2.imread('befor_after_png.png') # 画像の読み出し
st.image(befor_after_png, channels="BGR")

img_col = cv2.imread('coler_png.png') # 画像の読み出し
st.image(img_col, channels="BGR")

img = cv2.imread('original_png.png') # 画像の読み出し
# st.image(img, channels="BGR")


dic_color = np.load('dic_color.npy', allow_pickle='TRUE')
dic_color=dic_color.item()


img_result = np.copy(img)

cl_num_list=list(dic_color.keys())
# selectbox
#face and body
face_num = st.selectbox('お顔とお腹の色は？',cl_num_list, key="face")
# st.write('You selected: ', face_num)
body_num=face_num
# ear
l_e_num = st.selectbox('お耳の色は？',cl_num_list, key="ear")
r_e_num=l_e_num
# hand　and leg
l_h_num = st.selectbox('手足の色は？',cl_num_list, key="hand")
r_h_num=l_h_num
l_l_num=l_h_num
r_l_num=l_h_num

# button
button_state = st.button('クマちゃん出力！', key="create")
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


  st.image(img_result, channels="BGR")
  st.session_state.img_result=img_result
  st.write(st.session_state.count)
  st.session_state.count = 'Prop'
  
if st.session_state.count=='Prop':
  st.write(st.session_state.count)
  
  # button
  button_state_proposal = st.button('提案する', key="proposal")
  if button_state_proposal:
    st.write('if button_state_proposal')
    wb = openpyxl.load_workbook('20220327_proposal_data.xlsx')
    sheet = wb.worksheets[0]

    st.write('sheet = wb.worksheets[0]')
    # 行データを追加と保存
    sheet.append([face_num,l_e_num,r_e_num
                  ,body_num,l_h_num,r_h_num,l_l_num,r_l_num
                  ,datetime.datetime.now()])
    st.write('append')
    wb.save('20220327_proposal_data.xlsx')  
    st.write('save')  
    st.image(st.session_state.img_result, channels="BGR")
    st.session_state.count = 'NotProp'

