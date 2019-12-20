n1,n2,n3 = eval(input("输入3个数，以逗号隔开："))
def exch(p1,p2):
    return p2,p1
if n1 > n2:
    n1,n2 = exch(n1,n2)
if n1 > n3:
    n1,n3 = exch(n1,n3)
if n2 > n3:
    n2,n3 = exch(n2,n3)
print("{}<{}<{}".format(n1,n2,n3))
