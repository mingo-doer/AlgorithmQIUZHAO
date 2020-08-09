# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。
#
#
#
#  示例 1:
#
#  输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
#
#  示例 2:
#
#  输入: coins = [2], amount = 3
# 输出: -1
#
#
#
#  说明:
# 你可以认为每种硬币的数量是无限的。
#  Related Topics 动态规划
#  👍 724 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 暴力递归  超出时间限制
    def coinChange(self, coins, amount) -> int:
#         确定子问题

        def dp(n):
#             边界条件
            if n == 0 :
                return 0
            if n < 0 :
                return -1
#             求最小值 所以初始化 正无穷 负无穷 float('-inf')
            coins.reverse()
            print(coins.reverse())
            res = float('INF')
#             要凑出 金额n 至少要np(n)个
            for coin in coins[::-1]:
                # 定义子问题 状态空间
                subproblem = dp(n - coin)
                if subproblem == -1:
                    continue
                res = min(res, 1 + subproblem)

            return res if res != float('INF') else -1
        return dp(amount)
# dp
def coinChange(coins, amount):
    dp = [float('INF')] * (amount+1)
    dp[0] =0
    for i in range(1,amount+1):
        for coin in coins:
            if i < coin:
                continue
            #     重点理解这一句话
            dp[i] = min(dp[i], dp[i-coin] +1)
    return dp[-1] if dp[-1] != float('INF') else -1

if __name__ == '__main__':
    res = coinChange([1,2,5],11)
    print(res)
    # coins = [ 1,2,5]
    # print(coins.reverse())


# leetcode submit region end(Prohibit modification and deletion)
