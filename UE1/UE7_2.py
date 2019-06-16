from adt_graph import Graph
import csv


class Todo_list:

    def __init__(self):

        self.todo = []

    def get_weight(self, entry):

        i = 0
        while i < len(self.todo) and self.todo[i][1] != entry:
            i = i + 1

        return (i, self.todo[i][0]) if i < len(self.todo) else None

    def add(self, weight, entry):

        old = self.get_weight(entry)
        if old == None:
            i = 0
            while i < len(self.todo) and self.todo[i][0] < weight:
                i = i + 1

            self.todo = self.todo[:i] + [(weight, entry)] + self.todo[i:]
        elif old[1] > weight:
            index = old[0]
            self.todo = self.todo[:index] + self.todo[index + 1:]
            self.add(weight, entry)

    def get_next_entry(self):

        entry = self.todo[0]
        self.todo = self.todo[1:]
        return entry

    def __str__(self):
        return str(self.todo)


roads = None

with open('sh-map.csv') as csvfile:
    roads = list(csv.reader(csvfile))

# print(roads)

map = Graph(10)

for road in roads:

    n1 = map.get_node_with_label(road[0])
    if n1 == None:
        n1 = map.add_new_node(road[0])
    n2 = map.get_node_with_label(road[2])
    if n2 == None:
        n2 = map.add_new_node(road[2])

    map.add_edge_label(n1, road[1], n2)

print(map)


# Computes the shortes path between Start and Dest.
# Start and Dest should be nodes of the adt_graph, which are numbers.
def shortest_path(map, Start, Dest):
    visited = [Start]
    todo = Todo_list()

    next = (0, Start)

    while next[1] != Dest:
        next_nodes = map.neighbours(next[1])  # computes pairs with distance and node

        next_nodes = [(int(weight) + next[0], node)
                      for weight, node in next_nodes
                      if not (node in visited)]

        for next_node in next_nodes:
            todo.add(next_node[0], next_node[1])

        visited.append(next[1])
        next = todo.get_next_entry()

    return next[0]

# Computes the shortest path bestween Start and End
# Safes every entry on the way
def shortest_path_full(map, Start, Dest):
    visited = [Start]
    todo = Todo_list()

    next = (0, Start)
    stops = [next]

    while next[1] != Dest:
        next_nodes = map.neighbours(next[1])  # computes pairs with distance and node

        next_nodes = [(int(weight) + next[0], node)
                      for weight, node in next_nodes
                      if not (node in visited)]

        for next_node in next_nodes:
            todo.add(next_node[0], next_node[1])

        visited.append(next[1])
        next = todo.get_next_entry()

        # Every stops (and its distance from the star) is appended
        stops.append(next)

    # Now, the complete path between Start and Dest is returned
    return stops

''''
start = None
dest = None

while start == None:
    start = map.get_node_with_label(input("Start: "))

while dest == None:
    dest = map.get_node_with_label(input("Ziel: "))

print((start, dest))
'''

# Example: Pritning the path between KI and PLÖ
print(shortest_path_full(map, 0, 4)) # [(0, 0), (19, 2), (33, 4)]

