from math import sqrt
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

                next.set_visited()
                for near_of_near in self.window.win_map.get_nears(next):
                    near_of_near.set_front()

                new_cost = cost_so_far[current] + self.heuristic(next,current)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(self.goal_cell,next)
                    priority_of_frontier[priority] = next
                    frontier.put(priority)
                    came_from[next] = current

            self.render() 

if __name__ == "__main__":
    raise Exception("Bad entry point file, try main.py ...")