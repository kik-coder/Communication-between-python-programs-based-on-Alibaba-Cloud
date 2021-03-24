from linkkit import linkkit
import time
import json
# 连接阿里云
import im_math
import im_pic


def on_connect(session_flag, rc, userdata):
    # 连接阿里云
    print("on_connect:%d,rc:%d,userdata:" % (session_flag, rc))
    pass


def on_disconnect(rc, userdata):
    # 取消连接阿里云
    print("on_disconnect:rc:%d,userdata:" % rc)


def on_subscribe_topic(mid, granted_qos, userdata):
    # 订阅topic
    print("on_subscribe_topic mid:%d, granted_qos:%s" %
          (mid, str(','.join('%s' % it for it in granted_qos))))
    pass


def on_topic_message(topic, payload, qos, userdata):
    # 接收云端的数据

    #print("on_topic_message:" + topic + " payload:" + str(payload) + " qos:" + str(qos))
    # 不知道为什么下行的数据是“123”，设备端的接收到的数据却是b:"123"
    # 所以我在这里用了一个切片去处理数据
    m = str(payload)[2:-1]
    print("阿里云上传回的数据是:", str(payload)[2:-1])
    # 把得到的数据存入文件，方便后续对文件的分析
    with open('doc\\data.txt', 'w', encoding='utf-8') as f1:
        f1.write(m)
    p()
    pass

# 用于对接收的数据进行判断然后绘图


def p():
    with open('doc\\data.txt', 'r')as f:
        a = f.read()
    if len(a) > 100:
        im_pic.pic_read()
    else:
        im_math.math_read()


def on_unsubscribe_topic(mid, userdata):
    # 终止订阅云端数据
    print("on_unsubscribe_topic mid:%d" % mid)
    pass


def on_publish_topic(mid, userdata):
    # 发布消息的结果，判断是否成功调用发布函数
    print("on_publish_topic mid:%d" % mid)


# 一个新的设备
# 设置连接参数，方法为“一机一密”型
lk1 = linkkit.LinkKit(
    host_name="cn-shanghai",
    # 填自己的host_name
    product_key="a1n3CWdQf4J",
    # 填自己的product_key
    device_name="jieshou1",
    # 填自己的device_name
    device_secret="12280ad3e6fd7cbe41d8c0eb86e5d046")
# 填自己的device_secret
# 注册接收到云端数据的方法
lk1.on_connect = on_connect
# 注册取消接收到云端数据的方法
lk1.on_disconnect = on_disconnect
# 注册云端订阅的方法
lk1.on_subscribe_topic = on_subscribe_topic
# 注册当接受到云端发送的数据的时候的方法
lk1.on_topic_message = on_topic_message
# 注册向云端发布数据的时候顺便所调用的方法
lk1.on_publish_topic = on_publish_topic
# 注册取消云端订阅的方法
lk1.on_unsubscribe_topic = on_unsubscribe_topic

# 连接阿里云的函数（异步调用）
lk1.connect_async()
# 因为他是他是异步调用需要时间所以如果没有这个延时函数的话，他就会出现not in connected state的错误
# 使用循环以防止阿里云设备下线
while(1):
    time.sleep(2)
    rc = lk1.subscribe_topic(lk1.to_full_topic("user/get"))
    i = 0
    time.sleep(6)
