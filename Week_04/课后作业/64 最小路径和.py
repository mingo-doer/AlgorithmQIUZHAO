# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
#  说明：每次只能向下或者向右移动一步。
#
#  示例:
#
#  输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#
#  Related Topics 数组 动态规划
#  👍 612 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        weight = len(grid[0])
        # 从上到下
        for i in range(height):

            # 从左到右
            for j in range(weight):
                if j > 0 and i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif i > 0 and j == 0:
                    grid[i][j] += grid[i - 1][j]
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])

        return grid[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
