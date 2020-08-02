# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
#  示例：
# 二叉树：[3,9,20,null,null,15,7],
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回其层次遍历结果：
#
#  [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
#  Related Topics 树 广度优先搜索
#  👍 575 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import collections
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




#层序遍历 深度优先
def levelOrder(root:TreeNode) :
# leetcode submit region end(Prohibit modification and deletion)

# terminator
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        level = []
        for i in range(len(queue)):
            r = queue.pop(0)
            # 一层一层的放
            level.append(r.val)
            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)
        res.append(level)
    return res






