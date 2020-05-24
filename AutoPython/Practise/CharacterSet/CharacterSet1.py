"""
1.unicode 英文中文字符都占两个字符，16字节
2.ASCII不能存中文，只能存英文或者特殊字符，8字节
3.在Unicode基础上扩展了utf-8，所有的英文字符按照ASCII存储，所有的中文字符统一三个字节
"""
import sys

print(sys.getdefaultencoding())

'''
以下仅仅使用于python2

'''

# msg = '我爱北京'
# msg_gb2312 = msg.decode('utf-8').encode('gb2312')
# gb2312_to_gbk = msg_gb2312.decode("gbk").encode("gbk")
#
# print(msg)
# print(msg_gb2312)
# print(gb2312_to_gbk)

'''
以下仅仅使用于python3

'''

msg = "我爱北京天安门"
# msg_gb2312 = msg.decode("utf-8").encode("gb2312")
msg_gb2312 = msg.encode("gb2312")  # 默认就是unicode,不用再decode,喜大普奔
gb2312_to_unicode = msg_gb2312.decode("gb2312")
gb2312_to_utf8 = msg_gb2312.decode("gb2312").encode("utf-8")

print(msg)
print(msg_gb2312)
print(gb2312_to_unicode)
print(gb2312_to_utf8)
