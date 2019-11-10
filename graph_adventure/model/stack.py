class StackNode():
    def __init__(self, value):
        self.value = value
        self.previous = None

    def __str__(self):
        return str(self.value)


class Stack():
    def __init__(self):
        self.top = None
        self.last = None
        self.length = 0

    def __str__(self):
        output = [0] * self.length
        current_node = self.top

        if not current_node:
            return "[]"

        index = self.length - 1
        while current_node:
            output[index] = current_node
            current_node = current_node.previous
            index -= 1

        return ", ".join([str(node) for node in output])

    def __len__(self):
        return self.length

    @property
    def is_empty(self):
        return self.length == 0

    def push(self, value):
        new_node = StackNode(value)

        if self.length == 0:
            self.top = new_node
            self.last = new_node
            self.length += 1
            return self

        new_node.previous = self.top
        self.top = new_node
        self.length += 1

        return self

    def pop(self):
        if self.length == 0:
            return None

        old_top = self.top
        self.top = old_top.previous
        self.length -= 1

        return old_top

    def peek(self):
        return self.top

    def clear(self):
        self.top = None
        self.last = None
        self.length = 0
        return self
