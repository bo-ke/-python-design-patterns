# -*- coding: utf-8 -*-
'''
@author: kebo
@contact: kebo0912@outlook.com

@version: 1.0
@file: factory.py
@time: 2020/12/27 12:32:50

这一行开始写关于本文件的说明与解释

工厂模式，用于生产一大堆对象。这里用__subclass__来获取子类；
这样可以动态扩展子类，而不用改变factory的源码
'''


class Shape(object):
    @classmethod
    def factory(cls, name, *args, **kwargs):
        type = {c.__name__: c for c in cls.__subclass__()}  # 忽略性能:P
        shape_class = type[name]
        return shape_class(*args, **kwargs)


class Circle(Shape):
    pass


class Square(Shape):
    pass


if __name__ == "__main__":
    shapes = ["Circle", "Square"]
    for i in shapes:
        s = Shape.factory(i)
        print(s)
