#Here you must set some configs

#Note that each window scale must be divided entirely by cell size!
#Otherwise you will get the exception.
CELL_SIZE   =  None # -> 10
WINDOW_SIZE =  None # -> (500,500)

#the x coordinate satisfies this interval -> [0, WINDOW_SIZE[0]//CELL_SIZE-1] 
#                              and also y -> [0, WINDOW_SIZE[1]//CELL_SIZE-1]
GOAL_COORD = None # -> (WINDOW_SIZE[0]//CELL_SIZE-1,WINDOW_SIZE[1]//CELL_SIZE-1)
STRT_COORD = None # -> (0,0)

if __name__ == "__main__":
    raise Exception("Bad entry point file, try main.py ...")