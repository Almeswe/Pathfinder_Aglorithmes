import map
import sys
import pygame
import threading

from bfs import BFS
from astar import Astar
from dijkstra import Dijkstra

from config import WINDOW_SIZE,CELL_SIZE

class Window():

    win_size = None
    win_title =  None
    win_instance = None 
    win_draw_grid = False

    win_map = map.Map(WINDOW_SIZE,CELL_SIZE)

    def __init__(self, win_size, win_title = "pathfinders"):
        pygame.init()
        self.win_size = win_size
        self.win_title = win_title
        
        self.win_instance = pygame.display.set_mode(win_size)
        pygame.display.set_caption(self.win_title)

    def wndproc(self):
        self.render()
        hold_for_draw = False
        hold_for_blur = False

        thread = None

        LEFT = 1
        RIGHT = 3

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    hold_for_draw = True
                if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT and hold_for_draw:
                    hold_for_draw = False
                if hold_for_draw:
                    try:
                        self.block(event.pos)
                    except AttributeError:
                        pass

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                    hold_for_blur = True
                if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT and hold_for_blur:
                    hold_for_blur = False
                if hold_for_blur:
                    try:
                        self.unblock(event.pos)
                    except AttributeError:
                        pass

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if thread == None or not thread.is_alive():

                        # Set current algorithm here (Astar,BFS...)
                        thread = threading.Thread(None,Astar(self).run)
                        #                              ~~~~~~~~~~~
                        thread.start()
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    if thread == None or not thread.is_alive():
                        self.reset()


    def unblock(self,pos):
        self.win_map.get_cell(pos[0]//CELL_SIZE,pos[1]//CELL_SIZE).set_default()
        self.render()

    def block(self, pos):
        self.win_map.get_cell(pos[0]//CELL_SIZE,pos[1]//CELL_SIZE).set_block()
        self.render()

    def render(self):
        self.win_instance.fill((255,255,255))
        self.draw_grid()
        self.draw_cells()

        #without it alg works faster
        #pygame.time.Clock().tick(150)
        pygame.display.update()

    def draw_grid(self):
        if not self.win_draw_grid:
            return
        line_color = (0,0,0)
        for x in range(WINDOW_SIZE[0] // CELL_SIZE):
            pygame.draw.line(self.win_instance,line_color,[x*CELL_SIZE,0],[x*CELL_SIZE,WINDOW_SIZE[1]])
        for y in range(WINDOW_SIZE[1] // CELL_SIZE):
            pygame.draw.line(self.win_instance,line_color,[0,y*CELL_SIZE],[WINDOW_SIZE[0],y*CELL_SIZE])

    def draw_cells(self):
        for i in self.win_map.cells:
            if (i.type != map.Marker.DFLT):
                pygame.draw.rect(self.win_instance,i.type.value,pygame.Rect(i.x*CELL_SIZE,i.y*CELL_SIZE,i.size,i.size))

    def reset(self):
        for cell in self.win_map.cells:
            cell.type = map.Marker.DFLT
        self.render()


if __name__ == "__main__":
    window = Window(WINDOW_SIZE)
    window.wndproc()