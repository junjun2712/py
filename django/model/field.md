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