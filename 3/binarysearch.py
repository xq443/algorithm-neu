def binary_search(array, value):
    return binary_search_recursive(array, 0, len(array) - 1, value)
def binary_search_recursive(array, left, right, value):
    if left > right:
        return -1
    mid = (left + right) // 2  
    if value == array[mid]:
        return mid
    if value > array[mid]:
        return binary_search_recursive(array, mid + 1, right, value)
    return binary_search_recursive(array, left, mid - 1, value)

print(binary_search([0,11,22,33,44,55,66,77,88], 77))



def binary_search_iterative(array, value): 
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2 
        if value == array[mid]:
            return mid
        if value > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(binary_search_iterative([0,11,22,33,44,55,66,77,88], 77))