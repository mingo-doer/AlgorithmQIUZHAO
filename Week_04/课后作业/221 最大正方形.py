# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
#  示例:
#
#  输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4
#  Related Topics 动态规划
#  👍 502 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # dp不应该在原数组上改变，因为会把原数据改变，所以要去创建自己的动态空间
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0
        height = len(matrix)
        weight = len(matrix[0])
        maxside = 0
        res = 0
        # 从上到下
        # 创建状态空间
        # dp = [[0] * weight for _ in range(height)]
        for i in range(height):
            # 从左到右
            for j in range(weight):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        matrix[i][j] == '1'
                    else:
                        matrix[i][j] = min(int(matrix[i - 1][j]), int(matrix[i][j - 1]), int(matrix[i - 1][j - 1])) + 1
                    maxside = max(maxside, int(matrix[i][j]))

        res = maxside * maxside
        return res

# leetcode submit region end(Prohibit modification and deletion)

#
def maximalSquare(matrix):
    if not matrix:
        return 0
    height = len(matrix)
    weight = len(matrix[0])
    maxside = 0
    res = 0
    # 从上到下
    # 创建状态空间
    dp = [[0] * weight for _ in range(height)]
    print(dp)
    for i in range(height):
        # 从左到右
        for j in range(weight):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                maxside = max(maxside, dp[i][j])

    res = maxside * maxside
    return res

if __name__ == '__main__':
    res= maximalSquare([['1']])
    print(res)
