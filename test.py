import streamlit as st
from PIL import Image
import base64

st.title('converting image to base64 string')

img_file=st.file_uploader('upload image',type=['png','jpg','jpeg'])
if img_file is not None:
    with open('test.png','wb') as f:
        f.write(img_file.getbuffer())
    st.image(Image.open(img_file),width=250)

    with open('test.png','rb') as f:
        img_data=f.read()
        img_base64=base64.b64encode(img_data).decode('UTF-8')
    
    st.success(img_base64)
