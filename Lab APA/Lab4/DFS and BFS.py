import networkx as complex_graph
import matplotlib.pyplot as plt
import time


def BFS(graph, first_node):
    visited = []  # Create an array for visited nodes
    queue = [first_node]  # Create a queue for BFS
    while queue:
        node = queue.pop(0) #dequeue the vertex from queue
        if node not in visited:
            visited.append(node) # put the node in the visited list
            # Filter out the nodes that have already been visited
            not_visited = lambda n: n not in visited
            unvisited_nodes = filter(not_visited, graph.neighbors(node))
            # Add the unvisited nodes to the queue
            queue.extend(unvisited_nodes)
    return visited

def DFS(graph, start_node):
    visited = [] # store the value of the visited nodes
    stack = [start_node] # Create a stack for DFS
    while stack:
        node = stack.pop() #dequeue the vertex from stack
        if node not in visited:
            visited.append(node) # put the node in the visited list
            # Filter out the nodes that have already been visited
            not_visited = lambda n: n not in visited
            unvisited_nodes = filter(not_visited, graph.neighbors(node))
            # Add the unvisited nodes to the queue
            stack.extend(unvisited_nodes)
    return visited


DFS_time = []  #store time execution for DFS
BFS_time = []  #store time execution for BFS
node_counts = [] # store nodes

for n in range(15, 700 , 10):
    node_counts.append(n)
    graph = complex_graph.gnp_random_graph(n, 0.1)

    start_time = time.time()
    DFS(graph, 0)
    end_time = time.time()
    DFS_time.append(end_time - start_time)

    start_time = time.time()
    BFS(graph, 0)
    end_time = time.time()
    BFS_time.append(end_time - start_time)

plt.bar(node_counts, BFS_time, label="BFS", )
plt.xlabel('Number of nodes')
plt.ylabel('Execution time (seconds)')
plt.title('BFS Algorithm time execution')
plt.legend()
plt.show()


plt.bar(node_counts, DFS_time, label="DFS", )
plt.xlabel('Number of nodes')
plt.ylabel('Execution time (seconds)')
plt.title('DFS Algorithm time execution')
plt.legend()
plt.show()