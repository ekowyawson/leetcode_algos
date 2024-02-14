# Reversed Linked List

## Given the head of a singly linked list, reverse the list, and return the reversed list

To reverse a singly linked list, you need to change the direction of the pointers between the nodes so that each node points to its previous node instead of its next one. Since the list is singly linked, you don't have a built-in way to navigate backwards. The general strategy is to iterate through the list once, while keeping track of the current node's previous node so you can reverse the link. Here is a step-by-step guide to implement this in Python:

1. **Initialize three pointers:** Previous (`prev`), Current (`curr`), and Next (`next`). Initially, `prev` is set to `None` because the new tail of the list (which was the head of the original list) will point to `None`. `curr` is set to the head of the list.

2. **Iterate through the list:** For each node in the list, temporarily store the next node, reverse the current node's pointer to point to the previous node, update `prev` to be the current node, and move `curr` to the next node in the original list.

3. **Update head of the list:** Once you reach the end of the list (when `curr` is `None`), you know that `prev` is the new head of the reversed list. Return `prev`.

Here's how the code looks in Python:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next  # temporarily store the next node
        curr.next = prev  # reverse the current node's pointer
        prev = curr  # move the previous node forward
        curr = next_temp  # move to the next node in the list
    return prev  # `prev` is the new head of the reversed list
```

This function takes the head of a singly linked list and returns the head of the list after reversing it. The time complexity is O(n), where n is the number of nodes in the list, since we traverse the list once. The space complexity is O(1), as we only use a fixed amount of extra space.
