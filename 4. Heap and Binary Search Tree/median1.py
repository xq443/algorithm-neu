class Solution:
    def median1(self, X, Y):
        a = len(X)
        b = len(Y)

        # in this case, a == b
        # if a > b:  Ensure X is the smaller array
        #     return self.median1(Y, X)

        total_len = a + b
        a_start = 0
        a_end = a

        while a_start <= a_end:
            a_cut = (a_start + a_end) // 2  # Cut in X (left side)
            b_cut = (total_len + 1) // 2 - a_cut  # Cut in Y (left side)

            # Use conditional expressions to assign values to aL, bL, aR, bR
            aL = X[a_cut - 1] if a_cut > 0 else float('-inf')
            bL = Y[b_cut - 1] if b_cut > 0 else float('-inf')
            aR = X[a_cut] if a_cut < a else float('inf')
            bR = Y[b_cut] if b_cut < b else float('inf')

            if aR < bL:
                a_start = a_cut + 1  # Move to the right
            elif aL > bR:
                a_end = a_cut - 1  # Move to the left
            else:
                # We have partitioned the arrays correctly
                if total_len % 2 == 0:
                    # Even total length
                    return (max(aL, bL) + min(aR, bR)) / 2
                else:
                    # Odd total length
                    return max(aL, bL)

        return -1  # This line should never be reached if input arrays are sorted

# Create an instance of Solution
solution = Solution()

# Test cases
print(solution.median1([1], [2]))  # returns 1.5
print(solution.median1([1, 2], [3, 4]))  # returns 2.5
print(solution.median1([2, 3], [1, 4]))  # returns 2.5
print(solution.median1([1, 3, 5, 7], [2, 4, 6, 8]))  # returns 4.5
print(solution.median1([1, 2, 3, 4], [5, 6, 7, 8]))  # returns 4.5
print(solution.median1([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))  # returns 5.5
print(solution.median1([1, 3, 7, 8, 9], [2, 4, 5, 6, 10]))  # returns 5.5
print(solution.median1([10, 20, 30, 100], [15, 40, 60, 90]))  # returns 35.0
