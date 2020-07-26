# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
#  假设一个二叉搜索树具有如下特征：
#
#
#  节点的左子树只包含小于当前节点的数。
#  节点的右子树只包含大于当前节点的数。
#  所有左子树和右子树自身必须也是二叉搜索树。
#
#
#  示例 1:
#
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#
#
#  示例 2:
#
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#
#  Related Topics 树 深度优先搜索
#  👍 678 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#验证二叉搜索树是否是有效的


#方法一 最大值和最小值
#当前节点为左子树的上届 为右子树的下界
def isValidBST(root):
# leetcode submit region end(Prohibit modification and deletion)
    def travel(node,lower,upper):
        if not node:
            return True
        val = node.val
        if val <=lower or val >= upper:
            return False
        if not travel(node.right,val,upper):
            return False
        if not travel(node.left,lower,val):
            return False
        return True
    return travel(root, -float('inf'),float('inf'))

# bst-》中序遍历是 递增的
# 使用中序遍历结果 如果是递增是那就是二叉搜索树 反之就不是
def isvaildBST(root):
    res = []

    def helper(root):
        if not root:
            return
        helper(root.left)
        res.append(root.val)
        helper(root.right)

    helper(root)
    return res == sorted(res) and len(set(res)) == len(res)

