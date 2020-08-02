# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
#  示例:
#
#  输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
#  说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#  Related Topics 字符串 回溯算法
#  👍 806 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

def letterCombinations(digits) :
# leetcode submit region end(Prohibit modification and deletion)
#     利用hash 构造一个集合
    phone = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def backtrack(combination,next_digits):
#         terminatior
        if len(next_digits) == 0:
            output.append(combination)
#         process the logic
        else:
            for letter in phone[next_digits[0]]:
    #             drill down
                backtrack(combination+letter,next_digits[1:])
    output = []
    if digits:
        backtrack('',digits)
    return output

if __name__ == '__main__':
    res = letterCombinations('23')
    print(res)