# 您需要在二叉树的每一行中找到最大的值。
#
#  示例：
#
#
# 输入:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
#
# 输出: [1, 3, 9]
#
#  Related Topics 树 深度优先搜索 广度优先搜索
#  👍 81 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            curr_max = float('-inf')
            for _ in range(len(queue)):
                r = queue.pop(0)
                curr_max = max(curr_max,r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
                max = max(max,queue)
                res.append(curr_max)
        return res




# leetcode submit region end(Prohibit modification and deletion)
