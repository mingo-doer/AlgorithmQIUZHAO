# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
#
#  返回滑动窗口中的最大值。
#
#
#
#  进阶：
#
#  你能在线性时间复杂度内解决此题吗？
#
#
#
#  示例:
#
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10^5 
#  -10^4 <= nums[i] <= 10^4
#  1 <= k <= nums.length
#
#  Related Topics 堆 Sliding Window
#  👍 459 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque


def maxSlidingWindow_force( nums, k) :

# leetcode submit region end(Prohibit modification and deletion)
    #暴力法
    # 最简单直接的方法 是遍历每个窗口，找到每个窗口的最大值 一共有N-K+1个滑动窗口，每个有K个元素，时间复杂度为o（NK）
    #超出时间限制
    n = len(nums)
    if n * k ==0:
        return []
#可优化
    res=[]
    for i in range(n-k+1):
       res.append(max(nums[i:i+k]))
    return res
    #上述for三行 可以变为一行  return [max(nums[i:i + k]) for i in range(n - k + 1)]

#双向队列
# 堆 最大堆中heap[0]永远是最大的元素，在大小为k的堆中插入操作是logk的时间复杂度，所以算法是nlogk的
# 算法步骤
#     处理前K个元素，初始化双向队列
#     遍历整个数组
#     清理双向队列
#         只保留当前滑动窗口元素的索引
#         移除比当前元素小的所有元素，它们不可能是最大的
#     将当前元素添加到双向队列
#     将deque[0]添加到输出
#     返回输出数组
def maxSlidingWindow(nums,k):
    n = len(nums)
    if n * k == 0:
        return []
    if k == 1 :
        return nums
    def clean_deque(i):
        #只保留当前元素窗口的索引
        if deq and deq[0] == i-k:
            deq.popleft()
        #移除比当前元素小的所有元素
        while deq and nums[i] > nums[deq[-1]]:
            deq.pop()
    #初始化队列和输出
    deq = deque()
    max_id = 0
    for i in range(k):
        clean_deque(i)
        deq.append(i)
        if nums[i] > nums[max_id]:
            max_id = i
    res = [nums[max_id]]

    for i in range(k,n):
        clean_deque(i)
        deq.append(i)
        res.append(nums[deq[0]])
    return res

if __name__ == '__main__':
    nums=[1,3,-1,-3,5,3,6,7]
    k=3
    res=maxSlidingWindow(nums,k)
    print(res)