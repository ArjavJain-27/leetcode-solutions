class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Check whether palindrome is possible
        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        # Number of each character available in left half
        half = [x // 2 for x in cnt]

        # We try to make the left half as close to target's left half
        # as possible, but strictly greater.
        left_len = n // 2

        # First try to construct exactly target's left half
        used = [0] * 26
        possible = True

        for i in range(left_len):
            x = ord(target[i]) - ord('a')

            if half[x] == 0:
                possible = False
                break

            half[x] -= 1
            used[x] += 1

        # If target's left half can be formed, check whether
        # its corresponding palindrome is already > target.
        if possible:
            left = target[:left_len]

            candidate = left + middle + left[::-1]

            if candidate > target:
                return candidate

        # Restore counts
        for i in range(26):
            half[i] += used[i]

        # Find the rightmost position where we can increase
        # target's left half.
        for i in range(left_len - 1, -1, -1):

            # Characters before i must match target
            prefix_count = [0] * 26

            for j in range(i):
                x = ord(target[j]) - ord('a')
                prefix_count[x] += 1

            # Remove prefix from available characters
            remaining = half[:]

            valid = True

            for c in range(26):
                remaining[c] -= prefix_count[c]
                if remaining[c] < 0:
                    valid = False
                    break

            if not valid:
                continue

            current = ord(target[i]) - ord('a')

            # Find smallest character > target[i]
            for c in range(current + 1, 26):

                if remaining[c] > 0:
                    # Build left half
                    left = target[:i] + chr(c + ord('a'))

                    remaining[c] -= 1

                    # Fill rest with smallest characters
                    for x in range(26):
                        left += chr(x + ord('a')) * remaining[x]

                    # Make palindrome
                    ans = left + middle + left[::-1]

                    if ans > target:
                        return ans

                    remaining[c] += 1

        return ""