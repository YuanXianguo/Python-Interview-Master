"""题目：找到年龄最大的人，并输出。请找出程序中有什么问题。"""
person = {"li":18,"wang":50,"zhang":20,"sun":22}
maxAge = 'li'
for key in person.keys():
    if person[key] > person[maxAge]:
        maxAge = key
print(maxAge,person[maxAge])
