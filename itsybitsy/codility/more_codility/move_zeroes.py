def solution(the_list):
    left = 0
    mid = 0
    right = len(the_list)-1
    while mid <= right:
        if the_list[mid] == 0:
            the_list[left], the_list[mid] = the_list[mid], the_list[left]
            mid += 1
            left += 1
        elif the_list[mid]:
            mid += 1
    res = the_list[left:]
    for i in range(left):
        res.append(0)
    print(res)


inp = [0, 1, 0, 3, 12]
solution(inp)

'''
x = 0
count = 0
for i in range(len(nums)):
	if(nums[i]!=0):
		nums[x]=nums[i]
		x+=1
	else:
		count+=1
        
for i in range(len(nums)-1,-1,-1):
	if(count>0):
		nums[i] = 0
		count-=1
'''
