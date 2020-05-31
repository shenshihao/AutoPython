'''
装饰器不改变原有的函数调用方法增加额外的功能
高阶函数+嵌套函数--》装饰器
高潮：模拟为100个页面中的二十个页面加功能，只有登录后可以操作

'''

import time

user, passwd = 'alex', 'abc'


def auth(auth_type):
    print('auth_func', auth_type)

    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print('auth_func', *args, **kwargs)
            if (auth_type == 'local'):
                username = input('Username:').strip()
                password = input('passwd:').strip()
                if user == username and passwd == password:
                    print('user has passwd authentication')
                    # 解决被装饰函数中有返回值的问题
                    res = func(*args, **kwargs)
                    print(res)
                    print('after authentication ')
                    return res
                else:
                    print('Invalid username or passwd')
            elif auth_type == 'ldap':
                print('ldap')

        return wrapper

    return outer_wrapper


@auth
def index():
    print('index')


@auth(auth_type="local")
def home():
    return 'from home'


@auth(auth_type="ldap")
def bbs():
    print('bbs')


bbs()
