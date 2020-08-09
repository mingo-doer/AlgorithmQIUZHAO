# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
#  相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
#
#
#
#  例如，给定三角形：
#
#  [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#
#
#  自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
#
#
#  说明：
#
#  如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
#  Related Topics 数组 动态规划
#  👍 557 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

# leetcode submit region end(Prohibit modification and deletion)
# 第一想法是 找出每个二维矩阵中最小元素相加， 但是题目有限制 是 只能移动到相邻节点上
# 所以只能用动态规划
        height = len(triangle)

        # 从上到下
        for i in range(height - 2, -1, -1):
            # 从左到右
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

# 优秀优化代码  复杂度o(n)
def minimumTotal( triangle):
    res = triangle[-1]
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            res[j] = min(res[j],res[j+1]) + triangle[i][j]
    return res[0]