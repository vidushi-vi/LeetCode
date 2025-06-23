# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ListNode=head
        count=0
        while ListNode is not None:
            count+=1
            ListNode=ListNode.next
        mid=count//2+1
        ListNode=head

        while ListNode is not None:
            mid=mid-1
            if mid==0:
                break
            ListNode=ListNode.next
        return ListNode