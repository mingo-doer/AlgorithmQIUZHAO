# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
#  说明：解集不能包含重复的子集。
#
#  示例:
#
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#  Related Topics 位运算 数组 回溯算法
#  👍 674 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 第一想法   找重复性  迭代
# extend 和append
def subsets(nums) :
# leetcode submit region end(Prohibit modification and deletion)
    subsets = [[]]
    for num in nums:
        newset = []
        for subset in subsets:
            # 会遍历结果列表 妙啊！
            new_subset = subset + [num]
            newset.append(new_subset)
        subsets.extend(newset)
    return subsets
#代码优化
def subsets2(nums):
    res = [[]]
    for i in nums:
        # 一定要学会这样的语法糖
        res = res+ [[i] + nums for nums in res ]
    return res

if __name__ == '__main__':
    res = subsets2([1,2,3])
    print(res)
