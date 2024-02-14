from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self) -> str:
        # Adjusted to handle cycles: stops printing if a cycle is detected to prevent infinite loops
        nodes = []
        current = self
        seen = set() # To track visited nodes
        while current and current not in seen:
            nodes.append(str(current.val))
            seen.add(current)
            current = current.next
        if current: # If we stopped because of a cycle
            nodes.append("Cycle detected starting at " + str(current.val))
        return " -> ".join(nodes)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        # 2-pointer system using the Tortoise and Hare algorithm
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

def main():
    # Creating and linking the list nodes
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(6)
    head.next.next.next.next = ListNode(7)
    head.next.next.next.next.next = ListNode(9)

    # Creating a cycle in the list for testing
    # Linking the last node to the node with value 5 to create a cycle
    head.next.next.next.next.next.next = head.next.next

    # Applying the Solution to check for a cycle
    sol = Solution()
    has_cycle = sol.hasCycle(head)
    print("Does the linked list have a cycle?", has_cycle)

    # Note: Printing the list directly might lead to an infinite loop due to the cycle.
    # So it's commented out. Use the __str__ method cautiously with cycles.
    # print("Linked list:", head)

if __name__ == "__main__":
    main()
