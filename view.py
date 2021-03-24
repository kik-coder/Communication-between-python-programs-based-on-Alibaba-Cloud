import fu_emile
import os
from tkinter import *
from os import path
import tkinter as Tkinter
import tkinter as tk
from tkinter.messagebox import *
from PIL import Image, ImageTk
import tkinter
from tkinter import ttk
import de_math
import link_ali
# 上面的选项卡
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt
import pic
import schedule
from tkinter.filedialog import askopenfilename
import win32gui
from PIL import ImageGrab
from PIL import Image
import cv2 as cv2
from PIL import Image, ImageTk

# gui界面主要函数的地方


class InputFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.ProductKey = StringVar()
        self.DeviceName = StringVar()
        self.DeviceSecret = StringVar()
        # 设置只读选项
        self.cmb = ttk.Combobox(self, state="readonly")
        self.qq = StringVar()
        self.createPage()

    def email(self):
        # 对界面中的leble的读取
        qq = self.qq.get()
        fu_emile.send_email(qq)

    def se(self):
        # print(type(self.cmb.current()))
        if (self.cmb.current() == 0):
            k = de_math.bosong()
            # de_math.bs_pic(k)
            link_ali.up(k)
            QueryFrame
        elif(self.cmb.current() == 1):
            k = de_math.erxiang()
            link_ali.up(k)
            QueryFrame
        elif(self.cmb.current() == 2):
            k = de_math.zhengtai()
            link_ali.up(k)
            QueryFrame
            pass
        elif(self.cmb.current() == 3):
            k = 121
            link_ali.up(k)
            QueryFrame
            pass
        # 这里是带参方法的使用
        # keyword = self.keyName.get()
        # pagenum = self.importUrl.get()
        # text_name = select_news(keyword, pagenum)

    def createPage(self):

        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='ProductKey:', font=(12)).grid(
            row=1, stick=W, pady=10)
        Entry(self, textvariable=self.ProductKey).grid(
            row=1, column=1, stick=E)
        self.ProductKey.set('a1n3CWdQf4J')
        # entry为文本框

        Label(self, text='DeviceName:', font=(
            12)).grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.DeviceName).grid(
            row=2, column=1, stick=E)
        self.DeviceName.set("cucu1")

        Label(self, text='DeviceSecret:', font=(
            12)).grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.ProductKey).grid(
            row=3, column=1, stick=E)
        self.DeviceSecret.set("myJ2SqUblQDWIUDdLRsJaqI7BbB1Ubcs")

        Label(self, text='选择产生数据类型:', font=(
            12)).grid(row=4, stick=W, pady=10)
        # 下拉框，并且设置只可以读
        # cmb = ttk.Combobox(self, state="readonly")
        self.cmb.grid(row=4, column=1, stick=E)
        self.cmb['value'] = ('泊松分布产生随机数', '二项分布产生随机数', '正态分布产生随机数', '待定')
        # 设置下拉框默认的显示
        self.cmb.current(0)

        Label(self, text='发送QQ号:', font=(
            12)).grid(row=5, stick=W, pady=10)
        Entry(self, textvariable=self.qq).grid(
            row=5, column=1, stick=E)
        self.qq.set("1018963684")
        # 这里command是对点击按钮对于的函数的绑定，而后面的lambda是保证按钮对
        # 应函数不会再初始化时自动生成
        Button(self, text='转发数据至邮箱', font=12, command=lambda: self.email()).grid(
            row=7, column=0, stick=E, pady=10)

        Button(self, text='转发数据', font=12, command=lambda: self.se()).grid(
            row=7, column=1, stick=E, pady=10)

        # 复选框的写法
        # cb1 = tkinter.Checkbutton(self, text='随机数').grid(
        #     row=4, column=1, stick=E)复选框
        # self.normal_ddl.grid(row=4, column=1, stick=E)

        # Button(self, text='查询', font=12, command=lambda: se_news.select_news(name, url)).grid(
        #     row=6, column=1, stick=E, pady=10)


class QueryFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.itemName = StringVar()
        self.createPage()

    def email(self):

        fu_emile.pic_emile()

    def se(self):
        a = pic.de_pic()
        link_ali.up(a)
        pass

    def new(self):
        f = Figure(figsize=(4, 3), dpi=100)
        a = f.add_subplot(111)  # 添加子图:1行1列第1个
        de_math.clean()
        try:
            c = numpy.loadtxt('doc\\math_data.txt')
            pillar = 15
            a.hist(c, bins=pillar, density=True, stacked=True, range=[
                0, pillar], color='g', alpha=0.5)
            # a.savefig("img\\mth_pic.jpg")
            f.savefig('img\\math_pic.jpg', dpi=100)
        except:
            pass
        canvas = FigureCanvasTkAgg(f, master=self)
        canvas.draw()  # 注意show方法已经过时了,这里改用draw
        canvas.get_tk_widget().pack(side=tkinter.TOP,  # 上对齐
                                    fill=tkinter.BOTH,  # 填充方式
                                    expand=tkinter.YES)  # 随窗口大小调整而调整

    def createPage(self):
        # 以下  正常可以用
        # f = Figure(figsize=(4, 3), dpi=100)
        # a = f.add_subplot(111)  # 添加子图:1行1列第1个
        # de_math.clean()
        # try:
        #     c = numpy.loadtxt('doc\\math_data.txt')
        #     pillar = 15
        #     a.hist(c, bins=pillar, density=True, stacked=True, range=[
        #         0, pillar], color='g', alpha=0.5)
        #     # a.savefig("img\\mth_pic.jpg")
        #     f.savefig('img\\math_pic.jpg', dpi=100)
        # except:
        #     pass
        # canvas = FigureCanvasTkAgg(f, master=self)
        # canvas.draw()  # 注意show方法已经过时了,这里改用draw
        # canvas.get_tk_widget().pack(side=tkinter.TOP,  # 上对齐
        #                             fill=tkinter.BOTH,  # 填充方式
        #                             expand=tkinter.YES)  # 随窗口大小调整而调整
        # 以上
        # Button(self, text='转发图片至邮箱', font=12, command=lambda: self.email()).grid(
        #     row=10, column=0, stick=E, pady=10)

        # Button(self, text='转发图片', font=12, command=lambda: self.se()).grid(
        #     row=10, column=1, stick=E, pady=10)

        Button(self, text='转发图片至邮箱', font=12,
               command=lambda: self.email()).pack(padx=30, pady=5)
        Button(self, text='转发图片', font=12,
               command=lambda: self.se()).pack(padx=80, pady=5)
        Button(self, text='更新', font=12,
               command=lambda: self.new()).pack(padx=80, pady=5,)
        pass

        # 这个使显示图片的按钮函数
        # Button(self, text='显示', font=12, command=lambda: self.show()).grid(
        #     row=6, column=1, stick=E, pady=10)


class AboutFrame(Frame):  # 继承Frame类
    # global img_png           # 定义全局变量 图像的
    # var = tk.StringVar()    # 这时文字变量储存器

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.itemName = StringVar()
        self.var = StringVar()
        self.createPage()

    def email1(self):
        fu_emile.pic_emile('1018963684', 'img\\timg.jpg')

    def se(self):
        a = pic.de_pic('img\\timg.jpg')
        link_ali.up(a)
        pass

    def Open_Img(self):
        global img_png
        self.var.set('已打开')
        Img = Image.open('img\\timg.jpg')
        img_png = ImageTk.PhotoImage(Img)

    def Show_Img(self):
        global img_png
        self.var.set('已显示')
        label_Img = tk.Label(self, image=img_png)
        label_Img.pack()

    def createPage(self):
        # 创建文本窗口，显示当前操作状态
        Label_Show = Label(self,
                           textvariable=self.var,   # 使用 textvariable 替换 text, 因为这个可以变化
                           bg='white', font=('Arial', 10), width=12, height=1)
        Label_Show.pack(pady=1)
        # 创建打开图像按钮
        btn_Open = Button(self,
                          text='打开图像',      # 显示在按钮上的文字
                          width=10, height=1,
                          command=lambda:  self.Open_Img())     # 点击按钮式执行的命令
        btn_Open.pack(pady=1)    # 按钮位置
        # 创建显示图像按钮
        btn_Show = Button(self,
                          text='显示图像',      # 显示在按钮上的文字
                          width=10, height=1,
                          command=lambda: self.Show_Img())     # 点击按钮式执行的命令
        btn_Show.pack(pady=1)    # 按钮位置
        Button(self, text='转发图片至邮箱', width=12, height=1,
               command=lambda: self.email1()).pack(pady=1)
        Button(self, text='转发图片', width=12, height=1,
               command=lambda: self.se()).pack(pady=1)
        pass
