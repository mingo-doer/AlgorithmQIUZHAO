# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
#  你可以假设除了整数 0 之外，这个整数不会以零开头。
#
#  示例 1:
#
#  输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
#
#  示例 2:
#
#  输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#
#  Related Topics 数组
#  👍 502 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
#进位的问题
    # 不是9 直接返回
    # 是9 变0 首位加1
def plusOne(digits) :
# leetcode submit region end(Prohibit modification and deletion)

    if digits[-1] < 9:
        digits[-1] +=1
    elif len(digits) ==1 and digits[0] ==9:
        return [1, 0]
    else:
        digits[-1] = 0
        digits[0:-1] = plusOne(digits[0:-1])
    return digits

if __name__ == '__main__':
    res=plusOne([1,9])
    print(res)
