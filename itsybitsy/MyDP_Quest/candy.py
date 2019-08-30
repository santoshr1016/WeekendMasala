class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        L = len(ratings)
        stack = [1 for i in range(L)]
        for i in range(1,L):
            if ratings[i] > ratings[i-1]:
                stack[i] = stack[i-1] + 1
        for i in range(1,L):
            if ratings[-i] <ratings[-i-1]  :
                stack[-i-1] = max(stack[-i] + 1, stack[-i-1])
        return sum(stack)