class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Adds a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """Adds a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        """Prints all the elements of the list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
    
    def reverse_list(self):
        """Reverses the list by changing the links between the nodes."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        """Initiates merge sort on the list."""
        if self.head is None or self.head.next is None:
            return
        
        self.head = self.merge_sort_recursive(self.head)
    
    def merge_sort_recursive(self, h):
        """Recursively sorts the list using merge sort."""
        if h is None or h.next is None:
            return h
        
        middle = self.get_middle(h)
        next_to_middle = middle.next
        middle.next = None
        
        left = self.merge_sort_recursive(h)
        right = self.merge_sort_recursive(next_to_middle)
        
        sorted_list = self.sorted_merge(left, right)
        return sorted_list
    
    def get_middle(self, head):
        """Finds the middle of the list for splitting."""
        if head is None:
            return head
        
        slow = head
        fast = head
        
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def sorted_merge(self, a, b):
        """Merges two sorted lists into one."""
        if a is None:
            return b
        if b is None:
            return a
        
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        
        return result

def merge_sorted_lists(list1, list2):
    """Merges two sorted linked lists into one sorted list."""
    merged_list = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data < current2.data:
            merged_list.append(current1.data)
            current1 = current1.next
        else:
            merged_list.append(current2.data)
            current2 = current2.next

    # Append the remaining elements of one of the lists
    while current1:
        merged_list.append(current1.data)
        current1 = current1.next

    while current2:
        merged_list.append(current2.data)
        current2 = current2.next

    return merged_list
    

# Example usage:
# Create two lists
list1 = LinkedList()
list2 = LinkedList()

# Add elements to both lists
list1.append(1)
list1.append(3)
list1.append(5)

list2.append(2)
list2.append(4)
list2.append(6)

print("List 1:")
list1.print_list()

print("List 2:")
list2.print_list()

# Reverse list 1
print("\nReversed List 1:")
list1.reverse_list()
list1.print_list()

# Sort list 1 using merge sort
print("\nSorted List 1 after merge_sort:")
list1.merge_sort()
list1.print_list()

# Merge both lists
merged_list = merge_sorted_lists(list1, list2)
print("\nMerged sorted list:")
merged_list.print_list()


