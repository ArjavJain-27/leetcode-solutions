class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return 0, 0

            # Get sum and count from left subtree
            left_sum, left_count = dfs(node.left)

            # Get sum and count from right subtree
            right_sum, right_count = dfs(node.right)

            # Include current node
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            # Check average
            if total_sum // total_count == node.val:
                ans += 1

            # Return information to parent
            return total_sum, total_count

        dfs(root)

        return ans