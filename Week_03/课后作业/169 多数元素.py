# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
#  示例 1:
#
#  输入: [3,2,3]
# 输出: 3
#
#  示例 2:
#
#  输入: [2,2,1,1,1,2,2]
# 输出: 2
#
#  Related Topics 位运算 数组 分治算法
#  👍 677 👎 0

import collections
# leetcode submit region begin(Prohibit modification and deletion)
#出现的次数 频率 map
def counter (nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return count
def majorityElement(nums) :
# leetcode submit region end(Prohibit modification and deletion)
   count_nums=collections.Counter(nums)
   # print(count_nums)
   # for key in count_nums:
   #     if count_nums[key] > len(nums)/2:
   #          return key
   # return
# 优化写法：一定要学会对hash的key
   return max(count_nums.keys(),key=count_nums.get)

#排序 将nums排序 下标为num/2的一定是多数


if __name__ == '__main__':
    res = majorityElement([2,2,1,1,1,2,2])
    print(res)
