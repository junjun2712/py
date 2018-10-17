# 语句

## 条件判断 if elif else

```python
#!/usr/bin/env python3

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:
age = int(input('Input your age: '))

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
```


## 循环

### for x in ... 循环

把每个元素代入变量x，然后执行缩进块的语句。

```python
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
```

#### 打印数字0到10

```python
for num in range(11): # range(11) = range(0,11)
    print(num)
```


### while 循环

只要条件满足，就不断循环，条件不满足时退出循环。


### break 语句

可以提前退出循环


### continue 语句

跳过当前的这次循环，直接开始下一次循环。
