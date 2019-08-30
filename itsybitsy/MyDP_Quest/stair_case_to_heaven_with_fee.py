"""
You can take at max 2 steps

if _ ways 1, you are already there 1

     _1
if _|   ways needed from Ground 1, G->1
       _2
     _|
if _|   ways needed from Ground 2, G->1, 1->1
                                   G->2

         _3
       _|2
     _|1
if _|   steps needed from Ground will be Ways to reach from second last step to 3
        which is FROM 2 + 1 step OR 1 + 2 leap step
        ways are 2+1



"""


def stair_case(nth, fee):
    min_fee = [None]*(nth+1)
    min_fee[0] = 0
    min_fee[1] = fee[0]
    min_fee[2] = fee[0]
    for i in range(3,nth+1):
        min_fee[i] = min(min_fee[i-1] + fee[i-1],
                         min_fee[i-2] + fee[i-2],
                         min_fee[i-3] + fee[i-3])
    print(min_fee)
    return min_fee[nth]

step_to_climb = 5
fee = [2, 1, 3, 1, 2]
print(stair_case(step_to_climb, fee))
