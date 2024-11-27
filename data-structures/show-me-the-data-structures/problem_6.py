from typing import Optional

class Node:
    """
    A class to represent a node in a linked list.

    Attributes:
    -----------
    value : int
        The value stored in the node.
    next : Optional[Node]
        The reference to the next node in the linked list.
    """

    def __init__(self, value: int) -> None:
        """
        Constructs all the necessary attributes for the Node object.

        Parameters:
        -----------
        value : int
            The value to be stored in the node.
        """
        self.value: int = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
        --------
        str
            A string representation of the node's value.
        """
        return str(self.value)


class LinkedList:
    """
    A class to represent a singly linked list.

    Attributes:
    -----------
    head : Optional[Node]
        The head node of the linked list.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the LinkedList object.
        """
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        """
        Return a string representation of the linked list.

        Returns:
        --------
        str
            A string representation of the linked list, with nodes separated by " -> ".
        """
        cur_head: Optional[Node] = self.head
        out_string: str = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value: int) -> None:
        """
        Append a new node with the given value to the end of the linked list.

        Parameters:
        -----------
        value : int
            The value to be stored in the new node.
        """
        if self.head is None:
            self.head = Node(value)
            return

        node: Node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self) -> int:
        """
        Calculate the size (number of nodes) of the linked list.

        Returns:
        --------
        int
            The number of nodes in the linked list.
        """
        size: int = 0
        node: Optional[Node] = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the union of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all unique elements from both input linked lists.
    """
    # Use a set to store all unique elements
    if llist_1 is None and llist_2 is None:
        return LinkedList()
    
    if llist_1.head is None:
        return llist_2
    
    if llist_2.head is None:
        return llist_1
    
    unique_elements = set()
    node_1 = llist_1.head
    while node_1:
        unique_elements.add(node_1.value)
        node_1 = node_1.next

    node_2 = llist_2.head
    while node_2:
        unique_elements.add(node_2.value)
        node_2 = node_2.next
    
    result_list =  LinkedList()
    node = result_list.head
    for element in unique_elements:
        if node is None:
            result_list.head = Node(element)
            node = result_list.head
        else:
            node.next = Node(element)
            node = node.next

    node.next = None
    return result_list

def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the intersection of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all elements that are present in both input linked lists.
    """
    # Use sets to find the intersection
    if llist_1 is None or llist_2 is None:
        return LinkedList()

    val_set_1 = set()
    node_1 = llist_1.head
    while node_1:
        val_set_1.add(node_1.value)
        node_1 = node_1.next

    val_set_2 = set()
    node_2 = llist_2.head
    while node_2:
        val_set_2.add(node_2.value)
        node_2 = node_2.next

    llist_result = LinkedList()
    node = llist_result.head

    # Find the intersection of both sets
    for val in val_set_1:
        if val in val_set_2:
            if node is None:
                llist_result.append(val)
                node = llist_result.head
            else:
                node.next = Node(val)
                node = node.next
    if node:
        node.next = None
    return llist_result


if __name__ == "__main__":
    ## Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    
    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Test Case 1:")
    print("Union:", union(linked_list_1, linked_list_2)) # Expected: 1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65
    print("Intersection:", intersection(linked_list_1, linked_list_2)) # Expected: 4, 6, 21

    ## Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("\nTest Case 2:")
    print("Union:", union(linked_list_3, linked_list_4)) # Expected: 1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65
    print("Intersection:", intersection(linked_list_3, linked_list_4)) # Expected: empty

    ## Test case 3: Edge case with empty linked lists
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()
    print("\nTest Case 3:")
    print("Union:", union(linked_list_5, linked_list_6)) # Expected: empty
    print("Intersection:", intersection(linked_list_5, linked_list_6)) # Expected: empty

    ## Test case 4: Edge case with one empty linked list
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()
    for i in element_1:
        linked_list_7.append(i)
    print("\nTest Case 4:")
    print("Union:", union(linked_list_7, linked_list_8)) # Expected: 2, 3, 4, 6, 23, 35, 65
    print("Intersection:", intersection(linked_list_7, linked_list_8)) # Expected: empty
    