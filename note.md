---
typora-copy-images-to: imgs
---

#### 2.1 python中一切皆对象

​	python中类和函数也都是对象

![1535802745613](F:\python_jinjie\imgs\1535802745613.png)



#### 2.2 `type`  `object` 和 `class` 的关系

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

### 第四章 深入类和对象

#### 4.1 鸭子类型和多态

当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子,那么这只鸟就可以被称为鸭子

extend方法只需传入可迭代类型 iterable

如果一个对象实现了`__getitem__`方法，那python的解释器就会把它当做一个`collection`，就可以在这个对象上使用切片，获取子项等方法；

如果一个对象实现了`__iter__`和`next`方法，python就会认为它是一个`iterator`，就可以在这个对象上通过循环来获取各个子项。 

#### 4.2 抽象基类(abc模块)

python中的抽象基类不能实例化,动态语言是没有变量类型的,变量只是一个符号,可以赋值任意类型

python中少了编译时查错的功能

类似于Java中的接口,我们需要强制某个子类必须实现某些方法,需要设计一个抽象基类， 指定子类必须实现某些方法

#### 4.3 使用isinstance而不是type

isinstance会循着继承链去寻找

#### 4.4 类变量和对象变量(实例变量)

![1535875262123](F:\python_jinjie\imgs\1535875262123.png)

#### 4.5 类属性和实例属性以及查找顺序

由下而上的查找顺序

深度优先算法

![1535875921294](F:\python_jinjie\imgs\1535875921294.png)

广度优先算法

![1535876056832](F:\python_jinjie\imgs\1535876056832.png)

python 3中采用 C 3 算法

#### 4.6 类方法 静态方法 实例方法的区别

![1535876819819](F:\python_jinjie\imgs\1535876819819.png)

![1535877003172](F:\python_jinjie\imgs\1535877003172.png)

#### 4.8 数据封装和私有属性

![1535877568645](F:\python_jinjie\imgs\1535877568645.png)

#### 4.9 python的自省机制

自省是通过一定的机制查询到对象的内部结构

#### 4.10 super函数

super(). `__init__` 不是调用父类构造函数的意思,而是调用`mro`中的下一个函数

super的调用顺序和 `mro` 中的顺序保持一致

#### 4.11 mixin继承案例

混合模式

特点:

Mixin类功能单一

不和基类关联,可以和任意基类组合

在Mixin中不要使用super这种用法

#### 4.12 python中的with语句(上下文管理器)

try except finally

with语法可以优化上述语句

![1535891018615](F:\python_jinjie\imgs\1535891018615.png)

`contextlib` 简化上下文管理器