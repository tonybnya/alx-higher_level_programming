#!/usr/bin/python3
"""class Node that defines a node of a singly linked list."""


class Node:
    """Define a node."""
    def __init__(self, data, next_node=None):
        """
        Initialize attributes
        Args:
            data (int): the data in the node as an integer.
            next_node (Node): a pointer to the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Define a Singly Linked List."""
    def __init__(self):
        """
        Initialize attribute.
        Args:
            head (Node): a pointer to the head of the SLL
        """
        self.__head = None

    def __str__(self):
        """
        Print the entire Singly Linked List.
        One node number per line.
        """
        printer = ""
        tmp = self.__head
        while (tmp):
            printer += str(tmp.data) + "\n"
            tmp = tmp.next_node

        return (printer[:-1])

    def sorted_insert(self, value):
        new = Node(value)

        if not self.__head:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
