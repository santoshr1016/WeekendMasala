def solution(ll):
    day = 1
    alive = ll
    while True:
        die = []
        for idx in range(1, (len(alive))):
            cur = alive[idx]
            if cur > alive[idx-1]:
                die.append(alive[idx])
        if not die:
            return day
        else:
            alive = [item for item in alive if item not in die]
        day += 1


# input
level = [[3,6,2,7,5],[6,5,8,4,7,10,9]]
for item in level:
    print(solution(item))
