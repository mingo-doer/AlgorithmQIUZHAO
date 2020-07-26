# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
#  示例:
#
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#  Related Topics 回溯算法
#  👍 802 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

def permute(nums) :
    res = []
    n = len(nums)
# leetcode submit region end(Prohibit modification and deletion)
    def backtrack(first = 0):
        if first == n:
            res.append(nums[:])
        for i in range(first,n):
            nums[first],nums[i] = nums[i], nums[first]
            backtrack(first+1)
            nums[first], nums[i] = nums[i], nums[first]

    backtrack()
    return res
if __name__ == '__main__':
    nums = [1,2,3]
    res = permute(nums)
    print(res)
