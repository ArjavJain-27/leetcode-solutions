class Solution:
    def nodesBetweenCriticalPoints(self, head):
        min_dist = float('inf')
        max_dist = 0

        first = -1
        prev_critical = -1

        index = 1
        prev = head
        curr = head.next

        while curr.next:
            next_node = curr.next

            # Check if curr is a critical point
            is_critical = (
                (curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)
            )

            if is_critical:

                # First critical point
                if first == -1:
                    first = index

                # We already have a previous critical point
                else:
                    min_dist = min(
                        min_dist,
                        index - prev_critical
                    )

                    max_dist = max(
                        max_dist,
                        index - first
                    )

                prev_critical = index

            prev = curr
            curr = next_node
            index += 1

        # Fewer than 2 critical points
        if first == -1 or first == prev_critical:
            return [-1, -1]

        return [min_dist, max_dist]