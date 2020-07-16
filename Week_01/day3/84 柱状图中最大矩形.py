# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
#
#
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
#
#
#
#
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
#
#
#  示例:
#
#  输入: [2,1,5,6,2,3]
# 输出: 10
#  Related Topics 栈 数组
#  👍 795 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

def largestRectangleArea_force(heights) :
# leetcode submit region end(Prohibit modification and deletion)

# 方法一：双层遍历左右两个边界 比较面积 面积=（右端点-左端点+1）*最小的高度
#最小的高度可以在遍历的时候顺便求出
    res=0
    l,r = 0 , len(heights)
    for i in range(r):
        #遍历高度
        height=heights[i]
        for j in range(i,r):
            #遍历右高度，顺便记住最小的高度
            height=min(height,heights[j])
            res=max(res,(r-l+1)*height)
    return res
#方法二
#从中间向两边拓展  找出其左边第一个高度小于它的索引p，再找到右边第一个高度小于的索引q
#面积=(q-r+1)*heights[i]
#问题转化成 max(f(0), f(1), f(2), ..., f(n - 1))

#方法三 单调栈
#以B点为高的矩形最大宽度为 从a到c 其中 ac 分别为B的左边和右边第一个小于B的元素
#维护一个单调栈 当遇见大数的时候 压入堆栈 等待之后处理
#遇见小数的时候，意味着大数的右边界已经确定了。
#这时候可以pop  右边界 就是当前的小数  左边界是堆栈下一层元素a
#面积=(c-a+1)*pop() pop()==b
def largestRectangleArea(heights):
    stack=[-1]
    max_res=0
    for i in range(len(heights)):
        #判断stack栈顶元素序列 i所记录的一定是下标
        while len(stack)>1 and heights[i]<=heights[stack[-1]]:
            max_res=max(max_res,heights[stack.pop()]*(i - stack[-1] -1))
        stack.append(i)
    for i in range(len(stack)-1):
        #环结束，要清理堆栈。此时所有栈中继续存放的元素的右边界c都是结尾len(height)-1
        max_res=max(max_res,heights[stack.pop()]*(len(heights) -1 -stack[-1]))
    return max_res




if __name__ == '__main__':
    list = [-1, 0]
    heights=[2,1,5,6,2,3]
    print(list[-1])
    print(heights[list[-1]])
    res=largestRectangleArea(heights)
    print(res)