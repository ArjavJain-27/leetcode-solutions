class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        n = len(s)
        ans = []

        for i in range(n):
            t = ord(target[i]) - ord('a')

            # Try to keep prefix equal to target
            if freq[t] > 0:
                freq[t] -= 1
                ans.append(target[i])
                continue

            # Can't match target[i].
            # Try to make this position greater.
            for c in range(t + 1, 26):
                if freq[c] > 0:
                    freq[c] -= 1

                    result = ''.join(ans) + chr(c + ord('a'))

                    for j in range(26):
                        result += chr(j + ord('a')) * freq[j]

                    return result

            # Can't make current position greater.
            # Backtrack.
            break

        # We matched the whole target.
        # We still need to backtrack to make the answer greater.
        while ans:
            prev = ans.pop()
            prev_val = ord(prev) - ord('a')
            freq[prev_val] += 1

            # Try the smallest character greater than prev
            for c in range(prev_val + 1, 26):
                if freq[c] > 0:
                    freq[c] -= 1

                    result = ''.join(ans) + chr(c + ord('a'))

                    for j in range(26):
                        result += chr(j + ord('a')) * freq[j]

                    return result

        return ""