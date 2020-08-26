# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
#
#
#  示例：
#
#  s = "leetcode"
# 返回 0
#
# s = "loveleetcode"
# 返回 2
#
#
#
#
#  提示：你可以假定该字符串只包含小写字母。
#  Related Topics 哈希表 字符串
#  👍 254 👎 0
import collections

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 构建hashmap
        count = collections.Counter(s)
        # print(count)
        # 查找
        for idx , value in enumerate(s):
            # print(idx,value)
            if count[value] == 1:
                return idx
        return -1
# leetcode submit region end(Prohibit modification and deletion)
