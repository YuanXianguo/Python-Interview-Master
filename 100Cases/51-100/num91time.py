import time

now_time = time.localtime()
res_time = time.strftime("%Y-%m-%d %H:%M:%S", now_time)
print(res_time)
