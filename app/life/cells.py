class Cell:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.age = 0


    def __eq__(self, other):
        if other != None and isinstance(other, Cell):
            return self.x == other.x and self.y == other.y
        return False


    def __hash__(self):
        return hash(self.x) * hash(self.y)


    def __str__(self):
        return 'Cell(' + str(self.x) + ',' + str(self.y) + ',age=' + str(self.age) + ')'


    def is_neighbor(self, cell):
        return (cell != None and isinstance(cell, Cell) and cell != self and
                abs(cell.x - self.x) <= 1 and abs(cell.y - self.y) <= 1)


class Plane:
    def __init__(self, cells=set(), generation=0):
        self.cells = set(cells)
        self.generation = generation


    def add_cell(self, cell):
        if cell != None and isinstance(cell, Cell):
            self.cells.add(cell)


    def remove_cell(self, cell):
        if cell != None and isinstance(cell, Cell) and cell in self.cells:
            self.cells.remove(cell)


    def neighbors(self, cell):
        if cell != None and isinstance(cell, Cell):
            return set({c for c in self.cells if c.is_neighbor(cell)})
        return set()


    def neighbors_count(self, cell):
        return len(self.neighbors(cell))


    def cell_at(self, x, y):
        cells_at = list([c for c in self.cells if c.x == x and c.y == y])
        if len(cells_at) > 0:
            return cells_at[0]
        return None


    def empty_neigboring_spots(self, cell):
        if cell != None and isinstance(cell, Cell):
            return set([(x, y)
                        for x in range(cell.x - 1, cell.x + 2)
                        for y in range(cell.y - 1, cell.y + 2)
                        if self.cell_at(x, y) is None])
        return set()


    def all_empty_neighboring_spots(self):
        all_empties = set()
        for cell in self.cells:
            all_empties |= self.empty_neigboring_spots(cell)
        return sorted(all_empties)


    def newborns(self):
        return {Cell(x, y) for (x, y) in self.all_empty_neighboring_spots() if self.neighbors_count(Cell(x, y)) == 3}


    def dying(self):
        return {c for c in self.cells if self.neighbors_count(c) < 2 or self.neighbors_count(c) > 3}


    def change_generation(self):
        new = self.newborns()
        dead = self.dying()
        self.cells -= dead
        for c in self.cells:
            c.age += 1
        self.cells |= new
        self.generation += 1


    def __str__(self):
        return 'Plane(generation=' + str(self.generation) + ', cells=(' + ', '.join({str(c) for c in self.cells}) + ')'


if __name__ == '__main__':
    plane = Plane()
    plane.cells.add(Cell(1, 1))
    plane.cells.add(Cell(2, 1))
    plane.cells.add(Cell(3, 1))

    for i in range(0, 10):
        print(str(plane))
        plane.change_generation()
