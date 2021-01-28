# Pathfinding Algorithms
 This repository contains visualizations of several pathfinding algorithms.

# Requirements
 Installed python3 and pygame library for creating visualization
 ```python
 pip install pygame
 ```
 
 # Usage
  First of all, go to the 'config.py' file and set some constant values for yourself :
  
  ```python
  #config.py 
  #Here you must set some configs
  
  #Note that each window scale must be divided entirely by cell size!
  #Otherwise you will get the exception. 
  
  CELL_SIZE   =  None # -> 10
  WINDOW_SIZE =  None # -> (500,500)
  ```
  
 Next step is selecting coordinates of goal and start points :
  
   ```python
  #config.py 
  
  #the x coordinate satisfies this interval -> [0, WINDOW_SIZE[0]//CELL_SIZE-1] 
  #                              and also y -> [0, WINDOW_SIZE[1]//CELL_SIZE-1]
  
 GOAL_COORD = None # -> (WINDOW_SIZE[0]//CELL_SIZE-1,WINDOW_SIZE[1]//CELL_SIZE-1)
 STRT_COORD = None # -> (0,0)
  ```
 
 Well there is very little left, let's go to the main.py file and find 67 line :
 
  ```python
  #main.py [line 67]
  
  #Here you can see the object of algorithm class.
  #Сhange to one of the existing algorithms (Astar,BFS...)
  #Run main.py
  
  thread = threading.Thread(None,Astar(self).run)
                                #~~~~~~~~~~~
  ```
 Briefly about buttons :
  
- R_MOUSE_CLICK - delete obstacle
- L_MOUSE_CLICK - draw obstacle
- R - reset
- SPACE - run algorithm
#^
  
 Okay thats all, enjoy! 
