> 跟着官方文档（3.1）学习Django的笔记

## 一、Django安装与导入

安装Django

```
pip install Django
```

验证安装

```
C:\Users\Administrator>python -m django --version
3.1.4
```

导入Django模块

```
>>> import django
>>> print(django.get_version())
3.1.4
>>>
```



## 二、创建Django项目

### 1. 创建初始项目目录

cd到一个像放置代码的目录，然后执行以下命令

```
# 在当前目录下创建一个mysite目录
django-admin startproject mysite
```

mysite目录结构如下

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

- **manage.py**  一个用于管理Django项目的命令行工具
- **内层mysite/**  包含项目源代码
- **mysite/settings.py**  Django项目的配置文件
- **mysite/urls.py**  Django项目的URL声明
- **mysite/asgi.py**  作为项目的运行在 ASGI 兼容的Web服务器上的入口
- **mysite/wsgi.py**  作为项目的运行在 WSGI 兼容的Web服务器上的入口

### 2. 运行项目

一个简单的项目就这样创建好了，在外层mysite目录下可以运行这个项目

```
python manage.py runserver
```

![image-20201208202955559](Django.assets/image-20201208202955559.png)

访问http://127.0.0.1:8000/，看到如下页面

![image-20201208203052808](Django.assets/image-20201208203052808.png)

**更换端口**

```
python manage.py runserver 8080
```

**指定监听的ip**

```
# 0是0.0.0.0的简写
python manage.py runserver 0:8080
```

**什么情况下runserver会自动重载python代码？**

- 用于开发的服务器在需要的情况下会对每一次的访问请求重新载入一遍 Python 代码
- 然而，一些动作，比如添加新文件，将不会触发自动重新加载，需要手动重启服务器。



## 三、创建投票应用

### 1. 创建一个应用

在manage.py所在目录下，运行以下命令创建一个应用

```
# 创建一个叫polls的应用
python manage.py startapp polls
```

在这个目录下创建了一个polls目录，目录结构如下

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

### 2. 编写视图

**创建视图**：打开polls/views.py

```python
# ***** mysite/polls/views.py *****


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

**映射URL**

在polls目录中新建一个urls.py文件



