# 实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
#
#
#
#  示例 1：
#
#
# 输入: "Hello"
# 输出: "hello"
#
#  示例 2：
#
#
# 输入: "here"
# 输出: "here"
#
#  示例 3：
#
#
# 输入: "LOVELY"
# 输出: "lovely"
#
#  Related Topics 字符串
#  👍 131 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def toLowerCase(self, str: str) -> str:
        s = []
        for i in str:
            if i.islower():
                s.append(i)
            else:
                s.append(i.lower())
        return ''.join(s)
#'A' - 'Z' 对应的 ascii 是 65 - 90；
#'a' - 'z' 对应的 ascii 是 97 - 122；
# 分别相差32
# ord 转成ASCII码 chr转回
# 判断大小写还可以用
# if  65 <= ord(i) <= 90:
#     s.append(chr(ord(i) + 32))
# leetcode submit region end(Prohibit modification and deletion)