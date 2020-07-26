# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]
#
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树
#  👍 314 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归
#前序遍历  根左右
def preorderTraversal( root) :
# leetcode submit region end(Prohibit modification and deletion)
    res = []
    if not root:
        return []
    def travel(root):
        res.append(root.val)
        travel(root.left)
        travel(root.right)
    travel(root)
    return res

#迭代 颜色标记法
    #新节点为白色 已访问的节点为灰色
    #如果遇到节点为白色 则将其标记为灰色 然后将其节点按顺序入栈
    #如果遇到的节点是灰色 将节点的值输出
def preorderTravelsal_loop(root):
    white , gray = 0 , 1
    res = []
    stack = [(white,root)]
    while stack:
        color , node = stack.pop()
        if node is None: continue
        if color == white:
            stack.append((white,node.right))
            stack.append((white,node.left))
            stack.append((gray,node))
        else:
            res.append(node.val)
    return res



