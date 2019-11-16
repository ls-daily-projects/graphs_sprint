from data_structures import Stack, Queue
from .room import Room


class RoomGraph():
    DIRECTIONS = {
        "n": "s",
        "s": "n",
        "e": "w",
        "w": "e"
    }

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

        while not room_stack.is_empty:
            current_room = room_stack.pop().value

            if current_room.id not in visited:
                output.append(current_room.id)
                cb(current_room)
                visited.add(current_room.id)

                for neighbor_id in current_room.neighbors:
                    room_stack.push(self.get_room_with_id(neighbor_id))
        return output

    def traverse_backtracking_depth_first(self, starting_room=0, cb=print):
        output = []
        room_stack = Stack()
        visited = set()

        room_stack.push((self.get_room_with_id(starting_room), None))

        while not room_stack.is_empty:
            current_room, parent = room_stack.pop().value

            if current_room.id not in visited:
                visited.add(current_room.id)
                cb(current_room)
                output.append(
                    (current_room.id, parent.id if parent is not None else None))

                for neighbor_id in current_room.neighbors:
                    neighbor = self.get_room_with_id(neighbor_id)
                    room_stack.push((neighbor, current_room))

        return output

    def rooms_to_paths(self, room_paths):
        print(room_paths)

        def path_from_room_id_pair(room_1_pair, room_2_pair):
            path = []
            room_1_id, room_1_parent_id = room_1_pair
            room_2_id, room_2_parent_id = room_2_pair
            room_1 = self.get_room_with_id(room_1_id)
            room_1_parent = self.get_room_with_id(room_1_parent_id)
            room_2 = self.get_room_with_id(room_2_id)
            room_2_parent = self.get_room_with_id(room_2_parent_id)

            can_move_forward = room_1.direction_for_room_id(room_2_id)

            if not can_move_forward:
                can_move_backward = room_1.direction_for_room_id(room_1_parent)
                if can_move_backward:
                    path += [can_move_backward]
                return path

            return path
        return []

    def traverse_breadth_first(self, starting_room=0, cb=print):
        output = []
        room_queue = Queue()
        visited = set()

        room_queue.enqueue(self.get_room_with_id(starting_room))

        while not room_queue.is_empty:
            current_room = room_queue.dequeue().value

            if current_room.id not in visited:
                output.append(current_room.id)
                cb(current_room)
                visited.add(current_room.id)

                for neighbor_id in current_room.neighbors:
                    room_queue.enqueue(self.get_room_with_id(neighbor_id))

        return output

    def traverse_breadth_first_shortest_path(self, starting_room=0, cb=print):
        output = []
        room_queue = Queue()
        visited = set()

        room_queue.enqueue((self.get_room_with_id(starting_room), None))

        while not room_queue.is_empty:
            current_room, parent_room = room_queue.dequeue().value

            for neighbor_id in current_room.neighbors:
                if neighbor_id in visited:
                    output.append(
                        (current_room.id, parent_room.id))
                    cb(current_room)
                    continue
                neighbor = self.get_room_with_id(neighbor_id)
                room_queue.enqueue((neighbor, current_room))
                visited.add(current_room.id)

        return output
