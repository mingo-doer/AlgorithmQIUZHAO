# 给定一个字符串，逐个翻转字符串中的每个单词。
#
#
#
#  示例 1：
#
#  输入: "the sky is blue"
# 输出: "blue is sky the"
#
#
#  示例 2：
#
#  输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#
#
#  示例 3：
#
#  输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#
#
#
#
#  说明：
#
#
#  无空格字符构成一个单词。
#  输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#  如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#
#
#
#
#  进阶：
#
#  请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。
#  Related Topics 字符串
#  👍 211 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords(self, s: str) -> str:
    #     # 方法一 利用内置函数
    #     return " ".join(reversed(s.split()))
    # # 方法二：
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] !=" " : i -= 1
            res.append(s[i+1:j+1])
            while s[i] == " ": i -= 1
            # 指向下个单词的尾
            j = i
        return " ".join(res)
# if __name__ == '__main__':
#     res = Solution().reverseWords(" Hello World! ")
#     print(res)





# leetcode submit region end(Prohibit modification and deletion)
