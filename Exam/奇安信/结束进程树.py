pid = input().split()
ppid = input().split()

num = input()
q = [num]
cnt = 0
while q:
    k = q.pop(0)
    cnt += 1
    while k in ppid:
        index = ppid.index(k)
        q.append(pid.pop(index))
        ppid.pop(index)

print(cnt)
