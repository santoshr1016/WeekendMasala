# Complete the merge_overlapping_intervals function below.
def find_hotels(intervals):
    si = sorted(intervals, key=lambda tup: tup[1], reverse=True)
    s = set()
    for item in si:
        if item[0] not in s:
            print(item[0])
            s.add(item[0])

def merge_overlapping_intervals():
    n = int(input())
    l = list()
    for i in range(n):
        t = [int(i) for i in input().strip().split(" ")]
        l.append(tuple(t))
    ml = find_hotels(l)
    # print(len(ml))
    # for item in ml:
    #     print(item[0], item[1] )

merge_overlapping_intervals()