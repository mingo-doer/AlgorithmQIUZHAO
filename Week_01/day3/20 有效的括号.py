# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
#  有效字符串需满足：
#
#
#  左括号必须用相同类型的右括号闭合。
#  左括号必须以正确的顺序闭合。
#
#
#  注意空字符串可被认为是有效字符串。
#
#  示例 1:
#
#  输入: "()"
# 输出: true
#
#
#  示例 2:
#
#  输入: "()[]{}"
# 输出: true
#
#
#  示例 3:
#
#  输入: "(]"
# 输出: false
#
#
#  示例 4:
#
#  输入: "([)]"
# 输出: false
#
#
#  示例 5:
#
#  输入: "{[]}"
# 输出: true
#  Related Topics 栈 字符串
#  👍 1684 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
#暴力匹配法  时间复杂度较大
#考虑用栈
#将左括号 和右括号形成map
#  如果栈顶元素不能和左括号匹配，那么就是false
#  如果一致就将栈顶元素弹出
def isValid( s) :
# leetcode submit region end(Prohibit modification and deletion)
#如果为长度为奇数，直接为False
    if len(s) % 2 != 0:
        return False
    dic= {'{':'}',"[":']','(':')'}
    stack=[]
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
    if len(stack) == 0:
        return True
    return False

if __name__ == '__main__':
    s1="()[]{}"
    s2='(]'
    res=isValid(s2)
    print(res)