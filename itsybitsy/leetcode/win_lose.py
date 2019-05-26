def win_lose(energy_list):
    villans = energy_list[0]
    heros = energy_list[1]
    villans.sort()
    heros.sort()
    win = True
    for i in range(len(heros)):
        if heros[i] - villans[i] <= 0:
            win = False
            break
    return "WIN" if win else "LOSE"


for i in range(int(input())):
    num_players = int(input())
    # energy_list = []
    # for j in range(2):
    #     energy_list.append([int(i) for i in input().strip().split()])

    energy_list = [[int(ii) for ii in input().strip().split()] for jj in range(2)]
    print(energy_list)
    print(win_lose(energy_list))

'''
1
6
112 243 512 343 90 478
500 789 234 400 452 150
5
10 20 30 40 50
40 50 60 70 80
True

'''





