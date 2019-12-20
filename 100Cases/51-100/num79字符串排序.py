str1 = input("输入字符串：")
str2 = input("输入字符串：")
str3 = input("输入字符串：")

print(str1,str2,str3)
if str1 > str2:
    str1,str2 = str2,str1
if str1 > str3:
    str1,str3 = str3,str1
if str2 > str3:
    str2,str3 = str3,str2
print(str1,str2,str3)
