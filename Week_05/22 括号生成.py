# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
#  示例：
#
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#
#  Related Topics 字符串 回溯算法
#  👍 1234 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 第二遍刷题
        result = []
        left , right = 0 , 0
        s = ""
        def generate(left,right,n,s):
            # terminator
            if (left == n and right == n ):
                result.append(s)
                return
            # process logic
            s1 = s + "("
            s2 = s + ")"
            # drill down
            if left < n :
                generate(left + 1 ,right ,n, s1)
            if right < left:
                generate(left  ,right + 1 ,n, s2)
            # reverse
        generate(left, right , n ,"")
        return result
# leetcode submit region end(Prohibit modification and deletion)
