import random as r

#随机选取一个元素
print(r.choice('qwer''asdf'))

#【0，1）之间小数
print(r.random())

#产生数字10的随机序列
r.seed(10)
print(r.random())

#【a,b】之间小数
print(r.uniform(0,10))

#【a,b】之间整数
print(r.randint(0,10))

#【a,b）之间步长为k的整数
print(r.randrange(0,10,2))

#随机排列
list = [1,2,5,3]
r.shuffle(list)
print(list)


