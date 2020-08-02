# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
#  示例 1:
#
#  输入: 2.00000, 10
# 输出: 1024.00000
#
#
#  示例 2:
#
#  输入: 2.10000, 3
# 输出: 9.26100
#
#
#  示例 3:
#
#  输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25
#
#  说明:
#
#
#  -100.0 < x < 100.0
#  n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
#
#  Related Topics 数学 二分查找
#  👍 453 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
#1、暴力法 o(n)的复杂度并不好
    # res=x*n

# leetcode submit region end(Prohibit modification and deletion)

#分治模板：
# 1、terminator
# 2、process （split your big problem）
# 3、drill down merge
# 4、reverse states
def myPow( x,  n) :

    #  drill down
    def pow(n):
        #terminator
        if n == 0:
            return 1
        # process current logic and drill down
        # // 两数相除向下取整
        subres = pow( n // 2)
        if n % 2 ==1:
            return  subres * subres * x
        else:
            return subres * subres
    # 临界条件
    return pow(n) if n >=0 else 1.0/pow(-n)


if __name__ == '__main__':
    res=myPow(34.00515,-3)
    print(res)