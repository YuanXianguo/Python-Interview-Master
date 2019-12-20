import datetime


def day_of_year():
    year = input("请输入年份：")
    month = input("请输入月份：")
    day = input("请输入日期：")
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    print(date1, date2)
    return (date1 - date2).days + 1


def getDate(date):
    y = date.index('年')
    m = date.index('月')
    d = date.index('日')
    year = int(date[:4])
    month = int(date[y+1:m])
    day = int(date[m+1:d])
    return year,month,day

#判断年
def Year(year):
    if year % 100 != 0:
        if year % 4 == 0 :
            return True
    else:
        if year % 400 == 0:
            return True

#判断月
def Month(res,month):
    monthcount = 0
    n = {}
    for m in [1, 3, 5, 7, 8, 10, 12]:
        n[m] = 31
    for m in [4, 6, 9, 11]:
        n[m] = 30
    if res:
        n[2] = 29
    else:
        n[2] = 28
    for i in range(1,13):
        if i == month:
            return monthcount
        else:
            monthcount += n[i]

#判断日
def Day(monthcount,day):
    daycount = 0
    for i in range(1,32):
        daycount += 1
        if i == day:
            return daycount + monthcount

def main():
    date = input("输入日期（2018年8月9日），我将告诉你是当年第几天：")
    year, month, day = getDate(date)
    res = Year(year)
    monthcount = Month(res,month)
    result = Day(monthcount,day)
    print("{}是当年的第{}天".format(date,result))


if __name__ == '__main__':
    # main()
    print(day_of_year())




