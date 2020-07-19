# 反转一个单链表。
#
#  示例:
#
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
#  进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#  Related Topics 链表
#  👍 1096 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
# leetcode submit region end(Prohibit modification and deletion)
#循环的方法
#申请两个链表  一个空 一个完整 指向头
        pre = None
        curr = head
        while curr:
            #先将curr.next 保存在temp 防止链表丢失
            temp = curr.next
            #curr.next 指向前驱节点 pre
            curr.next = pre
            #pre 后移一位移到cur当前的位置
            pre = curr
            #cur也后移一位也就是temp的位置
            curr=temp
        return pre

    #递归的方法
    def reverseList_re(self,head):
        if head is None or head.next is None:
            return head
        newhead = self.reverseList_re(head.next)
        head.next.next = head
        head.next = None
        return newhead








