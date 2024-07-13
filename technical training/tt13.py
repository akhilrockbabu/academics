from collections import deque

def bfs_shortest_path(graph,start,goal):
    visited=set()
    queue=deque([[start]])
    print(deque)
    while queue:
        path=queue.popleft()
        node=path[-1]

        if node==goal:
            return path
        
        elif node not in visited:
            for neighbour in graph[node]:
                new_path=list(path)
                new_path.append(neighbour)
                queue.append(new_path)
            visited.add(node)
        print(queue)
    return None

graph={
    '1':['2'],
    '2':['3','5'],
    '3':['4'],
    '4':['5'],
    '5':['6'],
    '6':[]
}

shortest_path=bfs_shortest_path(graph,'1','6')
print("shortest path : ",shortest_path)


#github.com/zakbasil/Algorithms