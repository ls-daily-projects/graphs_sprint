import sys
import os
from time import time
from player import Player
from world import World

from sample_graphs import hallway, cross, fish, trident_fish, five_hundy
from room_graph import RoomGraph

from traversal_test import test_traversal


def create_world_from_graph(graph):
    world = World()
    world.loadGraph(graph)
    world.printRooms()
    return world


def create_player_in_world(player_name, world):
    return Player(player_name, world.startingRoom)


def create_room_graph(graph_data):
    room_graph = RoomGraph()

    for room_1_id, data in graph_data.items():
        coordinates, edges = data
        room_graph.add_room(room_1_id)

        for direction, neighbor_id in edges.items():
            room_graph.add_room_neighbor(room_1_id, neighbor_id, direction)

    return room_graph


def get_last_shortest_move_count(filename="last_shortest_path.txt"):
    max_moves = 1000
    with open(filename, "r") as f:
        max_moves = int(f.readline())
    return max_moves


def print_shortest_move_count(path, elapsed_time):
    print(f"{len(path)} moves in {elapsed_time}s")


def record_shortest_move_count(path, elapsed_time, filename="last_shortest_path.txt"):
    with open(filename, "w") as f:
        f.write(f"{len(path)}\n")


def record_shortest_path(path, elapsed_time, filename="shortest_path.md"):
    with open(filename, "w") as f:
        f.write("# Graph Traversal Sprint\n\n")
        f.write("| # of Moves | Search Time (in seconds) \n")
        f.write("|:--:|:--:|\n")
        f.write(f"| {len(path)} | {elapsed_time}s |\n")
        f.write("## Traversal Path Sequence\n")
        f.write("```python3\n[\n")
        f.write(",".join(path))
        f.write("\n]\n```")


def find_shorter_move_count(room_graph, last_shortest_path_count, callbacks=[]):
    path = []
    shortest_path_count = last_shortest_path_count
    t1 = time()
    while shortest_path_count >= last_shortest_path_count:
        path = room_graph.traverse_rooms_df()
        new_count = len(path)

        if new_count < shortest_path_count:
            shortest_path_count = new_count
            t2 = time()
            for cb in callbacks:
                cb(path, round(t2 - t1, 4))

    t3 = time()
    for cb in callbacks:
        cb(path, round(t3 - t1, 4))
    return path

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")


if __name__ == '__main__':
    selected_graph = five_hundy
    world = create_world_from_graph(selected_graph)
    player = create_player_in_world("Mikis", world)
    room_graph = create_room_graph(selected_graph)
    shortest_move_count = get_last_shortest_move_count()
    path = find_shorter_move_count(
        room_graph, shortest_move_count, [record_shortest_move_count, record_shortest_path, print_shortest_move_count])

    test_traversal(world, player, selected_graph, path)
