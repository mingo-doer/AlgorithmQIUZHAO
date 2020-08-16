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
#  👍 707 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        height = len(grid)
        if height == 0:
            return 0
        def gridmarker(grid,i,j):
            # terminator
            if i < 0 or j < 0 or i >= height or j >= len(grid[0]) or grid[i][j] != '1':
                return
            # process logic
            grid[i][j] = 0
            # drill down
            gridmarker(grid,i+1,j)
            gridmarker(grid,i-1,j)
            gridmarker(grid,i,j+1)
            gridmarker(grid,i,j-1)
            # reverse

        for i in range(height):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # 处理逻辑层
                    count += 1
                    gridmarker(grid,i,j)
        return count

# leetcode submit region end(Prohibit modification and deletion)
