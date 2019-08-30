deno = [1,2,5,10,20,50,100,500,1000]
size = len(deno)


def coins(value):
    ans = []
    i = size -1

    while i >=0:
        while value >= deno[i]:
            value -= deno[i]
            ans.append(deno[i])
        i -= 1
    for coin in ans:
        print(coin, end=" ")

value = 913
coins(value)
