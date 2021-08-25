import random
import numpy as np

import algorithmic_complexity.disjointset as ds

def makeMaze(rows, cols: int):
    maze = np.zeros((rows*2 + 1, cols*2+1))
    maze[1::2, 1::2] = 1
    maze[ 1][ 0] = 3
    maze[-2][-1] = 3

    walls = []
    walls.extend((i*cols+j, i*cols+j+1) for j in range(cols-1) for i in range(rows-1))
    walls.extend((i*cols+j, (i+1)*cols+j) for j in range(cols-1) for i in range(rows-1))
    walls.extend((i*cols+cols-1,(i+1)*cols+cols-1) for i in range(rows-1))
    walls.extend(((rows-1)*cols+j, (rows-1)*cols+j+1) for j in range(cols-1))

    s = ds.DisjointSet(len(walls))
    random.shuffle(walls)
    while len(walls) > 0:
        e1, e2 = walls.pop()
        r1, c1 = e1 // cols, e1 % cols
        r2, c2 = e2 // cols, e2 % cols
        if not s.sameset(e1, e2):
            if r1 == r2 and c1 < c2:
                maze[r1*2+1][c1*2+2] = 1
            elif r1 == r2:
                maze[r1*2+1][c2*2+2] = 1
            elif c1 == c2 and r1 < r2:
                maze[r1*2+2][c1*2+1] = 1
            else:
                maze[r2*2+2][c1*2+1] = 1

            s.union(e1, e2)

    return maze
