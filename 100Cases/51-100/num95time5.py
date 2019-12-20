import time

now_time = time.localtime()
res_time = time.strftime("%Y-%m-%d %H:%M:%S".format(now_time))
print(now_time,'\n',res_time)
