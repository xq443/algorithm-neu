import random
import heapq as hp

def partition(A, randomize = False):

    if randomize:
        pivot = random.randrange(len(A))
        A[0], A[pivot] = A[pivot], A[0]

    i = 0 # to store last index of the first partition
    for j in range(1, len(A)):
        if A[j] < A[0]: # we choose A[0] as a pivot, so compare with A[0]
            # If A[j] < A[0], we have to move A[j] to the first partition.  
            # So, swap the first element of the second partition (A[i+1]) with A[j],
            # and then increment i.
            A[i+1], A[j] = A[j], A[i+1]
            i += 1
        # Note that if A[j] >= A[0], we put A[j] into the second partition.
        # In this case, we don't have to change anything (all numbers are already in the second partition).

    # Now, we need to move the pivot between the first and the second partitions.
    # This is done by swapping the last element of the first partition with the pivot
    A[0], A[i] = A[i], A[0]
    return i # returning the index of the pivot

def quickSort(A, randomize = False):
    if len(A) < 2:
        return A
    k = partition(A, randomize)
    return quickSort(A[:k], randomize) + [A[k]] + quickSort(A[k+1:], randomize)

def select(A, i): #i = 1 .. len(A)
    if len(A) == 1:
        return A[0]
    k = partition(A)
    if i == k + 1:
        return A[k]
    elif i < k + 1:
        return select(A[:k], i)
    else:
        return select(A[k+1:], i - k - 1)

def median(A):
    n = len(A)
    if n % 2:
        return select(A, len(A)//2 + 1)
    else:
        return (select(A, len(A)//2) + select(A, len(A)//2 + 1))/2

test = [53, 10, 1, 70, 77, 30, 97, 42]
test = [822, 35, 294, 322, 175, 67, 517, 987, 154, 473]
print(quickSort(test))
print(quickSort(test, True))
for i in range(len(test)):
    print("{0}th smallest element is {1}".format(i+1, select(test, i+1)))
print("median:", median(test))
print("==========================")
test = [1,2,3,4,5,6,7,8,9,10]
print("Sorting:", test)
print(quickSort(test))
print(quickSort(test, True))

print("==========================")
test = [10,9,8,7,6,5,4,3,2,1]
print("Sorting:", test)
print(quickSort(test))
print(quickSort(test, True))

print(quickSort([251, 649, 888, 88, 340, 365, 230, 478, 112, 994]))


a = [96, 67, 33, 61, 97, 59, 88, 2, 79, 29]
b = []
for i in range(len(a)):
    hp.heappush(b, a[i])

print(b)
