from pyamaze import maze,agent,COLOR
def DFS(m,rows,cols,mXEnd,mYEnd):
    # start=(m.rows,m.cols)
    start = (rows,cols)
    end=(mXEnd,mYEnd)
    explored=[start]
    frontier=[start]
    dfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop()
        if currCell==end:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell]=currCell
    fwdPath={}
    cell=end
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return fwdPath


if __name__=='__main__':
    m=maze(5,5)
    m.CreateMaze(1,5)
    path=DFS(m,5,1,1,5)
    a=agent(m,5,1,footprints=True)
    m.tracePath({a:path})


    m.run()