class Vertex:
    def __init__(self, id = '', color = -1, neighbors = set()):
        self.id = id
        self.color = color
        if neighbors is None:
            self.neighbors = set()
        else:
            self.neighbors = set(neighbors)


    def has_neighbors_of_color(self, color):
        for neighbor in self.neighbors:
            if neighbor.color == color:
                return True
        return False


    def __str__(self):
        return "Vertex(%s, %d)" % (self.id, self.color)


    def __repr__(self):
        return "Vertex(%s, %d)" % (self.id, self.color)


class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2


    def __hash__(self):
        return hash(self.v1) * hash(self.v2)


    def __eq__(self, other):
        return (other is not None and isinstance(other, Edge) and
            ((other.v1 == self.v1 and other.v2 == self.v2) or (other.v1 == self.v2 and other.v2 == self.v1)))


class Graph:
    def __init__(self, vertices = list(), adjacency_list = list()):
        self.vertices = list(vertices)
        self.vertices_set = set(vertices)
        self.edges = set()
        self.adjacency_list = list(adjacency_list)
        for (a, b) in adjacency_list:
            self.register_edge(a, b)


    def register_edge(self, a, b):
        a.neighbors.add(b)
        b.neighbors.add(a)
        self.vertices_set.add(a)
        self.vertices_set.add(b)
        self.edges.add(Edge(a, b))


#Fails on a 6-vertices Apollonian - colors it with 5 colors
def color_naive_ignoreneighbors(graph):
    no_of_colors = 0
    colored = set()
    uncolored = list(graph.vertices)
    while len(uncolored) > 0:
        v = uncolored.pop()
        col = 0
        while v.has_neighbors_of_color(col):
            col += 1
        v.color = col
        if no_of_colors < col + 1:
            no_of_colors = col + 1
        colored.add(v)
    assert all_colored(graph)
    assert check_coloring(graph) < 5


def all_colored(graph):
    for v in graph.vertices:
        if v.color < 0:
            return False
    return True


def check_coloring(graph):
    colors = set()
    for v in graph.vertices:
        if v.color < 0:
            return False
        colors.add(v.color)
        for v1 in v.neighbors:
            if v.color == v1.color:
                return False
    print("Number of colors: %d" % len(colors))
    if len(colors) <= 4:
        print(str(graph.vertices))
    return len(colors)


# Works for connected graphs only.
def color_depthsearch(graph):
    no_of_colors = 0
    colored = set()
    to_color = list()
    to_color.append(graph.vertices[0])
    while len(to_color) > 0:
        v = to_color.pop()
        col = 0
        while v.has_neighbors_of_color(col):
            col += 1
        v.color = col
        if no_of_colors < (col + 1):
            no_of_colors = col + 1
        colored.add(v)
        for v1 in v.neighbors:
            if v1.color < 0:
                to_color.append(v1)
    assert all_colored(graph)
    check_coloring(graph) < 5


def color_widthsearch(graph, ):
    no_of_colors = 0
    colored = set()
    to_color = list()
    to_color.append(graph.vertices[0])
    while len(to_color) > 0:
        v = to_color.pop(0)
        col = 0
        while v.has_neighbors_of_color(col):
            col += 1
        v.color = col
        if no_of_colors < (col + 1):
            no_of_colors = col + 1
        colored.add(v)
        for v1 in v.neighbors:
            if v1.color < 0:
                to_color.append(v1)
    assert all_colored(graph)
    assert check_coloring(graph) < 5
    return True


def permutations(l):
    if l is None or len(l) <= 1:
        return l
    if len(l) == 2:
        return [l, list(reversed(l))]
    first = l[0]
    result = list()
    prev_result = permutations(l[1:])
    for smaller_l in prev_result:
        for i in range(0, len(l)):
            new_l = list(smaller_l[:])
            new_l[i:i] = [first]
            result.append(new_l)
    return result


def test_permutations():
    l = permutations([1, 2, 3, 4])
    print(l)
    print(len(l))
    assert len(l) == 24


if __name__ == '__main__':
    v0 = Vertex("v0")
    v1 = Vertex("v1")
    v2 = Vertex("v2")
    v3 = Vertex("v3")
    v4 = Vertex("v4")
    v5 = Vertex("v5")
    # v6 = Vertex("v6")
    # v7 = Vertex("v7")
    # v8 = Vertex("v8")

    # A simple Apollonian with 5 vertices
    # edges = ((v0 , v1), (v0 , v2), (v0 , v3), (v0 , v4), (v1 , v2), (v1 , v3), (v1 , v3), (v2 , v3),
    #          (v2 , v4), (v3, v4))

    # A simple Apollonian with 6 vertices
    edges = ((v0 , v1), (v0 , v2), (v0 , v3), (v0 , v4), (v1 , v2), (v1 , v3), (v1 , v3), (v2 , v3),
             (v2 , v4), (v3, v4), (v0, v5), (v2, v5), (v4, v5))

        # graph = Graph((v0, v1, v2, v3, v4, v5, v6, v7, v8),
        #           ((v0 , v1), (v0 , v2), (v0 , v3), (v0 , v4), (v0 , v5), (v0 , v6), (v0 , v7), (v0 , v8),
        #            (v1 , v2), (v2, v3), (v3, v4), (v4, v5), (v5, v6), (v6, v7), (v7, v8), (v8, v1)))

    # for vertices in permutations([v0, v1, v2, v3, v4, v5]):
    all_vertices = [v0, v1, v2, v3, v4, v5]
    for vertice in all_vertices:
        vertices = [vertice]
        vertices.extend([v for v in all_vertices if v != vertice])
        graph = Graph(vertices, edges)
        #color_depthsearch(graph)
        color_widthsearch(graph)

    # for vertices in permutations([v0, v1, v2, v3, v4, v5]):
    #     color_naive_ignoreneighbors(graph)
