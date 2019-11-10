from .room import Room
from .stack import Stack
from .queue import Queue


class RoomGraph():

    def __init__(self, room_data):
        self.size = len(room_data)
        self.adjacency_matrix = [
            [0 for _ in range(self.size)] for _ in range(self.size)]

        for room_1, values in room_data.items():
            for direction, room_2 in values[1].items():
                self.adjacency_matrix[room_1][room_2] = direction

    def __str__(self):
        output = "[\n  "

        output += "\n  ".join([", ".join([str(col) for col in row])
                               for row in self.adjacency_matrix])

        output += "\n]"
        return output

    def get_room_with_id(self, room_id):
        if not self.adjacency_matrix[room_id]:
            raise IndexError(f"Room with id {room_id} does not exist!")

        return Room(room_id, self.adjacency_matrix[room_id])

    def traverse_depth_first(self, starting_room=0, cb=print):
        output = []
        room_stack = Stack()
        visited = set()

        room_stack.push(self.get_room_with_id(starting_room))

        while len(room_stack) != 0:
            current_room = room_stack.pop().value

            if current_room.id not in visited:
                output.append(current_room.id)
                cb(current_room)
                visited.add(current_room.id)

                for neighbor_id in current_room.neighbors:
                    room_stack.push(self.get_room_with_id(neighbor_id))
        return output

    def traverse_breadth_first(self, starting_room=0, cb=print):
        output = []
        room_queue = Queue()
        visited = set()

        room_queue.enqueue(self.get_room_with_id(starting_room))

        while len(room_queue) != 0:
            current_room = room_queue.dequeue().value

            if current_room.id not in visited:
                output.append(current_room.id)
                cb(current_room)
                visited.add(current_room.id)

                for neighbor_id in current_room.neighbors:
                    room_queue.enqueue(self.get_room_with_id(neighbor_id))

        return output
