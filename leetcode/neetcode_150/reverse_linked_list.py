# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList_(self, head: Optional[ListNode]) -> ListNode: # input as list
        # empty head
        if len(head) <= 1:
            return head

        # first element in head
        first_node = ListNode(val = head[0], next=None)

        prev_node = first_node
        list_val = [first_node.val]

        # len(head) > 1
        if len(head) > 1:
            for i in range(1, len(head)):
                curr_node = ListNode(val = head[i], next=None)
                list_val.append(curr_node.val)
                prev_node.next = curr_node
                prev_node = curr_node
                
            # # traverse forward
            # next_node = first_node.next
            
            # while next_node != None:
            #     # print("Next: ", next_node.val)
            #     next_node = next_node.next

            # traverse reverse
            return list_val[::-1]
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # input as Listnode; only works on leetcode
        prev = None
        curr = head

        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt
        return prev




            


solved = Solution()
# print(solved.reverseList_(head = [1,2,3,4,5]))
# print(solved.reverseList_(head = [1,2]))
# print(solved.reverseList_(head = [-1]))
# print(solved.reverseList_(head = []))



