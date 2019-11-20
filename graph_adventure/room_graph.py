from enum import Enum
import random


class ExitDirection(Enum):
    north = "n"
    south = "s"
    east = "e"
    west = "w"


class RoomGraph():
    def __init__(self):
        self.rooms = {}
        self.reverse_direction = {
            "n": "s",
            "s": "n",
            "e": "w",
            "w": "e"
        }

    @property
    def size(self):
        return len(self.rooms)

    def __str__(self):
        output = ""

        for room_1, neighbors in self.rooms.items():
            output += f"Room {room_1} has:\n"
            for neighbor_id, direction in neighbors:
                output += f"  Room {neighbor_id} to the {direction.name}\n"

        return output

    def add_room(self, room_id):
        if self.rooms.get(room_id):
            return self

        self.rooms[room_id] = set()

        return self

    def add_room_neighbor(self, from_room_id, to_room_id, to_direction):
        self.add_room(from_room_id)
        self.add_room(to_room_id)
        self.rooms[from_room_id].add((to_room_id, ExitDirection(to_direction)))
        return self

    def get_valid_neighbors(self, room_id, visited=set()):
        neighbors = self.rooms[room_id]
        return [(neighbor, direction) for neighbor,
                direction in neighbors if neighbor not in visited]

    def get_reverse_direction(self, direction):
        return ExitDirection(self.reverse_direction[direction.value])

    def traverse_rooms_df(self):
        visited = set()
        directions = []
        stack = [(0, None)]
        current_room = 0

        visited.add(current_room)

        while len(visited) < self.size:
            valid_neighbors = self.get_valid_neighbors(current_room, visited)

            if valid_neighbors:
                random_neighbor, random_direction = random.choice(
                    valid_neighbors)
                stack.append((current_room, random_direction))
                current_room = random_neighbor
                # print(current_room, random_direction.value)
                directions.append(random_direction.value)
                visited.add(current_room)
            elif stack:
                room, direction = stack.pop()
                current_room = room
                # print(current_room, self.get_reverse_direction(direction).value)
                directions.append(self.get_reverse_direction(direction).value)

        return directions
