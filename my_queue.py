from node import Node


class MyQueue:

    def __init__(self) -> None:
        self.first = None
        self.last = None

    def enqueue(self, value) -> None:
        # self.first может ссылаться на None только если очередь пуста(ещё не добавлен 1й элемент
        # или отданы все элементы)
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            self.last.next_node = Node(value)
            self.last = self.last.next_node

    def dequeue(self) -> Node:
        if self.first is not None:
            result = self.first
            self.first = self.first.next_node
            return result
        else:
            raise Exception

    def empty(self) -> bool:
        return self.first is None
