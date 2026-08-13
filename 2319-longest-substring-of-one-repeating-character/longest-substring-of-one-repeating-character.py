class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        # tree[node] = (prefix, suffix, best, length)
        tree = [(0, 0, 0, 0)] * (4 * n)

        # First and last character of each segment
        first = [''] * (4 * n)
        last = [''] * (4 * n)

        def build(node, l, r):
            if l == r:
                tree[node] = (1, 1, 1, 1)
                first[node] = s[l]
                last[node] = s[l]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node)

        def merge(node):
            left = node * 2
            right = node * 2 + 1

            lp, ls, lb, llen = tree[left]
            rp, rs, rb, rlen = tree[right]

            first[node] = first[left]
            last[node] = last[right]

            if last[left] == first[right]:

                # Prefix
                prefix = lp
                if lp == llen:
                    prefix = llen + rp

                # Suffix
                suffix = rs
                if rs == rlen:
                    suffix = ls + rlen

                # Best
                best = max(lb, rb, ls + rp)

            else:
                prefix = lp
                suffix = rs
                best = max(lb, rb)

            tree[node] = (
                prefix,
                suffix,
                best,
                llen + rlen
            )

        def update(node, l, r, index, char):
            if l == r:
                tree[node] = (1, 1, 1, 1)
                first[node] = char
                last[node] = char
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            merge(node)

        build(1, 0, n - 1)

        answer = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            answer.append(tree[1][2])

        return answer