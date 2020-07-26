# 给定一个 N 叉树，返回其节点值的后序遍历。
#
#  例如，给定一个 3叉树 :
#
#
#
#
#
#
#
#  返回其后序遍历: [5,6,3,2,4,1].
#
#
#
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树
#  👍 85 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""



def postorder(root) :
# 这是递归的方法  还需要要去学会迭代的方法
# leetcode submit region end(Prohibit modification and deletion)
    res = []
    def travel(root):
        if not root:
            return
        children = root.children
        for child in children:
            travel(child)
        res.append(root.val)
    travel(root)
    return res
