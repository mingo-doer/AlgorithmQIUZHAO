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

#迭代
    # 把链表看做两部分 交换节点中前面的节点， 交换节点中后面的节点
    # 在完成交换，还得用prevNode记录A的前驱节点 防止链表断裂
def swapPairs(head) :
# leetcode submit region end(Prohibit modification and deletion)
    thead=ListNode(-1)
    thead.next=head
    prev_Node=thead
    while head and head.next :
        #准备节点
        first_Node=head
        second_Node=head.next
        #交换
        #prevnode 记录前驱节点
        prev_Node.next=second_Node
        first_Node.next=second_Node.next
        second_Node.next=first_Node
        #重初始化 头节点 和前驱节点为了下一次的交换
        prev_Node = first_Node
        head = first_Node.next

    return thead.next

#递归
    # 从链表的头节点head开始递归
    # 每次递归交换一对节点 交换firstNode 和 secondNode 表示要交换的节点
    # 下一次递归则是传递的下一对需要交换的节点 若链表中还有节点 则继续递归
    # 交换两个节点以后 返回secondNode 因为是交换后的表头
    # 在完成所有节点交换后 我们返回交换后的头 实际上原始链表的第二个节点

def swapPair_recursion(head):
    #如果链表为空或者链表只有一个节点
    if not head or not head.next :
        return head
    #设置变量
    first_Node = head
    second_Node = head.next

    #交换
    first_Node.next = swapPair_recursion(second_Node.next)
    second_Node.next = first_Node
    #头节点是第二个节点
    return second_Node








