def get_float(str_):
    str_ = str_.strip()
    cnt = 0
    res = ""
    for i in str_:
        if i == ".":
            cnt += 1
        if cnt < 2 and (i.isdigit() or i == "."):
            res += i
        else:
            break
    return eval(res)


def get_float2(str_):
    flag = 0
    res = 0
    cnt = 0
    for i in str_:
        if i == ".":
            flag = 1
            continue
        if not flag:
            res = res * 10 + int(i)
        else:
            cnt += 1
            res += int(i) / (10 ** cnt)
    return res

