"""题目：编写input()和output()函数输入，输出5个学生的数据记录。"""
def getList(stuList):
    for i in range(5):
        stuList.append(['','',[]])

def input_stu(stuList):
    for i in range(3):
        stuList[i][0] = input("输入姓名：")
        stuList[i][1] = input("输入学号：")
        for j in range(3):
            stuList[i][2].append(eval(input("输入各科成绩（按语数外顺序）：")))

def output_stu(stuList):
    for i in range(3):
        print("\n姓名：{}\n学号：{}\n语数外成绩分别为：".format(stuList[i][0],stuList[i][1]))
        for j in range(3):
            print("{}".format(stuList[i][2][j]),end=',')

def main():
    stuList = []
    getList(stuList)
    input_stu(stuList)
    print(stuList)
    output_stu(stuList)
main()
