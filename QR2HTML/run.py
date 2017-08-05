from PIL import Image
import numpy as np
import qrcode

#可以放上你的各种链接
data = '一些有趣的东西'
#设置qrcode相关参数
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    # 这里将二维码最小像素设为1个像素便于处理
    box_size=1,
    # 边框设为1个像素，这里随意
    border=1
)
#生成二维码图片
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image()
#将图片变成灰度矩阵，img转换后矩阵里面不是255就是0
img2=np.array(img.convert('L'))
#定义一个字典方便生成字符串
d={255:'█',0:'&emsp;'}
#注意这里的样式颜色字体很关键
li=['<html><head><meta charset="utf-8"/><style>body{background-color: black;}#info{color: #c0c0c0;font-family: "新宋体";}</style><body><div id="info">']
#遍历每个像素生成html文本
rows,cols=img2.shape
for i in range(rows):
    a=''
    for j in range(cols):
        a+=d[img2[i,j]]
    a+='<br>'
    li+=[a]
li+=['</div></body></html>']
#写入文件
f=open("QRcode.html","w",encoding='utf8')
f.writelines(li)
f.close()
