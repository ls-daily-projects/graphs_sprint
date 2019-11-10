from room import Room
from player import Player
from world import World

from room_graphs import hallway, cross, fish, trident_fish, five_hundy
from model import RoomGraph

from traversal_test import test_traversal

import random

# Load world
world = World()
selected_graph = cross
traversal_path = []

room_graph = RoomGraph(selected_graph)
traversed_rooms = []


def print_room_ids(room):
    traversed_rooms.append(room.id)


print(room_graph.traverse_depth_first(cb=print_room_ids))

world.loadGraph(selected_graph)
world.printRooms()
player = Player("Name", world.startingRoom)


test_traversal(world, player, selected_graph, traversal_path)

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
