import base64

with open('download.jpg','rb') as f:
        img_data=f.read()
        img_base64=base64.b64encode(img_data).decode('UTF-8')
f=open('log.txt','w')
f.write(img_base64)
f.close()
