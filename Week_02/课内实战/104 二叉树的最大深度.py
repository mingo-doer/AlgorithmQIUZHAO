# 给定一个二叉树，找出其最大深度。
#
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
#  说明: 叶子节点是指没有子节点的节点。
#
#  示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  返回它的最大深度 3 。
#  Related Topics 树 深度优先搜索
#  👍 615 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#最大深度 就是遍历最大子树长度+1

#递归法 dfs
class Solution:
    def maxDepth(self, root):
# leetcode submit region end(Prohibit modification and deletion)
        if not root:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height,right_height)+1

# 迭代 使用DFS策略访问每个节点 在每次访问时更新最大深度
# 所以我们从包含根结点且相应深度为 1 的栈开始。
# 然后我们继续迭代：将当前结点弹出栈并推入子结点。每一步都会更新深度。
def maxDepth(root):
    stack = []
    if root:
        stack.append((1,root))
    depth=0
    while stack:
        current_depth , root =stack.pop()
        if  root:
            depth = max(depth,current_depth)
            stack.append((current_depth+1,root.left))
            stack.append((current_depth+1,root.right))
    return depth

