# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
#
#
#
#  示例：
#
#  输入：3
# 输出：
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#
#
#
#  提示：
#
#
#  0 <= n <= 8
#
#  Related Topics 树 动态规划
#  👍 553 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#生成不同的二叉搜索树
# 递归
# 当前集合是(start,end)
# 根据二叉搜索树的性质，树可以被划分为 generate（start，i-1）和generate(i+1,end)
class Solution:
    def generateTrees(self, n: int) :
        if n:
            return self.generate(1,n)
        else:
            return []
    def generate(self,start,end):
        if start > end :
            return [None,]
        allTree = []
        #枚举所有节点
        for i in range(start,end + 1):
            #取左右子树
            leftTree = self.generate(start , i-1)
            rightTree = self.generate(i+1 , end)

            #拼接
            for l in leftTree:
                for r in rightTree:
                    currTree = TreeNode(i)
                    currTree.left = l
                    currTree.right = r
                    allTree.append(currTree)

    #     返回值
        return allTree