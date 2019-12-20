lis = [1,2,'a','b']
list1 = []
list2 = []
for i in lis:
    if lis.index(i) % 2 == 0:
        list1.append(i)
    else:
        list2.append(i)
l_dict = dict([list1,list2])
print(l_dict)
