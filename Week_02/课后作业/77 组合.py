# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
#  示例:
#
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#  Related Topics 回溯算法
#  👍 320 👎 0

# 这是一个回溯法函数，它将第一个添加到组合中的数和现有的组合作为参数。 backtrack(first, curr)
#
# 若组合完成- 添加到输出中。
#
# 遍历从 first t到 n的所有整数。
#
    # 将整数 i 添加到现有组合 curr中。
#
    # 继续向组合中添加更多整数 :
    # backtrack(i + 1, curr).
#
# 将 i 从 curr中移除，实现回溯。


# leetcode submit region begin(Prohibit modification and deletion)

def combine(n, k):
    #first 是从1开始而不是0
    def backtrack(first=1,curr = []):
        if len(curr) == k:
            #curr 和 curr[:]区别
            res.append(curr[:])
        for i in range(first, n+1):
            curr.append(i)
            backtrack(i+1,curr)
            curr.pop()
    res = []
    backtrack()
    return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = combine(4,2)
    print(res)