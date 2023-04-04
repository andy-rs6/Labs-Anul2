graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

# visited = [] # Create an array for visited nodes
# queue = [] # Create a queue for BFS
#
# def BFS(visited, node, graph):
#     visited.append(node) #put the node in visited array
#     queue.append(node) #mark the source node as visited
#     while queue:
#         index = queue.pop(0) #dequeue the vertex from queue
#         for neighbour in graph[index]: #Get all adjacent vertices of the dequeued vertex
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)
#
#

visited = set() # store the value of the visited nodes

def dfs(visited, graph, node):  #function for dfs
    if node not in visited: # check whether any node of the graph is visited or not
        visited.add(node) #and node to the visited set of nodes

        for neighbour in graph[node]: # go to the neighboring node of the graph
            dfs(visited, graph, neighbour) # (recursion) call the function again



dfs(visited, graph, '5')
# BFS(visited, '5', graph)