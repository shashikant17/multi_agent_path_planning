from pyamaze import maze,COLOR,agent
m=maze()
m.CreateMaze(saveMaze=True,loopPercent=10)
print("Maze Path\n",m.path)
print("\nMaze Map",m.maze_map)

a=agent(m,footprints=True,color='green',filled=True)
b=agent(m,x=9,y=9,footprints=True,shape='arrow')
m.tracePath({a:m.path,b:m.path},delay=200,kill=True)
# m.tracePath({b:m.path},delay=200,kill=True)

m.run()