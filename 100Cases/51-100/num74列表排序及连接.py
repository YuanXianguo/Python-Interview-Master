llist = []
for i in range(3):
    llist.append(input("输入："))
llist.sort()
lllist = llist[::-1]
llist += lllist
print(llist)
