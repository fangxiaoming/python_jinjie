class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    #使得company类成为一个可迭代对象
    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    def __str__(self):
        return ",".join(self.employee)


#员工姓名列表
company = Company(["tom", "bob", "jane"])

print(company)

class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_instance):
        re_vector = MyVector(self.x+other_instance.x, self.y+other_instance.y)
        return re_vector

    def __str__(self):
        return "x:{x}, y:{y}".format(x = self.x, y = self.y)

first_vec = MyVector(1,2)
second_vec = MyVector(2,2)
print(first_vec+second_vec)
# company1= company[:2]
#
# print(len(company))
#
# for em in company:
#     print(em)