from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionBleh:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 and list2) and (list1.val <= list2.val):
            merged_res_head = list1
            cur_node = list1
            list1 = list1.next
        elif (list1 and list2) and (list1.val > list2.val):
            merged_res_head = list2
            cur_node = list2
            list2 = list2.next
        elif list1:
            merged_res_head = list1
            cur_node = list1
            list1 = list1.next
        elif list2:
            merged_res_head = list2
            cur_node = list2
            list2 = list2.next
        else:
            return None

        list1_node = list1
        list2_node = list2
        while list1_node and list2_node:
            if list1_node.val <= list2_node.val:
                cur_node.next = list1_node
                cur_node = list1_node
                list1_node = list1_node.next
            else:
                cur_node.next = list2_node
                cur_node = list2_node
                list2_node = list2_node.next

        while list1_node:
            cur_node.next = list1_node
            cur_node = list1_node
            list1_node = list1_node.next

        while list2_node:
            cur_node.next = list2_node
            cur_node = list2_node
            list2_node = list2_node.next

        return merged_res_head


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # technique when we have Node that comes before merged list
        dummy = ListNode()
        cur_node = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur_node.next = list1
                list1 = list1.next
            else:
                cur_node.next = list2
                list2 = list2.next
            cur_node = cur_node.next

        cur_node.next = list1 if list1 else list2
        return dummy.next

# also there's recursive solution but i don't care enough


list1 = None
list2 = ListNode(1)
n2 = ListNode(2)
list2.next = n2
print(Solution().mergeTwoLists(list1, list2))
