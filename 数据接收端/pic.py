# 对图像的处理
import base64
import random
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import random


def de_pic(img_path='img\\math_pic.jpg'):
    # 对图片进行解码
    with open(img_path, 'rb') as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data)  # base64编码
        return base64_data
        # print(base64_data)
        # print(type(base64_data))

# 对图片进行编码后再现


def re_pic(base64_data):
    # 对图片进行解码，但是注意图片解码后生成的数据缺少前缀，
    # 直接读取文件中的数据是无法转换为图片的
    # 缺少前缀：data:image/jpeg;base64,
    # 需要在使用时得到字符串的同时进行拼接，得到完整的数据
    # print(type(base64_data))
    jiema = base64.b64decode(base64_data)  # 解码
    with open('img\\new.jpg', 'wb') as file:
        # file.write('data:image/jpeg;base64,'+str(jiema))  # 将解码得到的数据写入到图片中
        file.write(jiema)


def show_pic(img_path='img\\new.jpg'):
    # 对解码后得到的图片打开
    img = Image.open(img_path)
    plt.figure("pic")
    plt.imshow(img)
    plt.show()
