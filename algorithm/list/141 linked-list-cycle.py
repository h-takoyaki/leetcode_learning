class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 利用快慢指针确定是否存在环
        # 遍历改变节点的值
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


def main():
    head = [3, 2, 0, -4]
    pos = 1
    start = frontNode = ListNode(head[0])
    for i, num in enumerate(head[1:]):
        tempNode = ListNode(num)
        frontNode.next = tempNode
        frontNode = frontNode.next

    cycleNode = start

    for i in range(pos):
        cycleNode = cycleNode.next
    if pos:
        frontNode.next = cycleNode

    a = Solution()
    print(a.hasCycle(start))


if __name__ == '__main__':
    main()