# Linked List Cycle

> Given head, the head of a linked list, determine if the linked list has a cycle in it.

To determine if a linked list has a cycle, you can use Floyd's Tortoise and Hare algorithm. This algorithm uses two pointers, one moving at twice the speed of the other. If there is a cycle in the list, the faster-moving pointer (the "hare") will eventually meet the slower-moving pointer (the "tortoise") within the cycle.

Here's how you can implement this algorithm in Python:

1. Initialize two pointers, `slow` and `fast`, at the head of the linked list.
2. Move `slow` pointer by one step and `fast` pointer by two steps in each iteration of a loop.
3. If the linked list has a cycle, the `fast` pointer will eventually meet the `slow` pointer, indicating a cycle.
4. If the `fast` pointer reaches the end of the list (`None`), the list does not have a cycle.

Here is the implementation:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if not head:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next         # Move slow pointer by one step
        fast = fast.next.next    # Move fast pointer by two steps
        
        if slow == fast:         # A cycle is detected
            return True
    
    return False  # No cycle found
```

This function returns `True` if there is a cycle in the linked list and `False` otherwise. The key insight behind this algorithm is that if there is a cycle, the `fast` pointer, which moves at double the speed of the `slow` pointer, will "lap" the `slow` pointer at some point inside the cycle, allowing us to detect the cycle's presence. If there's no cycle, the `fast` pointer will reach the end of the list (`None`), and the loop will terminate without the two pointers meeting.
