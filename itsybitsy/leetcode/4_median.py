def find_median(nums1, nums2):
    nums1.extend(nums2)
    print(nums1.sort())
    print(nums1)
    mid = len(nums1)//2
    list_type = len(nums1)%2
    if list_type:
        return float(nums1[mid])
    else:
        return (nums1[mid] + nums1[mid-1]) / 2

l1 = [1, 3]
l2 = [2]
l1.sort()
print(find_median(l1, l2))