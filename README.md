# Automata-Theory
Programs that display a render (grid) according to a specified rule of cellular automaton, given an initial grid state.

### FILE INFORMATION:

config.txt:  Contains initial state of the grid, i.e. the location of cells that are live initially. <br />
rule.py:     Contains the rule according to which the render changes in each succesive state. <br />

output.txt:  File that Displays the grid state in each iteration. Live cells are represented by an 'X' <br />
             while dead cells are represented by an 'O'.

Instructions to run (Type the following command on terminal): <br />
for q1: q1/rule.py <br />
for q2: q2/rule.py <br />
for q3: q3/rule.py <br />

### RULES:

q1: if the cell to the immediate left of the current cell is live, the current cell becomes live.

q2: Conway's Game of Life-
   1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
   2. Any live cell with two or three live neighbours lives on to the next generation.
   3. Any live cell with more than three live neighbours dies, as if by overpopulation.
   4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
   
q3: 
  1. A live cell in the current render becomes dead in the next render.
  2. A dead cell in the current render becomes live in the next render.
