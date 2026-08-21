# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], max_on_path: int) -> int:
            if not node:
                return 0

            is_good = 1 if node.val >= max_on_path else 0
            new_max = max(max_on_path, node.val)

            left_good = dfs(node.left, new_max)
            right_good = dfs(node.right, new_max)

            return is_good + left_good + right_good

        # root is always on a path by itself, so start max with root.val
        return dfs(root, root.val)