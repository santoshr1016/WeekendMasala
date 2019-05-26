def solution(the_list):
    single = [i for i in the_list if i//10 == 0]
    double = [i for i in the_list if i//10 > 0]
    single.sort(reverse=True)
    double.sort(reverse=True)
    ret = []

    print(ret)


the_list = [1,34,3,98,9,76,45,4]
print(solution(the_list))