# 删除倒数第n个元素

[题目链接](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)

~~~txt
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。  
示例：  
给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
~~~

使用快慢指针（双指针）。快指针先于慢指针走n步，之后快慢指针一起向后走，当快指针走到末尾的时候，慢指针正好走到我们要处理的位置。  
如果用题目给定的例子表示就是，fastNode先走2步到达3，此时慢指针（1），快指针（3）一起向后走。即: 慢（1）快（3）->慢（2）快（4）->慢（3）快（5)。此时让慢指针指向快指针就跳过了倒数第n个指针（4）。

~~~python
# 有问题的代码
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
~~~

上面的代码能够很好的处理给出的例子，但是并没有考虑到头指针的问题，当head = [1],  n = 1, slow指针应该指向head指针前一个位置，所以这里可以引入哑指针（dummy Node）解决。哑指针指向头指针前一个位置，这样就解决了头指针没有前结点的问题。

~~~python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_node = ListNode(0)
        dummy_node.next = head
        slow, fast = dummy_node, dummy_node
        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy_node.next
~~~
