# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
#  此外，你可以假设该网格的四条边均被水包围。
#
#
#
#  示例 1:
#
#  输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#
#
#  示例 2:
#
#  输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集
#  👍 681 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dfs(self, grid, row, col):
        grid[row][col] = 0
        for (x, y) in [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    self.dfs(grid, row, col)
        return count
