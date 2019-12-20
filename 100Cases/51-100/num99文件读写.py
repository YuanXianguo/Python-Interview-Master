txt = 'E:\\Python\\Python100例\\51-100'
tlist = []
with open(txt+'\\97.txt') as f1:
    for i in f1.read():
        tlist.append(i)
with open(txt+'\\98.txt') as f2:
    for j in f2.read():
        tlist.append(j)
tlist.sort()
with open(txt+'\\99.txt','w',encoding='utf-8') as f:
    f.write(''.join(tlist))
    """f.writelines(tlist)
    f.write(str(tlist))"""
    f.close()
