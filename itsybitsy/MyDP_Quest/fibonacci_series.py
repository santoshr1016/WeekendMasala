class Fibonacci():
    def __init__(self):
        self.memo = dict()
        self.memo[0] = 0
        self.memo[1] = 1

    def dp_approach(self, n):
        if n in self.memo:
            return self.memo.get(n)

        self.memo[n-1] = self.dp_approach(n-1)
        self.memo[n-2] = self.dp_approach(n-2)

        sum_of_previous = self.memo[n-1] + self.memo[n-2]
        self.memo[n] = sum_of_previous

        return sum_of_previous

    def naive(self, n):
        # f(n) = f(n-1) + f(n-2)
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.naive(n-1) + self.naive(n-2)

fib = Fibonacci()
# print(fib.naive(11))
print(fib.dp_approach(3))
