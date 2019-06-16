class Graph:

    def __init__(self, size):

        # Graph wird als zweidimensionale Matrix der Größe size*size dargestellt
        # Alle Einträge sin zu Beginn 0 (keine Kanten)

        self.matrix = [[0 for i in range(size)] for j in range(size)]

    def add_edge(self, node1, edge, node2):

        # Eintrag in der Matrix wird geändert
        self.matrix[node1][node2] = edge

    # Selektoren

    # Kantenbeschriftung wird aus der Matrix ausgelesen
    def get_edge(self, node1, node2):

        return self.matrix[node1][node2]

    # Bestimmt alle Nachbarn eines gegeben Knoten
    # Ausgabe als Liste mit Knotennummern
    def neighbours(self, node):

        neighbours = []
        for i in range(len(self.matrix)):
            if self.matrix[node][i] != 0:
                neighbours.append(i)

        return neighbours


#--------------------------------Testprogramm----------------------------------------

# Beispiel aus der Vorlesung

sh_map = Graph(5)
sh_map.add_edge(0, 70, 1)
sh_map.add_edge(0, 69, 2)
sh_map.add_edge(1, 80, 3)
sh_map.add_edge(1, 30, 2)
sh_map.add_edge(2, 50, 3)
sh_map.add_edge(2, 60, 4)
sh_map.add_edge(3, 70, 4)

#Ausgabe der Matrix
print(sh_map.matrix)
'''Ausgabe: 
[[0, 70, 69, 0, 0], 
 [0, 0, 30, 80, 0], 
 [0, 0, 0, 50, 60], 
 [0, 0, 0, 0, 70], 
 [0, 0, 0, 0, 0]]'''

print(sh_map.get_edge(0, 1)) #Ausgabe: 70
print(sh_map.get_edge(2, 1)) #Ausgabe_ 0

print(sh_map.neighbours(2)) #Ausgabe: [3,4]
