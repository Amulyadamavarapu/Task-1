import streamlit as st
import base64
from PIL import Image
import requests
import json

api='https://uc64l1q8dg.execute-api.us-east-1.amazonaws.com/prod/recognition'
st.title('Serverlesss Image Recognition Engine')

img_file=st.file_uploader('upload image',type=['png','jpg','jpeg'])

if st.button('Invoke API'):
    if img_file is not None:
        with open('test.png','wb') as f:
            f.write(img_file.getbuffer())
        st.image(Image.open(img_file),width=250)
    
    with open('test.png','rb') as f:
        img_data=f.read()
        img_base64=base64.b64encode(img_data).decode('UTF-8')
    
    data={"image":img_base64}
    response=requests.post(api,json=data)
    response=json.loads(response.text)
    response=response["Labels"]
    for i in response:
        st.success(i['Name']+' ,'+str(i['Confidence']))