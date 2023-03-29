#!/usr/bin/python3
"""
Module: 100-singly_linked_list
defines two classes, Node and SinglyLinkedList
"""


class Node:
    """
    definition of the class Node
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

        """
        gets the property attribute, data
        """
        @property
        def data(self):
            return self.__data

        """
        sets the property attribute for data
        """
        @data.setter
        def data(self, value):
            if type(value) != int:
                raise TypeError("data must be an integer")
            self.__data = value

        """
        gets the property attribute for next_node
        """
        @property
        def next_node(self):
            return self.__next_node

        """
        sets the property attribute for next_node
        """
        @next_node.setter
        def next_node(self, value):
            if value is not None and type(value) is not Node():
                raise TypeError("next_node must be a Node object")
            self.__next_node = value


class SinglyLinkedList:
    """
    the class definition
    """
    def __init__(self):
        self.__head = None

    """
    returns the nodes in the specified format
    """
    def __str__(self):
        value = ""
        current = self.__head
        while current is not None:
            value += (str(current.data))
            current = current.next_node
            if current is not None:
                value += "\n"
        return value

    """
    sorts the node while inserting new element
    """
    def sorted_insert(self, value):
        newnode = Node(value)
        if self.__head is None:
            self.__head = newnode
            return
        elif self.__head.data >= value:
            newnode.next_node = self.__head
            self.__head = newnode
            return
        else:
            current = self.__head
            while current.next_node is not None\
                    and current.next_node.data < value:
                current = current.next_node
            newnode.next_node = current.next_node
            current.next_node = newnode
            return
