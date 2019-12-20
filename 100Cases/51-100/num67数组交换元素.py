def getlist(list):
    for i in range(5):
        list.append(eval(input("输入数字：")))

def mmax(list):
    max = list[0]
    for i in list:
        if max < i:
            max = i
    l1 = list.index(max)
    list[0],list[l1] = list[l1],list[0]

def mmin(list):
    min = list[-1]
    for i in list:
        if min > i:
            min = i
    l2 = list.index(min)
    list[-1],list[l2] = list[l2],list[-1]

def main():
    list = []
    getlist(list)
    mmax(list)
    mmin(list)
    print(list)

main()
