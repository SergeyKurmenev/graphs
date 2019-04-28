class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next_node = None

    def __str__(self):
        return '{}'.format(self.value)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return False
