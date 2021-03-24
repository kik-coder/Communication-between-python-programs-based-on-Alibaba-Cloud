import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# 默认发送该文件

# 发送邮件主要使用的是smtplib库，这里发送的信息是由阿里云回传信息
# 写入文件的数据，目的接收者的邮箱地址由字符拼接组成，这样在gui界面
# 获取接收端地址时仅需要写qq号，更加方便一点。注意从邮箱发送数据要先
# 获取密钥，而不是qq密码，具体位置在qq邮箱账号设置中，我们使用stmp，
# 所以端口号选择587.下面带附件的邮箱发送，原理和直接发送数据相似，只
# 是发送的不是从文件读取到的内容，更像是将需要的文件完全发送过去。


def send_email(toaddr):  # 发送邮件的方法
    fromaddr = "1018963684@qq.com"  # 发送端的qq邮箱号码
    # toaddr = "***"#邮件接收端的qq邮箱号码
    toaddr = str(toaddr)+"@qq.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "阿里云的回传数据"
    with open('doc\\math_data.txt', 'r')as f:
        message = f.read()
    body = message
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP("smtp.qq.com", 587)
    server.starttls()
    server.login(fromaddr, "kznctcbafswxbbih")  # 邮件发出端的密钥
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def pic_emile(toaddr='1018963684', filename="img\\math_pic.jpg"):
    fromaddr = "1018963684@qq.com"
    # 邮件发送者的地址
    toaddr = str(toaddr)+"@qq.com"
    # 邮件接受者的地址
    msg = MIMEMultipart()
    # 实例化一个MIMEMultipart
    msg['From'] = fromaddr
    # 设置来源地址
    msg['To'] = toaddr
    # 设置目的地地址
    msg['Subject'] = "aliyun回传后图片"
    # 设置邮件的主题
    body = "邮件传输"
    # 设置邮件的正文

    msg.attach(MIMEText(body, 'plain'))
    # filename = "timg.jpg"
    # 需要传递的附件的名称（相对地址）
    attachment = open(filename, 'rb')
    # 打开该文件
    part = MIMEBase('application', 'octet-stream')
    # 进行格式转换
    part.set_payload((attachment).read())
    # 设置数据
    encoders.encode_base64(part)
    # 解码
    part.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(part)
    # 添加附件

    server = smtplib.SMTP("smtp.qq.com", 587)
    # 设置SMTP
    server.starttls()
    # 开始
    server.login(fromaddr, "kznctcbafswxbbih")
    # 第二个参数还是那个邮件发送端的授权码
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    # 发送邮件
    server.quit()
    # 结束


# send_email('1018963684')
