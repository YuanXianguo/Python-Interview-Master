def mypow(x, n):
    mult = 1
    while n:
        mult *= x
        n -= 1
    return mult


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.main(x, -n)
        return self.main(x, n)

    def main(self, x, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.main(x * x, n // 2)
        return self.main(x * x, (n - 1) // 2) * x


if __name__ == '__main__':
    print(mypow(2.10000,3))
