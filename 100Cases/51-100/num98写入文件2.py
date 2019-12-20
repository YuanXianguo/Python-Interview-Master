num = input("输入字符串：")
txt = 'E:\\Python\\Python100例\\51-100'
with open(txt+'\\98.txt','w',encoding='utf-8') as f:
    f.write(num.upper())
    f.close()
