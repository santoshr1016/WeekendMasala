def solution(the_list):
    left = 0
    mid = 0
    right = len(the_list)-1
    while mid <= right:
        if the_list[mid] == 0:
            the_list[left], the_list[mid] = the_list[mid], the_list[left]
            mid += 1
            left += 1
        elif the_list[mid] == 1:
            mid += 1
    return the_list


def solution_2(the_list):
    l_1s = []
    l_0s = []
    size = len(the_list)
    for i in range(size):
        if the_list[i]:
            l_1s.append(the_list[i])
        else:
            l_0s.append(the_list[i])
    print(l_1s)
    print(l_0s)
    return l_0s + l_1s
    print(l_0s)

the_list = [0,0,1,0,1,1,0,1,0,1]
print(solution(the_list))
t_list = [0,0,1,0,1,1,0,1,0,1]
print(solution_2(t_list))