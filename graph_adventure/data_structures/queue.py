class QueueNode():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class Queue():

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        output = []
        current_node = self.first

        if not current_node:
            return "[]"

        while current_node:
            output.append(current_node)
            current_node = current_node.next

        return ", ".join([str(node) for node in output])

    def __len__(self):
        return self.length

    @property
    def is_empty(self):
        return self.length == 0

    def enqueue(self, value):
        new_node = QueueNode(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node
            self.length += 1
            return self

        previous_last = self.last
        previous_last.next = new_node
        self.last = new_node
        self.length += 1
        return self

    def dequeue(self):
        if self.length == 0:
            return None

        previous_first = self.first
        self.first = previous_first.next
        self.length -= 1
        return previous_first

    def peek(self):
        return self.first

    def clear(self):
        self.first = None
        self.last = None
        self.length = 0
        return self
