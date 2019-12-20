array1 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
array2 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
arraysum = [[0,0,0],
            [0,0,0],
            [0,0,0]]
for i in range(3):
    for j in range(3):
        arraysum[i][j] = array1[i][j] + array2[i][j]
print(arraysum)
for line in arraysum:
    print(line)
