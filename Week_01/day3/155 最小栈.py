# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
#
#  push(x) —— 将元素 x 推入栈中。
#  pop() —— 删除栈顶的元素。
#  top() —— 获取栈顶元素。
#  getMin() —— 检索栈中的最小元素。
#
#
#
#
#  示例:
#
#  输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# 输出：
# [null,null,null,null,-3,null,0,-2]
#
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#
#
#
#
#  提示：
#
#
#  pop、top 和 getMin 操作总是在 非空栈 上调用。
#
#  Related Topics 栈 设计
#  👍 603 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack:
#采取辅助栈的方式 这个栈同时保存x 和 最小值 这个元素是一个元组（当前值x，栈内最小值）
#这个元组是一个整体，同时进栈和出栈。即栈顶同时有值和栈内最小值，top()函数是获取栈顶的当前值，即栈顶元组的第一个值； getMin() 函数是获取栈内最小值，即栈顶元组的第二个值；pop() 函数时删除栈顶的元组。


    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]


    def push(self, x: int) :
        if not self.stack:
            self.stack.append((x,x))
        else:
            #保存x 和栈内最小值 是元组的第1个值
            self.stack.append((x,min(x,self.stack[-1][1])))


    def pop(self) :
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1][0]


    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == '__main__':

# Your MinStack object will be instantiated and called as such:
    x=[[],[-2],[0],[-3],[],[],[],[]]
    obj = MinStack()
    obj.push(x)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
