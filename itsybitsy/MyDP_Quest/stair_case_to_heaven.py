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


def stair_case(nth):
    memo = [None]*(nth+1)
    memo[0] = 1
    memo[1] = 1
    for step in range(2,nth+1):
        memo[step] = memo[step-1] + memo[step-2]
    print(memo)
    return memo[nth]

step_to_climb = 7
print(stair_case(step_to_climb))
