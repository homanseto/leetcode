# merge two Sorted lists with linked lists
# know more about your data
# know more about what your code do 

# linked list vs array 
# https://medium.com/@alejandro.itoaramendia/arrays-vs-linked-lists-a-complete-guide-bc23c0ab0e7c
# https://blog.algomaster.io/p/linked-list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val    # The data (e.g., 5, "A", etc.)
        self.next = next  # Pointer to the next node

    def getNext(self):
        return self.next
    
    def setNext(self, next_node):
        self.next = next_node

# insert_after
# Before: A -> B -> C
# Step 1: Create new_node (X) > (X (new_node) -> None)
# Step 2: new_node.next = node.next (B) > (X -> B -> C)
# Step 3: node.next = new_node (X) > (A -> X -> B -> C)
# After:  A -> X -> B -> C

def insert_after(node, new_val):
    new_node = ListNode(new_val)  # Create new node with value X. This creates a new node with val = X and next = None.
    new_node.next = node.next     # Point new_node to B (node.next is B). node.next is B, so now new_node.next points to B.
    node.next = new_node          # Point A to new_node (X). Now A points to X, and X points to B.


# Deletion
# Before: A -> B -> C
# Delete B: - current starts at A, - current.next is B (val matches), - Set A.next = B.next (which is C)
# After deleting B: A -> C

def delete_node(head, val):
    if head.val == val:
        return head.next  # Delete head
    current = head
    while current and current.next:  # Traverse until the second-to-last node
        if current.next.val == val:
            # Found the node to delete (current.next)
            current.next = current.next.next  # Skip the node to delete
            break
        current = current.next # Move to the next node
    # Return the (possibly unchanged) head
    return head

def delete_node_at_index(head, index):
    if index == 0:
        return head.next  # Delete the head

    current = head
    for _ in range(index - 1):  # Move to the node before the target
        if not current.next:
            return head  # Index out of bounds, return original list
        current = current.next

    if not current.next:
        return head  # Index out of bounds, return original list

    # Skip the node at the target index
    current.next = current.next.next
    return head

def delete_nth_occurrence(head, val, n):
    count = 0
    current = head

    # Handle deletion of the head
    if head and head.val == val:
        count += 1
        if count == n:
            return head.next

    # Traverse the list
    while current and current.next:
        if current.next.val == val:
            count += 1
            if count == n:
                current.next = current.next.next  # Delete the nth occurrence. Pay attention to if the current.next.next is null
                break
        current = current.next

    return head


# Reversal 






