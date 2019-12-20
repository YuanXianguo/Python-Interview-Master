import time

start = time.clock()
for i in range(200):
    print(i)
end = time.clock() - start
print(end)
