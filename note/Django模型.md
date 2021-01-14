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

#### ① 数字

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

    

#### ② 日期和时间

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

    

#### ③字符

- **CharField** 一个字符串字段，有一个必要参数`max_length`，及该字段接受的最大字符串长度

    ```python
    CharField(max_length=<int>)
    ```

    

- **TextField** 适用于大量文本的字段



#### ④ 文件

- **FileField** 一个文件字段

- **ImageField** 图像



#### <font color='red'>⑤ 外键</font>

**ForeignKey** 多对一关系

需要两个位置参数

- 模型相关的类

- on_delete 选项

    当一个由 ForeignKey 引用的对象被删除时，Django 将模拟 on_delete 参数所指定的 SQL 约束的行为。

    on_delete 的可能值可以在 django.db.models 中找到

    - CASCADE
    - PROTECT
    - RESTRICT
    - SET_NULL
    - ...(详见https://docs.djangoproject.com/zh-hans/3.1/ref/models/fields/#django.db.models.ForeignKey)





### 4. 字段选项

- `default` 该字段的默认值

- `null=True|False` 如果设置为 `True`，当该字段为空时，Django 会将数据库中该字段设置为 `NULL`。默认为 `False` 。

- `blank=True|False` 如果设置为 `True`，该字段允许为空。默认为 `False`。

- `primary_key=True|False` 主键

    > 在一个模型中，如果你没有对任何一个字段设置 primary_key=True 选项。 Django 会自动添加一个 id（IntegerField） 字段，并设置为主键

- `unique=True|False`  是否在整个表中保持唯一

- `choices` 一系列二元组，用作此字段的选项。如果提供了二元组，默认表单小部件是一个选择框，而不是标准文本字段，并将限制给出的选项。每个二元组的第一个值会储存在数据库中，而第二个值将只会用于在表单中显示。

    > ```python
    > YEAR_IN_SCHOOL_CHOICES = [
    >     ('FR', 'Freshman'),
    >     ('SO', 'Sophomore'),
    >     ('JR', 'Junior'),
    >     ('SR', 'Senior'),
    >     ('GR', 'Graduate'),
    > ]
    > ```

    > 每当 `choices` 的顺序变动时将会创建新的迁移。

    要获取该字段二元组中相对应的第二个值，使用 `get_FOO_display()` 方法

    > ```python
    > from django.db import models
    > 
    > class Person(models.Model):
    >     SHIRT_SIZES = (
    >         ('S', 'Small'),
    >         ('M', 'Medium'),
    >         ('L', 'Large'),
    >     )
    >     name = models.CharField(max_length=60)
    >     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    > ```
    >
    > ```
    > >>> p = Person(name="Fred Flintstone", shirt_size="L")
    > >>> p.save()
    > >>> p.shirt_size
    > 'L'
    > >>> p.get_shirt_size_display()
    > 'Large'
    > ```

    

### 5. 模型关联关系

模型之间三种关系：

- 多对一

    ```python
    from django.db import models
    
    # 制造商
    class Manufacturer(models.Model):
        # ...
        pass
    
    # 汽车
    class Car(models.Model):
        manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
        # ...
    ```

    一个制造商可以制造很多汽车，一辆汽车只会是一个制造商制造

    `manufacturer`字段归Car模型所有，与Manufacturer模型关联

- 多对多

    定义多对多关系使用`django.db.models.ManyToManyField`类

    ```python
    from django.db import models
    
    # 配料
    class Topping(models.Model):
    	# ...
    	pass
    	
    # 披萨
    class Pizza(models.Model):
    	toppings = models.ManyToManyField(Topping)
    ```

    一种披萨可以有多种配料，一种配料也可以用在多种披萨上

    **对于多对多光联关系的两个模型，可以在任何一个模型中添加 `ManyToManyField` 字段，但只能选择一个模型设置该字段，即不能同时在两模型中添加该字段。**

