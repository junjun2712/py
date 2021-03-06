# 程序结构


1. 声明Python程序
2. 程序注释
3. 引入包
4. 定义全局变量
5. 类定义(类上方空两行)
6. 函数定义(函数上方空两行)
7. main入口
8. 以上遵循pycodestyle

示例：
```python
#!/usr/bin/env python3
# import sys
# import os

debug = True


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name, self.score))


class FooClass(object):
    pass


def test():
    foo = FooClass()
    stu = Student("dl", "80")
    stu.print_score()
    if debug:
        print("run test()")


if __name__ == "__main__":
    print("moduel name:", __name__)
    test()

```
运行：
```shell
# python demo.py 
moduel name: __main__
dl:80
run test()
```

关于__name__：
```shell
# python
Python 3.6.2 (default, Sep 18 2017, 20:31:49) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-16)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import demo
>>> print(demo.__name__)
demo
>>> exit()
```
在python中，当一个module作为整体被执行时,moduel.__name__的值将是"__main__"；

而当一个module被其它module引用时，module.__name__将是module自己的名字。
