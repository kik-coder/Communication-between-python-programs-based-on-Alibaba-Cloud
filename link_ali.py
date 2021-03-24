from linkkit import linkkit
import time
import json
# 连接阿里云


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
    pass


def on_unsubscribe_topic(mid, userdata):
    # 终止订阅云端数据
    print("on_unsubscribe_topic mid:%d" % mid)
    pass


def on_publish_topic(mid, userdata):
    # 发布消息的结果，判断是否成功调用发布函数
    print("on_publish_topic mid:%d" % mid)


# 设置连接参数，方法为“一机一密”型
lk = linkkit.LinkKit(
    host_name="cn-shanghai",
    # 填自己的host_name
    product_key="a1n3CWdQf4J",
    # 填自己的product_key
    device_name="cucu1",
    # 填自己的device_name
    device_secret="myJ2SqUblQDWIUDdLRsJaqI7BbB1Ubcs")
# 填自己的device_secret
# 注册接收到云端数据的方法
lk.on_connect = on_connect
# 注册取消接收到云端数据的方法
lk.on_disconnect = on_disconnect
# 注册云端订阅的方法
lk.on_subscribe_topic = on_subscribe_topic
# 注册当接受到云端发送的数据的时候的方法
lk.on_topic_message = on_topic_message
# 注册向云端发布数据的时候顺便所调用的方法
lk.on_publish_topic = on_publish_topic
# 注册取消云端订阅的方法
lk.on_unsubscribe_topic = on_unsubscribe_topic

# 连接阿里云的函数（异步调用）
lk.connect_async()
# 因为他是他是异步调用需要时间所以如果没有这个延时函数的话，他就会出现not in connected state的错误
# 使用循环以防止阿里云设备下线
#


def up(a):
    # 由lk发送向云的数据，由lk1接收来自云的数据
    time.sleep(2)
    # 订阅这个topic，不需要写prodect_key和device_name
    # rc, mid = lk.subscribe_topic(lk.to_full_topic("user/get"))
    # 下原 rc = lk.subscribe_topic(lk.to_full_topic("user/get"))
    # 下面这句之前的流转接收
    # rc = lk1.subscribe_topic(lk1.to_full_topic("user/get"))
    # print(rc)
    # a = input("你想要传的数据：")
    # 调用数据上传的函数，将string类的a上传到阿里云上去
    # rc, mid = lk.publish_topic(lk.to_full_topic("user/update"), str(a))

    #
    # 由于这次实践要求使用俩个pc来进行数据的传递，以下程序为上传数据
    # 的函数（update），另外传输的数据需要的格式为字符型，需要强转
    # 一次，这个也是导致我们在接收数据端要二次清理数据后才可以继续
    # 正常使用
    mid = lk.publish_topic(lk.to_full_topic(
        "user/update"), str(a))
    # 该程序设置发送数据后程序结束，阿里云设备下线，但是如果这样的话，数
    # 据可能还来不及转发，设备就下线了，从而导致接收端无法接收到数据，所
    # 以我设置了一个延时5秒的函数，保证数据有足够的时间传递数据、转发数
    # 据，同样这样也保证了客户端可以多次向接收端发送数据而不产生多次登录
    # 阿里云设备而产生的错误

    time.sleep(5)

    return
