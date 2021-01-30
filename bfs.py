from queue import Queue

from base import AlgorithmBase

class BFS(AlgorithmBase):

    def run(self):
        frontier = Queue()
        frontier.put(self.start_cell)
        came_from = {}
        came_from[self.start_cell] = None

        while not frontier.empty():
            current = frontier.get()
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
                    frontier.put(next)
                    came_from[next] = current 
            self.render()


if __name__ == "__main__":
    raise Exception("Bad entry point file, try main.py ...")