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

#### 日期

- **DateField** 一个日期，在python中用`datetime.time`实例表示

    ```python
    DateField(auto_now=False, auto_now_add=False, **options)	# 默认
    ```

    `DateField(auto_now=True)` 保存时自动将该字段设置为当前时间（只在调用`Model.save()`时更新）

    `DateField(auto_now_add=False)` 第一次创建对象时，自动将该字段设置为当前时间

- **DateTimeField** 日期和时间，在python中使用`datetime.datetime`实例表示，使用和DateTime相同的额外参数