from scipy.stats import binom, poisson, norm
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as npe
import numpy as np
import numpy
import random
# %matplotlib inline
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

# 二项分布


def erxiang():
    n = 10
    p = 0.5
    sample = np.random.binomial(n, p, size=24)
    print(sample)
    with open('doc\\math_data.txt', 'w') as f:
        f.write(str(sample))
    return sample


def erxiang_pic():
    pass
    # 正态分布


def zhengtai():
    mu = 0
    sigma = 1
    sample = np.random.normal(mu, sigma, size=24)
    print(sample)
    with open('doc\\math_data.txt', 'w') as f:
        f.write(str(sample))

    return sample
# 泊松分布


def bosong():
    x = np.random.poisson(lam=5, size=24)
    print(x)
    # print(type(x))
    # pillar = 15
    # a = plt.hist(x, bins=pillar, density=True, stacked=True, range=[
    #              0, pillar], color='g', alpha=0.5)
    # plt.grid()
    # plt.show()
    # print(a)
    with open('doc\\math_data.txt', 'w') as f:
        f.write(str(x))
    return x
    # print(a[0].sum())


def bs_pic(x):
    pillar = 15
    # 调整画布大小
    plt.figure(figsize=(6, 4))
    # 这里的hist函数产生的是直方图，后面是对绘图时如画笔颜色等的定义
    a = plt.hist(x, bins=pillar, density=True, stacked=True, range=[
                 0, pillar], color='g', alpha=0.5)
    plt.grid()
    # 保存plt绘图
    plt.savefig("img\\math_pic.jpg")
    plt.show()


# x = bosong()
# 对numpy类型存入文本文件对数据的数据清理，方便后续已知数据的画图，
# 随机数产生的数据存入文件会包含[],在读取的时候我们需要用replce函
# 数将它们去掉，然后再次将清洗后的数据写入文件，plt绘图时使用这个
# 文件的数据
def clean(doc_path='doc\\math_data.txt'):
    with open(doc_path, 'r') as f1:
        x = f1.read()
    a = x.replace('[', '')
    b = a.replace(']', '')
    # print(b)
    with open(doc_path, 'w')as f2:
        f2.write(b)
    # 对文本文件中数据格式的转换，可以读取数据后绘图
    # c = numpy.loadtxt('doc\\data.txt')


# # 对文本文件中数据格式的转换，可以读取数据后绘图
# c = numpy.loadtxt('doc\\data.txt')

# 正常的读取数据方式
# x = bosong()
# print(type(x))
# bs_pic(x)
# clean()
# c = numpy.loadtxt('doc\\math_data.txt')
# print(c)
# bs_pic(c)
