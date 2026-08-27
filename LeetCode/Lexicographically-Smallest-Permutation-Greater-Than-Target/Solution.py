1class Solution:
2    def lexGreaterPermutation(self, s: str, target: str) -> str:
3        freq = [0] * 26
4
5        for ch in s:
6            freq[ord(ch) - ord('a')] += 1
7
8        n = len(s)
9        ans = []
10
11        for i in range(n):
12            t = ord(target[i]) - ord('a')
13
14            # Try to keep prefix equal to target
15            if freq[t] > 0:
16                freq[t] -= 1
17                ans.append(target[i])
18                continue
19
20            # Can't match target[i].
21            # Try to make this position greater.
22            for c in range(t + 1, 26):
23                if freq[c] > 0:
24                    freq[c] -= 1
25
26                    result = ''.join(ans) + chr(c + ord('a'))
27
28                    for j in range(26):
29                        result += chr(j + ord('a')) * freq[j]
30
31                    return result
32
33            # Can't make current position greater.
34            # Backtrack.
35            break
36
37        # We matched the whole target.
38        # We still need to backtrack to make the answer greater.
39        while ans:
40            prev = ans.pop()
41            prev_val = ord(prev) - ord('a')
42            freq[prev_val] += 1
43
44            # Try the smallest character greater than prev
45            for c in range(prev_val + 1, 26):
46                if freq[c] > 0:
47                    freq[c] -= 1
48
49                    result = ''.join(ans) + chr(c + ord('a'))
50
51                    for j in range(26):
52                        result += chr(j + ord('a')) * freq[j]
53
54                    return result
55
56        return ""