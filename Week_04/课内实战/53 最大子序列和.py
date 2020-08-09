# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
#  示例:
#
#  输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#
#  进阶:
#
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#  Related Topics 数组 分治算法 动态规划
#  👍 2271 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
# leetcode submit region end(Prohibit modification and deletion)
        # 最大子序列和等于 当前最大 或者包含之前的最大
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i]+nums[i-1])
            #这里的nums[i]是相邻序列的和
        # 返回最大的
        return max(nums)
