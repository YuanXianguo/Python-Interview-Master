n = "true or false and true"


def get_bool(s):
    ss = s.split("or")
    flag = 0
    for i in ss:
        if not i:
            return "error"

        cnt_f = 0
        for j in i.strip().split("and"):
            if j.strip() == "true":
                pass
            elif j.strip() == "false":
                cnt_f += 1
            else:
                return "error"

        if cnt_f % 2 == 0:
            flag = 1

    return "true" if flag else "false"


if __name__ == '__main__':
    while True:
        try:
            print(get_bool(input()))
        except:
            break

