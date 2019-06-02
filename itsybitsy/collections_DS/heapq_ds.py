import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# Top 3 elements
print(heapq.nlargest(3, nums))

# Lowest 3 elements
print(heapq.nsmallest(3, nums))

portfolio = [
       {'name': 'IBM', 'shares': 100, 'price': 91.1},
       {'name': 'AAPL', 'shares': 50, 'price': 543.22},
       {'name': 'FB', 'shares': 200, 'price': 21.09},
       {'name': 'HPQ', 'shares': 35, 'price': 31.75},
       {'name': 'YHOO', 'shares': 45, 'price': 16.35},
       {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# Top 3 shares expensive
print(heapq.nlargest(3, portfolio, key=lambda x:x['price']))

# top 3 cheapest
print(heapq.nsmallest(3, portfolio, key=lambda x: x['price']))


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(nums)
print(nums)
# heapq.heappop()
print(sorted(nums)[-3:])
print(sorted(nums)[:3])

hq = []
for item in nums:
       heapq.heappush(hq, item)
print(hq)
print(heapq.heappop(hq))