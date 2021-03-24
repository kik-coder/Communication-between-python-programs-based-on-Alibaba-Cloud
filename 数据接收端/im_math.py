import math_de
import numpy


def math_read():
    math_de.clean()
    # with open('doc\\data.txt','w')as f:
    #     a = f.read()
    c = numpy.loadtxt('doc\\data.txt')
    # print(c)
    math_de.bs_pic(c)
