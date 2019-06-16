class Graph:

    def __init__(self, size):
        self.g = [None for i in range(size)]

    def add_node_label(self, n, nl):
        old_node = self.g[n]
        if old_node == None:
            self.g[n] = (nl, [])
        else:
            old_label, succs = old_node
            self.g[n] = (nl, succs)

    def add_new_node(self, nl):
        n = self.get_node_with_label(nl)
        if n != None:
            return n
        else:
            i = 0
            while i < len(self.g) and self.g[i] != None:
                i = i + 1

            if i == len(self.g):
                self.g.append((nl, []))
                return len(self.g) - 1
            else:
                self.g[i] = (nl, [])
                return i

    def add_edge_label(self, n1, el, n2):
        old_node = self.g[n1]
        if old_node == None:
            self.g[n1] = (None, [(el, n2)])
        else:
            nl, succs = self.g[n1]
            succs.append((el, n2))
        old_node = self.g[n2]
        if old_node == None:
            self.g[n2] = (None, [(el, n1)])
        else:
            nl, succs = self.g[n2]
            succs.append((el, n1))

    def add_new_edge(self, nl1, el, nl2):
        n1 = self.get_node_with_label(nl1)
        n2 = self.get_node_with_label(nl2)
        if n1 != None and n2 != None:
            self.add_edge_label(n1, el, n2)
            return True
        else:
            return False

    # Selektoren:
    def get_node_label(self, n):
        return self.g[n][0]

    def get_node_with_label(self, l):
        i = 0
        while i < len(self.g) and (self.g[i] == None or self.g[i][0] != l):
            i = i + 1

        return i if i < len(self.g) else None

    def get_edge_label(self, n1, n2):
        succs = self.g[n1][1]
        i = 0
        while i < len(succs) and succs[i][1] != n2:
            i = i + 1

        if i == len(succs):
            return None
        else:
            return succs[i][0]

    # Bestimmt alle Nachbarn eines gegeben Knoten mit dem zugehörigen label
    # als Liste
    def neighbours(self, n):
        return list(self.g[n][1])  # produce a copy

    def __str__(self):

        return (str(self.g))
