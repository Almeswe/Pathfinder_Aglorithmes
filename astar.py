from math import sqrt,pow
from queue import PriorityQueue

from base import AlgorithmBase

class Astar(AlgorithmBase):

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
                self.draw_spath(current,came_from)
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

if __name__ == "__main__":
    raise Exception("Bad entry point file, try main.py ...")