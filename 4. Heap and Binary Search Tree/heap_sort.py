def left(i):
    return 2*(i + 1) - 1

def right(i):
    return 2*(i + 1)

def parent(i):
    return (i + 1)// 2 - 1

def max_heapify (A, size, i):
    l, r = left(i), right(i)

    largest = i
    if l < size and A[l] > A[largest]:
        largest = l
    if r < size and A[r] > A[largest]:
        largest  = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, size, largest)

def build_max_heap(A):
    n = len(A)
    for i in reversed(range(n)):
        max_heapify (A, n, i)

def extract_max(A, size):
    A[0], A[size - 1] = A[size - 1], A[0]
    max_heapify(A, size - 1, 0) # O(log n)
    return A[size - 1]

def heap_sort(A):
    build_max_heap(A)  # O(n)
    size = len(A)
    for i in reversed(range(1, size + 1)):
        extract_max(A, i)
    return A

a = [10, 8, 9, 7, 5, 6, 2, 4, 3, 1]
print(heap_sort(a))

heap_size = len(a)
build_max_heap(a)

print(a)
print(extract_max(a, heap_size))
print(a)
heap_size -= 1
print(extract_max(a, heap_size))
print(a)
