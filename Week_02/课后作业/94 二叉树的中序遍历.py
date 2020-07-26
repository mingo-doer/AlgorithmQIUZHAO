# 给定一个二叉树，返回它的中序 遍历。
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
# 输出: [1,3,2]
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树 哈希表
#  👍 585 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#中序遍历  左根右
 # 对树的操作就是明白迭代 和  递归  终止条件
 #超哥代码模板：
 #递归
def inorderTraversal( root: TreeNode) :
# leetcode submit region end(Prohibit modification and deletion)
    res = []
    def travel(root):
        if not root:
            return
        travel(root.left)
        res.append(root.val)
        travel(root.right)
    travel(root)
    return res

#迭代  使用栈

def inorderTravelsal_loop(root):
    res = []
    stack = []
    #p regard as pointer
    p = root
    while p or stack :
        #左子树入栈
        while p:
            stack.append(p)
            p = p.left
        #输出栈顶
        p = stack.pop()
        res.append(p.val)
        #开始右子树
        p = p.right
    return res
