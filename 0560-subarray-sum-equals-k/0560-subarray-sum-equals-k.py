class Solution:
    def subarraySum(self, nums, k):
        prefix = 0
        count = 0

        mp = {0: 1}

        for num in nums:

            prefix += num

            if prefix - k in mp:
                count += mp[prefix - k]

            mp[prefix] = mp.get(prefix, 0) + 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna