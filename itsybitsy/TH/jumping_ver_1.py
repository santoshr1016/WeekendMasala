def solution(a):
    count = 0
    end_of_list = len(a)-1
    start_idx = 0
    while True:
        next_idx = a[start_idx] + start_idx
        count += 1
        if next_idx > end_of_list:
            break
        start_idx = next_idx
    return count

# a = [2, 3, -1, 1, 3]
a = [1, 1, -1, 1]
print(solution(a))
