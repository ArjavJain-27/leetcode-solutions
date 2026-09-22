from typing import List


class Solution:
    def resultArray(
        self, nums: List[int], k: int, queries: List[List[int]]
    ) -> List[int]:

        n = len(nums)

        # tree[node] = (product % k, count of prefixes for each remainder)
        tree = [(1 % k, [0] * k) for _ in range(4 * n)]

        def merge(left, right):
            left_prod, left_cnt = left
            right_prod, right_cnt = right

            # Product of the whole combined segment
            prod = (left_prod * right_prod) % k

            # Prefixes completely inside left
            cnt = left_cnt[:]

            # Prefixes that start in left and continue into right
            for r in range(k):
                cnt[(left_prod * r) % k] += right_cnt[r]

            return prod, cnt

        def build(node, l, r):
            if l == r:
                value = nums[l] % k

                cnt = [0] * k
                cnt[value] = 1

                tree[node] = (value, cnt)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, value):
            if l == r:
                value %= k

                cnt = [0] * k
                cnt[value] = 1

                tree[node] = (value, cnt)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Permanent update
            update(1, 0, n - 1, index, value)

            # We only care about nums[start ... n-1]
            _, cnt = query(1, 0, n - 1, start, n - 1)

            answer.append(cnt[x])

        return answer