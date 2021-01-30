from queue import PriorityQueue

from base import AlgorithmBase

class Greedy(AlgorithmBase):

    def run(self):
        frontier = PriorityQueue()
        frontier.put(0)
        priority_of_frontier = {}
        priority_of_frontier[0] = self.start_cell

        came_from = {}
        came_from[self.start_cell] = None

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

                if next not in came_from:
                    priority = self.heuristic(self.goal_cell,next)
                    priority_of_frontier[priority] = next
                    frontier.put(priority)
                    came_from[next] = current
            self.render()


if __name__ == "__main__":
    raise Exception("Bad entry point file, try main.py ...")