class Room():
    def __init__(self, id, neighbor_data):
        self.id = id
        self.edges = {}

        for index, value in enumerate(neighbor_data):
            if value == 0:
                continue
            self.edges[value] = index

    def __str__(self):
        output = "******* Printing Room *******\n"
        output += f"Room {self.id}\n"
        output += "  Exits:\n  ---- "
        output += ", ".join(self.exits) + "\n"
        output += "  Neighbors:\n  ---- "
        output += ", ".join([str(id) for id in self.neighbors]) + "\n"
        return output

    @property
    def exits(self):
        return [exit for exit in self.edges.keys()]

    @property
    def neighbors(self):
        return [neighbor_id for neighbor_id in self.edges.values()]
