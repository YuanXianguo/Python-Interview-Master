for i in range(1,10):
    for m in range(1,i+1):
        print("{:<}×{:<}={:>2}".format(i,m,i*m),end=' ')
    print("")
