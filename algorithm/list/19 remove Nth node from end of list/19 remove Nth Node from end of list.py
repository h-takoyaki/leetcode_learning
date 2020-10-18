import typing


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     dummy_node = ListNode(0)
    #     dummy_node.next = head
    #     slow = dummy_node
    #     fast = dummy_node
    #     for _ in range(n):
    #         fast = fast.next

    #     while fast.next:
    #         slow = slow.next
    #         fast = fast.next
    #     slow.next = slow.next.next
    #     return dummy_node.next
    


def main():
    head = [1, 2, 3, 4, 5]
    n = 2

    # Init the singly linked-list
    headNode = ListNode(val=head[0])
    r = headNode
    for i in range(1, len(head)):
        r.next = ListNode(val=head[i])
        r = r.next
    solution = Solution()
    new_head = solution.removeNthFromEnd(headNode, n)

    # print out result
    res = []
    while new_head:
        res.append(new_head.val)
        new_head = new_head.next

    print(res)


if __name__ == '__main__':
    main()
