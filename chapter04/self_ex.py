#自省是通过一定的机制查询到对象的内部结构
from chapter04.class_method import Date
class Person:
    """
    人
    """
    name = "user"

class Student(Person):
    def __init__(self, scool_name):
        self.scool_name = scool_name

if __name__ == "__main__":
    user = Student("慕课网")

    #通过__dict__查询属性

    user.__dict__["school_addr"] = "北京市"
    print(user.__dict__)
    print(user.school_addr)
    print(Person.__dict__)
    print(user.name)
    # a = [1,2]
    print(dir(Person))

