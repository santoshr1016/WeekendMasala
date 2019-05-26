def duplicate(A):
    A.sort()
    for i in range(len(A)):
        if (A[abs(A[i])] < 0):
            print("duplicate exist")
            return True
        else:
            A[A[i]] = -1 * A[A[i]]

print(duplicate(A=[1,2,3,4,5,6,7,4]))