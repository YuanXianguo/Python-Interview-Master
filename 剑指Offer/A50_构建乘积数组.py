"""
题目：给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

思路：B[i]中的值可以看作下图中的矩阵中每行的乘积
下三角用连乘，上三角，从下向上也是连乘
B0 1 A1 A2 ... An-2 An-1
B1 A0 1 A2 ... An-2 An-1
B2 A0 A1 1 ... An-2 An-1
...
Bn-3 A0 A1 A2 ... An-2 An-1
Bn-2 A0 A1 A2 ... 1    An-1
Bn-1 A0 A1 A2 ... An-2 1
"""


def mul(array):
    if not array or not len(array):
        return
    b = [1] * len(array)
    for i in range(1, len(array)):
        b[i] = b[i-1] * array[i-1]
    tmp = 1
    for i in range(len(array)-2, -1, -1):
        tmp *= array[i+1]
        b[i] *= tmp
    return b


class Solution:
    def multiply(self, A):
        # write code here
        n = len(A)
        B = [1] * n
        # 下三角连乘
        for i in range(1, n):
            B[i] = B[i-1] * A[i-1]
        # 上三角连乘
        tmp = 1
        for i in range(n-2, -1, -1):
            tmp *= A[i+1]
            B[i] *= tmp
        return B


def mul2(array):
    b = [1] * len(array)
    for i in range(1, len(b)):
        b[i] = b[i-1] * array[i-1]
    tmp = 1
    for i in range(len(b)-2, -1, -1):
        tmp *= array[i+1]
        b[i] *= tmp
    return b


if __name__ == '__main__':
    print(mul(list(range(1, 10))))
