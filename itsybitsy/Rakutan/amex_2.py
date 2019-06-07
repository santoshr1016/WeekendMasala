def solution():
    n = input()
    l = [int(num) for num in input().split(' ')]
    for item in l:
        for num in range(1, item+1):
            if not num % 15:
                print("FizzBuzz")
            elif not num % 3:
                print("Fizz")
            elif not num % 5:
                print("Buzz")
            else:
                print(num)


print(solution())
