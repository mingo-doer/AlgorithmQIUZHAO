# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
#
#  例如，给定一个 3叉树 :
#
#
#
#
#
#
#
#  返回其层序遍历:
#
#  [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#
#
#
#
#  说明:
#
#
#  树的深度不会超过 1000。
#  树的节点总数不会超过 5000。
#  Related Topics 树 广度优先搜索
#  👍 98 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

#层序遍历  就是BFS
#利用队列  先进队列  对每个子树进行遍历
import collections


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        #维护一个队列
        queue = collections.deque([root])
        #队列非空
        while queue:
            level = []
            for i in range(len(queue)):

                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            res.append(level)
        return  res


# leetcode submit region end(Prohibit modification and deletion)


