class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")

        count = sum(c in vowels for c in s[:k])
        ans = count

        for i in range(k, len(s)):
            count += (s[i] in vowels)
            count -= (s[i - k] in vowels)

            ans = max(ans, count)

        return ans