# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        node_v=ListNode(0)
        node_v.next=head
        prev=node_v

        for i in range(left-1):
            prev=prev.next
        start=prev.next
        end=start.next

        for i in range(right-left):
            start.next=end.next
            end.next=prev.next
            prev.next=end
            end=start.next
        return node_v.next