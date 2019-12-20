import time
for i in range(5):
    t = time.localtime()
    print(time.strftime('''%Y-%m-%d %Hh%M'%S"''').format(t))
    time.sleep(1)
