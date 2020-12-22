# -*- coding: utf-8 -*-
'''
@author: kebo
@contact: kebo0912@outlook.com

@version: 1.0
@file: singleton.py
@time: 2020/12/22 23:52:08

这一行开始写关于本文件的说明与解释

这个例子用MetaClass实现，其实Python里还有其他实现方式。
但是Python里的MetaClass就是用来实例化Class的，用来实现单例类正好。
refer: https://www.cnblogs.com/blackmatrix/p/6906023.html
'''
class SingletonMeta(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.instance
    
class CurrentUser(object, metaclass=SingletonMeta):
    def __init__(self, name=None):
        super(CurrentUser, self).__init__()
        self.name = name
    
    def __str__(self):
        return f"{repr(self)}:{repr(self.name)}"

if __name__ == "__main__":
    u = CurrentUser("ke")
    print(u)
    u2 = CurrentUser()
    u2.name = "bo"
    print(u2)
    print(u)
    assert u is u2
