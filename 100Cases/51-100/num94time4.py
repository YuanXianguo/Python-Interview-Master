import time

scale = 100
print("{0:*^{1}}".format('Textbar',scale))
start = time.perf_counter()
for i in range(scale+1):
    a = '*'*i+'->'
    b = i / scale * 100
    dur = time.perf_counter() - start
    print("\r{2:.0f}%[{0:.<{1}}]{3:.3f}".format(a,scale,b,dur),end='')
    time.sleep(0.3)
