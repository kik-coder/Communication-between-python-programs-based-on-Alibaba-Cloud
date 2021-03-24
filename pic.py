# 对图像的处理
import base64
import random
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import random
img_path = 'timg.jpg'

# 对具体存图片编码的文件进行修改，增加前缀信息，修改后编码可以直接在
# base64转换图片网站中使用，但这对于直接读取没什么作用。。。记录一下
# def img_clean(text_path='doc\\data.txt'):
#     with open(text_path, 'r') as f:
#         k = f.read()
#     # a = k.replace('b'','')
#     a = 'data:image/jpeg;base64,'+k
#     # 更改后的格式是完整的图片的base64码，但是直接读取不需要这些。。。
#     with open(text_path, 'w') as f1:
#         f1.write(a)


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
    with open('new.jpg', 'wb') as file:
        # file.write('data:image/jpeg;base64,'+str(jiema))  # 将解码得到的数据写入到图片中
        file.write(jiema)


def show_pic(img_path='new.jpg'):
    # 对解码后得到的图片打开
    img = Image.open(img_path)
    plt.figure("pic")
    plt.imshow(img)
    plt.show()

# 该函数是对图片处理的函数，产生随机噪声
# def re_zaopic(img_path):
#     img = cv2.imread(img_path, 1)
#     imgInfo = img.shape
#     height = imgInfo[0] - 1  # 防止越界
#     width = imgInfo[1] - 1
#     temp = 500  # 噪声点的个数
#     for i in range(0, temp):
#         if random.randint(1, temp) % 2 == 0:
#             img[random.randint(0, height), random.randint(
#                 0, width)] = (255, 255, 255)
#         if random.randint(1, temp) % 2 != 0:
#             img[random.randint(0, height), random.randint(
#                 0, width)] = (0, 0, 0)
#     # 运行后直接显示图片
#     # cv2.imshow('dst', img)
#     # 生成随机噪点处理后的图片
#     cv2.imwrite('noise.jpg', img)
#     cv2.waitKey(0)


# 正确生成方式，命令行产生方式
# x = de_pic('timg.jpg')
# with open('doc\\data.txt', 'wb') as f:
#     f.write(x)
# with open('doc\\data.txt', 'rb') as f1:
#     m = f1.read()
# re_pic(m)
# print(str(m))
# a = str(m)

# # 按以下方法可以将文件正常转换
# #
# with open('doc\\data.txt', 'r') as f:
#     a = f.read()
# b = a.encode()
# m = base64.b64encode(b)
# re_pic(b)
# #
