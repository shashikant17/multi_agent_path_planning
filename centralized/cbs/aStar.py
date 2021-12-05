from os import cpu_count
from pyamaze import maze,agent,textLabel,COLOR
from queue import PriorityQueue
from DFS import DFS
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)
def aStar(m,rows,cols,mXEnd,mYEnd):
    # start=(m.rows,m.cols)
    start = (rows,cols)
    end = (mXEnd,mYEnd)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,end)

    open=PriorityQueue()
    open.put((h(start,end),h(start,end),start))
    aPath={}
    while not open.empty():
        currCell=open.get()[2]
        if currCell==end:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,end)

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,end),childCell))
                    aPath[childCell]=currCell
    fwdPath={}
    cell=end
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(5,5)
    m.CreateMaze(1,5,loadMaze='maze--2021-12-05--12-45-12.csv',theme=COLOR.dark)
    
    # Agent A -> A*
    a=agent(m,x=4,y=3,footprints=False,color=COLOR.red)
    # Agent B -> BFS
    b=agent(m,color=COLOR.yellow,footprints=False)
    # c=agent(m,x=5,y=1,color=COLOR.red)
    # Agent D -> DFS
    d=agent(m,x=2,y=2,color=COLOR.cyan,footprints=False)
    # e=agent(m,color=COLOR.black,footprints=True)
    
    # Agent A -> A* path
    aPath=aStar(m,rows=4,cols=3,mXEnd=1,mYEnd=5)
    # Agent B -> BFS path
    bPath=m.path
    # cPath=aStar(m,rows=5,cols=1)
    # Agent D -> DFS path
    dPath=DFS(m,rows=2,cols=2,mXEnd=1,mYEnd=5)

    # Trace Path by all Agents
    m.tracePath({a:aPath},kill=True,delay=1000)
    m.tracePath({b:bPath},kill=True,delay=1000)
    # # m.tracePath({c:cPath},kill=True,delay=3000)
    m.tracePath({d:dPath},kill=True,delay=1000)
    # m.tracePath({e:m.path},delay=3000)

    # m.tracePath({a:aPath,b:bPath,d:dPath},delay=100,kill=True)

    # al=textLabel(m,'A Star Path Length for Agent A',len(aPath)+1)
    # bl = textLabel(m,'A Star Path Length for Agent B',len(bPath)+1)
    # cl = textLabel(m,'A Star Path Length for Agent C',len(cPath)+1)
    # dl = textLabel(m,'A Star Path Length for Agent D',len(dPath)+1)
    # el = textLabel(m,'A Star Path Length for Agent E',len(dPath)+1)

    m.run()