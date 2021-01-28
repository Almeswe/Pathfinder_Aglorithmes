from map import MapCell
from math import sqrt,pow
from queue import PriorityQueue
from config import CELL_SIZE, WINDOW_SIZE

class Astar():

    start = (0,0)
    goal  = (WINDOW_SIZE[0]//CELL_SIZE-1,WINDOW_SIZE[1]//CELL_SIZE-1)

    start_cell = MapCell(start[0],start[1],CELL_SIZE)
    goal_cell  = MapCell(goal[0],goal[1],CELL_SIZE)

    def __init__(self, pygame_window):
        self.window = pygame_window
        self.draw_goal_and_start()

    def run(self):
        frontier = PriorityQueue()
        frontier.put(0)
        priority_of_frontier = {}
        priority_of_frontier[0] = self.start_cell

        came_from = {}
        cost_so_far = {}

        came_from[self.start_cell] = None
        cost_so_far[self.start_cell] = 0

        while not frontier.empty():
            current = priority_of_frontier[frontier.get()]
            current.set_visited()

            if current.equals(self.goal_cell):
                while not self.start_cell.equals(came_from[current]):
                    current.set_path()
                    current = came_from[current]
                self.window.render()
                break

            for next in self.window.win_map.get_nears(current):
                if next.isBlocked():
                    continue
                new_cost = cost_so_far[current] #+ cost?
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(self.goal_cell,next)
                    frontier.put(priority)
                    priority_of_frontier[priority] = next
                    came_from[next] = current
            self.render() 

    def heuristic(self, from_cell, to_cell):
        return sqrt(pow(from_cell.x - to_cell.x,2)+pow(from_cell.y - to_cell.y,2))

    def draw_goal_and_start(self):
        self.window.win_map.get_cell(self.start[0],self.start[1]).set_start() 
        self.window.win_map.get_cell(self.goal[0],self.goal[1]).set_goal()
        self.render()

    def render(self):
        self.window.render()

if __name__ == "__main__":
    raise Exception("Bad entry point file, try main.py ...")