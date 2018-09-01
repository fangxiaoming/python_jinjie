---
typora-copy-images-to: imgs
---

#### 2.1 python中一切皆对象

​	python中类和函数也都是对象

![1535802745613](F:\python_jinjie\imgs\1535802745613.png)



#### 2.2 type,object和class的关系

​	![1535803793178](F:\python_jinjie\imgs\1535803793178.png)

​	object是type的实例,       `str` `list` `dict`等都是type的实例,同时type也继承了object(有点绕),type也是type自身的一个实例,一切皆对象,一切皆继承自object.  type自己也是自己的对象实例

#### 2.3 python中的常见内置类型

​	![1535804480108](F:\python_jinjie\imgs\1535804480108.png)

​	a = None 

​	b = None 则 id(a) ==id(b)为true

python代码本身也会被python解释器变成对象类型

type也是一种类型

### 第三章 魔法函数

#### 3.1 什么是魔法函数

双下划线开头,双下划线结尾

使用python提供的魔法函数,不能自己去定义魔法函数

魔法函数会贯穿整个课程

#### 3.2 python的数据模型以及数据模型对python的影响

魔法函数是独立于类和object外的,直接会影响到某一个类python的语法

python的默认语法会在执行语句时默认的去调用魔法函数,如果修改魔法函数的话,也就影响了Python的语法

**魔法函数定义后不需要显式的去调用**

#### 3.3 魔法函数一览

非数学运算和数学运算,分散在后续章节中介绍

#### 3.4  len函数的特殊性

`len`函数会隐式的去调用`__len__`函数

使用python时尽量使用python内置的数据类型