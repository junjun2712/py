# 模型字段


## 字段选项 

下列参数可用于所有字段类型。都是可选的。

### null
如果为```True```, Django将在数据库中将空值存储为```NULL```。默认为```False```。

### blank
如果为```True```，则允许字段为空。默认是```False```。与```null```不同，```blank```是验证相关的，表单验证将允许输入空值。
如果```blank=False```，字段值是必要的。

### choices

### db_index
如果为```True```，将为该字段创建数据库索引。

### default
字段的默认值。这可以是一个值或可调用对象。如果可调用，它将在每次创建新对象时被调用。默认值不能是可变对象(模型实例、列表、集合等)。
如果您想为JSONField指定一个默认的dict，使用一个函数:
```python
def contact_default():
    return {"email": "to1@example.com"}

contact_info = JSONField("ContactInfo", default=contact_default)
```

### help_text
表单小部件将显示额外的“帮助”文本(表单中input项后面的提示信息，非验证提示)。即使您的字段没有在表单上使用，它对文档也很有用。
```python
help_text="账号长度必须大于6位，且包括大小写字母数字"
```

### verbose_name
