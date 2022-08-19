def dfs(x, y, visited):
    global cycle 
    if finished[x][y] == 1: # if문 순서 잘 지켜야 한다. 
        return
    if visited[x][y] == 1:
        cycle = True
        return
    visited[x][y] = 1
    dx, dy = direction[graph[x][y]]
    dfs(x + dx, y + dy, visited) 
    finished[x][y] = 1