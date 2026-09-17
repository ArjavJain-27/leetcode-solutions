class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        # best[i] = minimum length of one valid subarray
        # completely within arr[0:i+1]
        best = [float('inf')] * n

        # prefix_sum -> latest index
        prefix = {0: -1}

        prefix_sum = 0
        answer = float('inf')

        for i in range(n):
            prefix_sum += arr[i]

            # First, carry forward the best subarray found so far
            if i > 0:
                best[i] = best[i - 1]

            # Need prefix_sum - target before current position
            needed = prefix_sum - target

            if needed in prefix:
                j = prefix[needed] + 1
                length = i - j + 1

                # If there is a valid subarray before j
                if j > 0 and best[j - 1] != float('inf'):
                    answer = min(answer, length + best[j - 1])

                # This is the best single subarray ending at i
                best[i] = min(best[i], length)

            # Store current prefix sum
            prefix[prefix_sum] = i

        return -1 if answer == float('inf') else answer