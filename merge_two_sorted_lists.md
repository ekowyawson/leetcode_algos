# Merge Two Sorted Lists

## You are given the heads of two sorted linked lists list1 and list2

> Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists

Merging two sorted linked lists involves combining the nodes of the two lists into a single list that preserves the sorted order. The algorithm essentially involves iterating through both lists simultaneously, comparing their nodes, and attaching the node with the smaller value to the merged list. Here's a step-by-step explanation of how to achieve this:

### Step 1: Create a Dummy Head and a Current Pointer

- **Dummy Head:** This is a temporary node that serves as the starting point of the new list. It simplifies edge cases, such as initializing the new list. The merged list will actually start from `dummy_head.next`.
- **Current Pointer:** This pointer will be used to add nodes to the new list. Initially, it points to the dummy head.

### Step 2: Iterate Through Both Lists

- As long as neither `list1` nor `list2` is exhausted (i.e., neither is pointing to `None`), compare the values of the current nodes of `list1` and `list2`.
- Attach the node with the smaller value to the node pointed to by the current pointer.
- Move the current pointer to the node you just added to the merged list.
- Advance `list1` or `list2` (whichever had the smaller node) to the next node in their list.

### Step 3: Handle Remaining Nodes

- After the loop, at least one of the lists will be exhausted. If any nodes remain in either list, attach the remainder of that list to the merged list. There's no need to continue comparisons because both lists are sorted; the remaining elements of the non-exhausted list will all be greater than the last element added to the merged list.

### Step 4: Return the Merged List

- The merged list starts from `dummy_head.next` because `dummy_head` is a temporary node used for simplification.

### Example Code in Python

Here's how you could implement this algorithm in Python:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Step 1: Create a dummy node and a current pointer
    dummy_head = ListNode(-1)
    current = dummy_head
    
    # Step 2: Iterate through both lists
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Step 3: Handle remaining nodes
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    # Step 4: Return the merged list
    return dummy_head.next
```

This function takes two sorted linked lists (`list1` and `list2`) and returns a new list that is the result of merging them. The algorithm ensures that the merged list is also sorted. The time complexity is O(n + m), where n and m are the lengths of `list1` and `list2`, respectively, since it iterates through each list at most once. The space complexity is O(1), as it only uses a fixed amount of extra space (excluding the output list, which is necessary for the operation).

## What is the following line doing in the code above

```python
dummy_head = ListNode(-1)
```

The line `dummy_head = ListNode(-1)` in the code creates a temporary "dummy" head node for the merged linked list. This node serves several important purposes in the context of merging two sorted linked lists:

1. **Simplifies Edge Cases:** By starting with a dummy head, you avoid having to write separate logic for the edge case of initializing the head of the merged list. Without a dummy head, you would need additional code to handle the first comparison and set the head of the merged list, which complicates the implementation.

2. **Acts as a Placeholder:** The dummy head acts as a stable starting point for the merged list. Since the actual head of the merged list cannot be determined until the first comparison between the heads of the two lists (`list1` and `list2`) is made, the dummy head provides a reference point that precedes the real head of the merged list.

3. **Facilitates Iteration:** As the algorithm progresses, nodes from `list1` and `list2` are compared and appended to the end of the merged list. The dummy head provides an anchor from which the "current" pointer (which is used to add nodes to the merged list) can start. This way, you can always add the next node to `current.next`, and then advance `current` to `current.next`.

4. **Extracting the Merged List:** After the merge operation is complete, the merged list can be easily obtained by skipping over the dummy head and returning `dummy_head.next`. This is the actual head of the merged list. The value `-1` is arbitrary and does not have a specific meaning in the context of the merge operation; it's just a placeholder value. The key is that the dummy node itself is not part of the final merged list—it's just a tool used for the convenience of implementation.

By using a dummy head, the code becomes cleaner, easier to understand, and less prone to errors related to edge cases, especially those involving an initially empty merged list.
