import pic
import base64


def pic_read():
    with open('doc\\data.txt', 'r') as f:
        a = f.read()
    b = a.rstrip('\'')
    c = b.replace('b\'', '')
    # 去文本中的b'
    with open('doc\\data.txt', 'w', encoding='utf-8') as f1:
        f1.write(c)
    with open('doc\\data.txt', 'r') as f:
        a = f.read()

    b = a.encode()
    pic.re_pic(b)
    pic.show_pic()
