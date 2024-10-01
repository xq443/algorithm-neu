def maxSubArray(A: list):
    if not A or len(A) == 0:
        return [], 0
    
    currSum = A[0]
    max = A[0]
    
    start = end = 0
    temp = 0
    
    for i in range(1, len(A)):
        if currSum > 0:
            currSum += A[i]
        else:
            currSum = A[i]
            temp = i  # update temp start index when starting a new subarray
        
        if currSum > max:
            max = currSum
            start = temp  # update the start index of the maximum subarray
            end = i  # update the end index of the maximum subarray
    
    return A[start:end + 1], max

# Test cases
print(maxSubArray([-100]))  # Expected: ([-100], -100)
print(maxSubArray([13, -100, 20]))  # Expected: ([20], 20)
print(maxSubArray([-100, 20, -10, 60, 80]))  # Expected: ([20, -10, 60, 80], 150)
print(maxSubArray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]))
# Expected: ([18, 20, -7, 12], 43)
