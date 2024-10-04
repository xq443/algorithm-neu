import heapq

class Solution: # TC: O(log(n + m))
    def median2(self, X, Y):
        m = len(X)
        n = len(Y)

        # Check if the total number of elements is even or odd
        if (m + n) % 2 == 0:
            return 0.5 * (self.findKth(X, Y, (m + n) // 2) +
                          self.findKth(X, Y, (m + n) // 2 + 1))
        else:
            return self.findKth(X, Y, (m + n) // 2 + 1)

    def findKth(self, X, Y, k):
        # Priority queue to store elements and their respective array labels
        min_heap = []
        i, j = 0, 0

        if X:
            heapq.heappush(min_heap, (X[i], 1))  # (value, label)
            i += 1
        if Y:
            heapq.heappush(min_heap, (Y[j], 2))  # (value, label)
            j += 1

        result = None

        # Extract k elements from the heap
        for _ in range(k):
            value, label = heapq.heappop(min_heap)
            result = value  # Update the result to the current smallest element

            if label == 1 and i < len(X):
                heapq.heappush(min_heap, (X[i], 1))
                i += 1
            elif label == 2 and j < len(Y):
                heapq.heappush(min_heap, (Y[j], 2))
                j += 1

        return result

# Test cases:
solution = Solution()
print(solution.median2([], [2, 3]))  # returns 2.5
print(solution.median2([1], [2, 3]))  # returns 2.0
print(solution.median2([1, 3], [2]))  # returns 2.0
print(solution.median2([1, 2], [3, 4]))  # returns 2.5
print(solution.median2([1, 2, 3, 4], [3, 4]))  # returns 3.0
print(solution.median2([0, 0, 0, 2, 2], [1, 1, 1, 1, 1]))  # returns 1.0
print(solution.median2([1, 3, 5, 7, 9], [2, 4, 6, 8, 10, 11]))  # returns 6.0
print(solution.median2([1, 3, 7, 8, 9], [2, 4, 5, 6, 10, 11]))  # returns 6.0
print(solution.median2([1], [2, 3, 4, 5, 6, 7]))  # returns 4.0
print(solution.median2([10, 20, 30, 100], [40, 60]))  # returns 35.0
