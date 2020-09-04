# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
#
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
#
#  示例 1:
#
#
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
#
#
#  示例 2:
#
#
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
#
#
#  注意:
#
#
#  输入的字符串长度不会超过1000。
#
#  Related Topics 字符串 动态规划
#  👍 294 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
#         定义子问题
# i in height  j in i+1
# 1、 s[i]==s[j]时是回文串
# 2、 s[i]==s[j] and (j-i<2 or dp[i-1][j+1])
# 定义状态空间
#  [0]*n 是一行 n 个 0 然后循环 3层
#dp = [[0]*n  for _ in range(n)]
# 暴力法
        res = 0
        n = len(s)
        dp = [[0] *n for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                # i - j < 2 : i-j ==0 or i -j == 1 也就是相邻或者相同位置的两个
                # 为什么不能 j - i ?
                if s[i] == s[j] and (i -j < 2 or dp[i-1][j+1])  :
                    res += 1
                    dp[i][j] = 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
