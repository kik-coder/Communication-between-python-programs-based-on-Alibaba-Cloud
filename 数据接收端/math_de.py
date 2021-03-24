from scipy.stats import binom, poisson, norm
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as npe
import numpy as np
import random
# %matplotlib inline
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


def clean(doc_path='doc\\data.txt'):
    with open(doc_path, 'r') as f1:
        x = f1.read()
    a = x.replace('[', '')
    b = a.replace(']', '')
    # print(b)
    with open(doc_path, 'w')as f2:
        f2.write(b)


def bosong():
    x = np.random.poisson(lam=5, size=10)
    print(x)
    pillar = 15
    a = plt.hist(x, bins=pillar, density=True, stacked=True, range=[
                 0, pillar], color='g', alpha=0.5)
    plt.grid()
    plt.show()
    # print(a)
    return x
    # print(a[0].sum())


def bs_pic(x):
    pillar = 15
    a = plt.hist(x, bins=pillar, density=True, stacked=True, range=[
                 0, pillar], color='g', alpha=0.5)
    plt.grid()
    plt.show()
