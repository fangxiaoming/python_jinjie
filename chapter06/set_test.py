#set 集合 fronzenset (不可变集合) 无序， 不重复
# s = set('abcdee')
# s = set(['a','b','c','d','e'])
s = {'a','b', 'c'}
# s = frozenset("abcde") #frozenset 可以作为dict的key
# print(s)

#向set添加数据
another_set = set("cef")
s.update(another_set) #合并两个set
print(s)
re_set = s.difference(another_set)  #获取两个集合的差集
re_set = s - another_set
re_set = s & another_set  #交集
re_set = s | another_set  #并集

#set性能很高
# | & -  #集合运算
print(re_set)

print (s.issubset(re_set))
# if "c" in re_set:
#     print ("i am in set")
