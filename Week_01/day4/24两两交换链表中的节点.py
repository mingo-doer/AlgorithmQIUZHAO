# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
#  示例:
#
#  给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#  Related Topics 链表
#  👍 549 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head) :
# leetcode submit region end(Prohibit modification and deletion)
    thead=ListNode(-1)
    thead.next=head
    c=thead
    while c.next and c.next.next :
        a,b = c.next , c.next.next
        c.next , a.next = b , b.next
        b.next = a
        c = c.next.next
    return thead.next





