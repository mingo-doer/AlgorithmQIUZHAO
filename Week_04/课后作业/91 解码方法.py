# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
#
#  'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
#  给定一个只包含数字的非空字符串，请计算解码方法的总数。
#
#  示例 1:
#
#  输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#
#
#  示例 2:
#
#  输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#
#  Related Topics 字符串 动态规划
#  👍 462 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDecodings(self, s: str) -> int:
        # 判空
        if not s or s[0] == '0':
            return 0
        # 初始化dp
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1
        # 遍历s (1,n)
        for i in range(1,len(s)):
            if (s[i] == '0'):
                print(s[i])
                if (s[i-1] == '1' or s[i-1] == '2'):
                    # 当前位置的解码方式和上一位相同
                    dp[i+1] = dp[i-1]
                else:
                    print(1)
                    return 0
            else:
                # 判断何时既可以自身解码也可以和前一位结合
                # 可以与上一位结合的
                if s[i-1] == '1' or s[i-1] == '2' and ('1'<=s[i]<='6' ):
                    dp[i+1] = dp[i] + dp[i-1]
                else:
                    dp[i+1] = dp[i]
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    res = Solution().numDecodings('230')
    print(res)
