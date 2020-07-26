# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
#
#
#  示例 1:
#
#  输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
#
#  示例 2:
#
#  输入: nums = [1], k = 1
# 输出: [1]
#
#
#
#  提示：
#
#
#  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
#  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
#  你可以按任意顺序返回答案。
#
#  Related Topics 堆 哈希表
#  👍 403 👎 0
import heapq
from collections import Counter
# leetcode submit region begin(Prohibit modification and deletion)

# counter 实现：count函数
def count(list):
    count_dict=dict()
    for item in list:
        if item in count_dict:
            count_dict[item] +=1
        else:
            count_dict[item] = 1
    return count_dict

def topKFrequent(nums, k) :
# leetcode submit region end(Prohibit modification and deletion)
# 建立hashmap
    nums = Counter(nums)
#建立堆
    return heapq.nlargest(k, nums.keys(),key=nums.get)




if __name__ == '__main__':
    nums = [1,1,1,1,2,2,3,4,4,4,4,4]
    res = topKFrequent(nums,2)
    print(res)
