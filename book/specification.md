# 开发规范

PEP 8 -- Style Guide for Python Code 

https://legacy.python.org/dev/peps/pep-0008/

## 文件名

1. 以 .py 为后缀扩展名；
2. 文件名均由小写字母组成；
3. 文件名只能是英文字母、数字和下划线的组合。


## 变量

#### 变量命名
* 变量名必须是大小写英文、数字和_的组合；
* 且不能以数字开头。

#### 全局变量
* 一般在函数体外定义的变量为全局变量；
*  全局变量所有作用域都可读。
```
函数内部也可以定义全局变量，使用global定义。
```

#### 局部变量
* 在函数内部定义的变量称为局部变量。
* 局部变量只能在本函数可读
```python
name = 'A' #全局变量

def f1():
    name='a' #如果需要改变全局变量的值，需要使用global定义：global name;name='a'
    age = 18 #局部变量
    print(age,name)

def f2():
    age=19 #局部变量
    print(age,name)
    global a #如果不用global定义，func外部print(a)则提示：NameError: name 'a' is not defined
    a=20

f1()
f2()
print(a)

if a > 10:
    b=1
print(b)

#打印结果：
(18, 'a')
(19, 'A')
20
1
```
函数在读取变量时，优先读取函数本身自有的局部变量，再去读全局变量。


## 常量

Python
* 通常用全部大写的变量名表示常量。
```python
PI = 3.14159265359
```
