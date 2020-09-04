# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
#  你可以对一个单词进行如下三种操作：
#
#
#  插入一个字符
#  删除一个字符
#  替换一个字符
#
#
#
#
#  示例 1：
#
#  输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
#
#  示例 2：
#
#  输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#  Related Topics 字符串 动态规划
#  👍 1117 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        print(n1,n2)
#         构造dp方程
        dp = [[0] * (n2 + 1) for _ in range( n1 + 1)]
        if n1 == 0 :
            return n2
        if n2 == 0 :
            return n1

        # 第一行 是 word1 为空变成 word2 最少步数，就是插入操作
        for i in range(1,n2 + 1):
            dp[0][i] = dp[0][i-1] + 1
        #     第一列 是 word2 为空，需要的最少步数，就是删除操作
        for i in range(1,n1+1):
            dp[i][0] = dp[i-1][0] + 1
        #     只需要从非空再来判断
        for i in range(1,n1 + 1):
            for j in range(1,n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    res = Solution().minDistance("","")
    print(res)