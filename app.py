import streamlit as st
from skimage.io import imread, imshow
from skimage.transform import rotate

st.write("Raspberry Pi Camera Pseudo Zoom Helper")

image_path = st.file_uploader("Choose an image", type = "jpg")

if image_path is not None:

  image = rotate(imread(image_path), 180)
  x = st.number_input("x", min_value = 0.0, max_value = 1.0, value = .2, step = 0.01)
  y = st.number_input("y", min_value = 0.0, max_value = 1.0, value = .2, step = 0.01)
  w = st.number_input("w", min_value = 0.0, max_value = 1.0, value = .7, step = 0.01)
  h = st.number_input("h", min_value = 0.0, max_value = 1.0, value = .8, step = 0.01)

  col1, col2 = st.columns(2)
  col1.image(image, caption = 'Original')
  col2.image(image[int(720*x):int(720*w), int(1280*y):int(1280*h), 0:3], caption = 'Pseudo Zoom')
