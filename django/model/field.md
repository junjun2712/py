# 模型字段


## 字段选项 

下列参数可用于所有字段类型。都是可选的。

### null
如果设置为 True ， 当该字段为空时，Django会将数据库中该字段设置为 NULL 。默认为 False 。

### blank
如果设置为 True ，该字段允许为空。默认为 False 。

注意该选项与 False 不同， null 选项仅仅是数据库层面的设置，然而 blank 是涉及表单验证方面。如果一个字段设置为 blank=True ，在进行表单验证时，接收的数据该字段值允许为空，而设置为 blank=False 时，不允许为空。

### choices
该参数接收一个可迭代的列表或元组（基本单位为二元组）。如果指定了该参数，在实例化该模型时，该字段只能取选项列表中的值。
一个选项列表：
```python
YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
)
* 每个二元组的第一个值会储存在数据库中，而第二个值将只会用于显示作用。
* 对于一个模型实例，要获取该字段二元组中相对应的第二个值，使用 get_FOO_display() 方法。例如：
```
```python
from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
```
```python
>>> p = Person(name="Fred Flintstone", shirt_size="L")
>>> p.save()
>>> p.shirt_size
'L'
>>> p.get_shirt_size_display()
'Large'
```

### db_index
如果为```True```，将为该字段创建数据库索引。

### default
字段的默认值。可以是一个值或者是个可调用的对象，如果是个可调用对象，每次实例化模型时都会调用该对象。默认值不能是可变对象(模型实例、列表、集合等)。
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

### primary_key
如果设置为 True ，将该字段设置为该模型的主键。

在一个模型中，如果你没有对任何一个字段设置 primary_key=True 选项。 Django 会自动添加一个 IntegerField 字段，用于设置为主键，因此除非你想重写 Django 默认的主键设置行为，你可以不手动设置主键。

### unique
如果为 True ，这个字段值在整个表中必须是唯一的。

### verbose_name
字段的备注名（表单input项前的文本标签如：“名称：”）。
* 除了 ForeignKey ， ManyToManyField 和 OneToOneField ，任何字段类型（第一个参数）都接收一个可选的参数 verbose_name（不用加verbose_name＝） ，如果未指定该参数值， Django 会自动使用该字段的属性名作为该参数值，并且把下划线转换为空格。
* ForeignKey, ManyToManyField and OneToOneField 接收的第一个参数为模型的类名，后面可以添加一个 verbose_name 参数
https://docs.djangoproject.com/zh-hans/2.1/topics/db/models/#verbose-field-names


## 字段类型

### CharField

### DateTimeField

### DecimalField

### IntegerField

### ForeignKey

### ManyToManyField

### OneToOneField


