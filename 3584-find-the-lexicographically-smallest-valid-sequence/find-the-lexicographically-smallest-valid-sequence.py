class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # suf[i] = maximum number of characters of word2
        # that can be matched exactly using word1[i:]
        suf = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1]

            if j >= 0 and word1[i] == word2[j]:
                suf[i] = max(suf[i], m - j)
                j -= 1

        ans = []
        p = 0
        used = False

        for j in range(m):
            while p < n:
                # Normal match
                if word1[p] == word2[j]:
                    ans.append(p)
                    p += 1
                    break

                # Use our one allowed change
                if not used:
                    # Need to match word2[j+1:] exactly
                    need = m - (j + 1)

                    if suf[p + 1] >= need:
                        ans.append(p)
                        p += 1
                        used = True
                        break

                p += 1
            else:
                return []

        return ans