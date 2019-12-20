days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
m = input("输入首字母：").upper()
for i in days:
    if m == i[0]:
        if m not in 'TS':
            print(i)
        else:
            n = input("输入第二个字母")
            if n == i[1]:
                print(i)
                break
            else:
                continue

