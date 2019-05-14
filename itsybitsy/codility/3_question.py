
def solution(A, B):
    a_array = ['a']* A
    b_array = ['b']* B
    result = []
    i =0
    j = 0
    while i < A and j < B:
        result.append(a_array[i])
        result.append(b_array[j])
        i += 1
        j += 1
    if i < A:
        upto = i+2
        while i <= A and i <upto:
            result.append('a')
            i += 1
    if j < B:
        upto = j+2
        while j <= B and j <upto:
            result.append('b')
            j += 1

    return result



A = 1
B = 4
print(solution(A, B))