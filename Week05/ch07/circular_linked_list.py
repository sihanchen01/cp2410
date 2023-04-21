class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, data) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            node = self.head
            while node.next != self.head:
                node = node.next
            node.next = new_node
            new_node.next = self.head
            self.head = new_node

    def pop(self) -> Node | None:
        if self.is_empty():
            return None
        data = self.head.data
        if self.head.next == self.head:
            self.head = None
        else:
            node = self.head
            while node.next != self.head:
                node = node.next
            node.next = self.head.next
            self.head = self.head.next
        return data

    def traverse(self) -> None:
        if self.is_empty():
            print("List is empty")
        else:
            node = self.head
            while True:
                print(node.data, end=" ")
                node = node.next
                if node == self.head:
                    break
            print()

    def count_nodes(self) -> int:
        """ Return number of nodes inside circular linked list. """
        if self.head == None:
            return 0

        count = 1
        current = self.head
        while current.next != self.head:
            current = current.next
            count += 1
        return count
