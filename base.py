from map import MapCell
from config import CELL_SIZE,GOAL_COORD,STRT_COORD

class AlgorithmBase():
    start = STRT_COORD
    goal  = GOAL_COORD

    start_cell = MapCell(start[0],start[1],CELL_SIZE)
    goal_cell  = MapCell(goal[0],goal[1],CELL_SIZE)

    def __init__(self, pygame_window):
        self.window = pygame_window
        self.draw_goal_and_start()

    def run(self):
        raise Exception('Base \'run\' method is not implemented.')

    def draw_spath(self, current, came_from):
        while not self.start_cell.equals(came_from[current]):
            current.set_path()
            current = came_from[current]
        self.window.render()

    def draw_goal_and_start(self):
        self.window.win_map.get_cell(self.start[0],self.start[1]).set_start() 
        self.window.win_map.get_cell(self.goal[0],self.goal[1]).set_goal()
        self.render()

    def render(self):
        self.window.render()

if __name__ == "__main__":
    raise Exception("Bad entry point file, try main.py ...")