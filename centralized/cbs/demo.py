from pyamaze import maze,COLOR,agent
m=maze(5,5)
m.CreateMaze(2,5,loadMaze='.\maze--2021-12-05--12-26-58.csv')
# m.CreateMaze(loadMaze='.\maze--2021-12-05--12-03-54.csv')
print("\nMaze Path: ",m.path)
print("\nMaze Map: ",m.maze_map)
print("\nMaze Rows: ",m.rows,"\nMaze Coloums: ",m.cols)
a=agent(m,footprints=True,color=COLOR.red,filled=True)
# b=agent(m,x=8,y=2,footprints=True,color=COLOR.yellow)
b=agent(m,x=5,y=1,goal=(2,5),footprints=True,color=COLOR.yellow)
m.tracePath({a:m.path},delay=100,kill=True)
m.tracePath({b:m.path},delay=100)

m.run()