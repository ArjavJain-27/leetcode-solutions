class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")

        count = 0

        # First window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        ans = count

        # Slide the window
        for i in range(k, len(s)):

            # New character enters
            if s[i] in vowels:
                count += 1

            # Old character leaves
            if s[i-k] in vowels:
                count -= 1

            ans = max(ans, count)

        return ans