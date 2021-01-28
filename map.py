from enum import Enum
from config import CELL_SIZE 

class Marker(Enum):
    BLCK = (0,0,0),
    FRNT = (200,180,220),
    VSTD = (0,255,0),
    GOAL = (255,0,0),
    STRT = (0,0,255),
    PATH = (255,255,0),
    DFLT = (255,255,255)

class MapCell():
    x = None
    y = None
    size = None

    type  = Marker.DFLT

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.type = Marker.DFLT

    def isBlocked(self):
        return True if self.type == Marker.BLCK else False

    def isFront(self):
        return True if self.type == Marker.FRNT else False

    def isVisited(self):
        return True if self.type == Marker.VSTD else False

    def isGoal(self):
        return True if self.type == Marker.GOAL else False

    def isStart(self):
        return True if self.type == Marker.STRT else False

    def isPath(self):
        return True if self.type == Marker.PATH else False

    def isDefault(self):
        return True if self.type == Marker.DFLT else False

    def set_visited(self):
        if self.isStart() or self.isGoal():
            return
        self.type = Marker.VSTD

    def set_front(self):
        if self.isBlocked() or self.isVisited() or self.isGoal() or self.isStart():
            return
        self.type = Marker.FRNT

    def set_block(self):
        if self.type == Marker.DFLT:
            self.type = Marker.BLCK

    def set_default(self):
        if self.type == Marker.BLCK:
            self.type = Marker.DFLT

    def set_path(self):
        if self.isStart() or self.isGoal() or self.isBlocked():
            return
        self.type = Marker.PATH

    def set_start(self):
        self.type = Marker.STRT

    def set_goal(self):
        self.type = Marker.GOAL

    def equals(self, cell):
        return True if self.x == cell.x and self.y == cell.y else False

    def to_str(self):
        return str(self.x) + str(self.y)


class Map():
    cells = []

    def __init__(self, window_size, cell_size):
        self.window_size = window_size
        self.cell_size   = cell_size
        self.create_map()

    def create_map(self):
        width  = self.window_size[0]
        height = self.window_size[1]

        if width % self.cell_size != 0 or height % self.cell_size != 0:
            raise Exception('Bad window scales ...')

        counter_x = width  // self.cell_size
        counter_y = height // self.cell_size

        for y in range(counter_y):
            for x in range(counter_x):
                self.cells.append(MapCell(x,y,CELL_SIZE))

    def get_nears(self, cell):
        nears = []
        x = cell.x
        y = cell.y
        if self.possible_x_coord(x-1) and self.possible_y_coord(y-1):
            nears.append(self.get_cell(x-1,y-1))

        if self.possible_y_coord(y-1):
            nears.append(self.get_cell(x,y-1))
        
        if self.possible_x_coord(x+1) and self.possible_y_coord(y-1):
            nears.append(self.get_cell(x+1,y-1))

        if self.possible_x_coord(x+1):
            nears.append(self.get_cell(x+1,y))

        if self.possible_x_coord(x+1) and self.possible_y_coord(y+1):
            nears.append(self.get_cell(x+1,y+1))

        if self.possible_y_coord(y+1):
            nears.append(self.get_cell(x,y+1))

        if self.possible_x_coord(x-1) and self.possible_y_coord(y+1):
            nears.append(self.get_cell(x-1,y+1))

        if self.possible_x_coord(x-1):
            nears.append(self.get_cell(x-1,y))

        #for c in nears:
        #    c.set_front()
        return nears

    def get_cell(self,x,y):
        for c in self.cells:
            if c.x == x and c.y == y:
                return c
        return None

    def possible_x_coord(self, coord):
        return False if coord < 0 or coord > self.window_size[0]//CELL_SIZE-1 else True

    def possible_y_coord(self, coord):
        return False if coord < 0 or coord > self.window_size[1]//CELL_SIZE-1 else True


if __name__ == "__main__":
    raise Exception("Bad entry point file, try main.py ...")