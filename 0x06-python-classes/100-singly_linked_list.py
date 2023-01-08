#1/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

    def __str__(self):
        return self.__data


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        dummy = self.__head
        if self.__head is None:
            new = Node(value)
            self.__head = new
        else:
            new = Node(value)
            while dummy.next_node() is not None:
                dummy = dummy.next_node()
            dummy.next_node(new)

    def display(self):
        temp = self.__head
        while temp:
            print(temp.__str__())
            temp = temp.next_node()
