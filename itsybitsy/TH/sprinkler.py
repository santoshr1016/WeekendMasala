numbers = int(input())
num = [int(input()) for _ in range(numbers)]


def count_up(start = 1):
    while True:
        yield start
        start += 1


def get_ones(val):
    beauty = 0
    while val > 0:
        beauty = beauty + (val & 1)
        val = val // 2
    return beauty

for i in num:
    count = 0
    for val in count_up():
        count += get_ones(val)
        if count >=i:
            break
    print(val)
