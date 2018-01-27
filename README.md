QRCode to HTML demo
原理是使用python的qrcode模块生成特定图片再进行处理生成HTML文本。代码基于python3.5，需要先安装好numpy和qrcode模块。
修改代码中的data变量，运行后打开生成的QRcode.html
显示效果如图
![效果](http://otskc31jo.bkt.clouddn.com/AEE%5BBS8%5B5R%28GX%60TRDG1$FS6.png "效果")  
那么既然是想显示二维码为什么不直接用图片呢？
这样的二维码是基于HTML文本的，这样可以实现特别的效果，比如用js控制一点点的显示二维码出现。如网页：http://withzz.cn/html/info.html 的效果。
