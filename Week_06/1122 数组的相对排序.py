# 给你两个数组，arr1 和 arr2，
#
#
#  arr2 中的元素各不相同
#  arr2 中的每个元素都出现在 arr1 中
#
#
#  对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末
# 尾。
#
#
#
#  示例：
#
#  输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
#
#
#
#
#  提示：
#
#
#  arr1.length, arr2.length <= 1000
#  0 <= arr1[i], arr2[i] <= 1000
#  arr2 中的元素 arr2[i] 各不相同
#  arr2 中的每个元素 arr2[i] 都出现在 arr1 中
#
#  Related Topics 排序 数组
#  👍 75 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 使用计数排序 0-1000 所以是 1001
        temp = [0 for _ in range(1001) ]
        res = []
        # 构建计数排序的 个数数组
        for i in arr1:
            temp[i] += 1
        for i in arr2:
            res += [i] * temp[i]
            temp[i] = 0
        # 剩下没有出现过的元素
        for i in range(len(temp)):
            res += [i] * temp[i]
        return res

# leetcode submit region end(Prohibit modification and deletion)
