while True:
    txt = 'E:\\Python\\Python100例\\51-100'
    with open(txt +'\\97.txt','a',encoding='utf-8') as f:
        innum = input("输入字符（#结束）：")
        if innum != '#':
            f.write(innum)
        else:
            f.close()
            break
