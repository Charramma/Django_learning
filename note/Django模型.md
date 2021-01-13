# 模型

> https://docs.djangoproject.com/zh-hans/3.1/topics/db/models/
>
> 本文档只是对模型的详细介绍，具体在项目中的使用见基础教程

模型**准确且唯一**的描述了数据

**每一个模型都映射一张数据库表**

**模型类的每个属性都相当于一个数据库的字段**



### 1. 模型的定义

```python
from django.db import models

class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
```

- 一个类通过继承django.db.models.Model成为一个模型类
- 字段通过类属性指定，如上面的模型中有两个字段
    - first_name	长度为30的字符字段
    - last_name    长度为30的字符字段

**Django会根据配置文件中指定的数据库后端生成对应的SQL语句**

> 会自动生成一个id字段作为主键，这种行为可被改写



### 2. 字段

- 字段在类属性中定义

- 字段名应避免与模型API名称冲突

- 每个字段都是Field类的实例

    

### 3. 常用Django内置字段类型：

> 详细参考：https://docs.djangoproject.com/zh-hans/3.1/ref/models/fields/#model-field-types

#### 数字

- **IntegerField** 一个整数 范围-2147483648~2147483647

- **FloatField** 一个浮点数

- **DecimalField** 高精度浮点数，有两个必要参数`max_digits`、`decimal_places`

    ```
    DecimalField(max_digits=None, decimal_places=None, **options)
    ```

    `max_digits` 数字中允许的最大位数，必须大于或等于`decimal_places`

    `decimal_places` 与数字一起查处的小数位数

    > 例如，如果要存储精度为小数点后两位的 `999` 的数字，你可以使用：
    >
    > ```
    > models.DecimalField(..., max_digits=5, decimal_places=2)
    > ```
    >
    > 并以 10 位小数的精度来存储最多约 10 亿的数字：
    >
    > ```
    > models.DecimalField(..., max_digits=19, decimal_places=10)
    > ```

    

#### 日期和时间

- **DateField** 一个日期，在python中用`datetime.time`实例表示

    ```python
    DateField(auto_now=False, auto_now_add=False, **options)	# 默认
    ```

    `DateField(auto_now=True)` 保存时自动将该字段设置为当前时间（只在调用`Model.save()`时更新）

    `DateField(auto_now_add=False)` 第一次创建对象时，自动将该字段设置为当前时间

- **DateTimeField** 日期和时间，在python中使用`datetime.datetime`实例表示，使用和DateTime相同的额外参数

- **TimeField** 一个时间 在python中用datetime.time实例表示，接受DateField相同的自动填充选项

    ```python
    TimeField(auto_now=False, auto_now_add=False, **options)
    ```

    

#### 字符

- **CharField** 一个字符串字段，有一个必要参数`max_length`，及该字段接受的最大字符串长度

    ```python
    CharField(max_length=<int>)
    ```

    

- **TextField** 适用于大量文本的字段

#### 文件

- **FileField** 一个文件字段

- **ImageField** 图像



### 4. 字段选项

- `null=True|False` 如果设置为 `True`，当该字段为空时，Django 会将数据库中该字段设置为 `NULL`。默认为 `False` 。
- `blank=True|False` 如果设置为 `True`，该字段允许为空。默认为 `False`。