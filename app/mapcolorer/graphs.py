from enum import Enum

class Vertex:
    def __init__(self, id='', color=-1, neighbors=[]):
        if neighbors is None:
            self.neighbors = set()
        else:
            self.neighbors = set(neighbors)
        self.id = id
        self.color = color


