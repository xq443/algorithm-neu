def bubbleSort(A):
    n = len(A)
    for i in range(n - 1):
        swap = False 
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swap = True
                
        if not swap: # if the first scan does not exist swap, the array is already sorted
            break
    return A
        
        
print(bubbleSort([-100, 13, 20])) # returns [-100, 13, 20]
print(bubbleSort([13, -100, 20])) # returns [-100, 13, 20]
print(bubbleSort([-100, 20, -10, 60, 80])) # returns [-100, -10, 20, 60, 80]
print(bubbleSort([-100, -10, 20, 60, 80]))
        