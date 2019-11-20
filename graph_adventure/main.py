from player import Player
from world import World

from sample_graphs import hallway, cross, fish, trident_fish, five_hundy
from room_graph import RoomGraph

from traversal_test import test_traversal


# Load world
world = World()
selected_graph = five_hundy

world.loadGraph(selected_graph)
world.printRooms()
player = Player("Name", world.startingRoom)

# Build room graph
room_graph = RoomGraph()

for room_1_id, data in selected_graph.items():
    coordinates, edges = data
    room_graph.add_room(room_1_id)

    for direction, neighbor_id in edges.items():
        room_graph.add_room_neighbor(room_1_id, neighbor_id, direction)

traversal_path = room_graph.traverse_rooms_df()
shortest_path = len(traversal_path)

while shortest_path > 960:
    traversal_path = room_graph.traverse_rooms_df()

    if len(traversal_path) < shortest_path:
        shortest_path = len(traversal_path)
        print(shortest_path)


# print(f"Traversal Path:\n----{traversal_path}")
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
