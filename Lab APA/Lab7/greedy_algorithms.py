# import networkx as nx
# import random
# import time
# import matplotlib.pyplot as plt
#
# class RandomGraph:
#     def __init__(self, nodes, sparse=False):
#         self.nodes = nodes
#         self.sparse = sparse
#         self.graph = self.generate_graph()
#
#     def generate_graph(self):
#         if self.sparse:
#             edge_prob = 0.1  # smaller probability for sparse graph
#         else:
#             edge_prob = 0.8  # larger probability for dense graph
#
#         graph = nx.fast_gnp_random_graph(self.nodes, edge_prob)
#
#         for (u, v, w) in graph.edges(data=True):
#             w['weight'] = random.randint(1, 100)
#
#         return graph
#
#
# class MST:
#     def __init__(self, graph):
#         self.graph = graph
#
#     def run_prim(self):
#         start_time = time.time()
#         mst = nx.minimum_spanning_tree(self.graph, algorithm='prim')
#         end_time = time.time()
#         return mst, end_time - start_time
#
#     def run_kruskal(self):
#         start_time = time.time()
#         mst = nx.minimum_spanning_tree(self.graph, algorithm='kruskal')
#         end_time = time.time()
#         return mst, end_time - start_time
#
#
# class GraphDrawer:
#     def __init__(self, graph, mst, algorithm):
#         self.graph = graph
#         self.mst = mst
#         self.algorithm = algorithm
#
#     def draw(self):
#         pos = nx.spring_layout(self.graph)
#         nx.draw_networkx(self.graph, pos, with_labels=False, node_size=100)
#         nx.draw_networkx_edges(self.graph, pos, edgelist=self.mst.edges(), width=2, edge_color='r')
#         plt.title(f'MST using {self.algorithm}')
#         plt.show()
#
#
# def compare_algorithms(nodes, sparse):
#     prim_times = []
#     kruskal_times = []
#
#     for n in nodes:
#         graph_obj = RandomGraph(n, sparse)
#         mst_obj = MST(graph_obj.graph)
#
#         _, prim_time = mst_obj.run_prim()
#         prim_times.append(prim_time)
#
#         _, kruskal_time = mst_obj.run_kruskal()
#         kruskal_times.append(kruskal_time)
#
#     # plot the results
#     plt.figure(figsize=(10, 6))
#     plt.plot(nodes, prim_times, label="Prim's Algorithm")
#     plt.plot(nodes, kruskal_times, label="Kruskal's Algorithm")
#     plt.xlabel('Number of nodes')
#     plt.ylabel('Execution time (seconds)')
#     plt.title('Performance of Prim\'s and Kruskal\'s Algorithms')
#     plt.legend()
#     plt.grid(True)
#     plt.show()
#
# nodes = [100, 500, 1000, 2000]
# compare_algorithms(nodes, False)  # for a dense graph
# compare_algorithms(nodes, True)  # for a sparse graph
#
# nodes = 10
# sparse = False
#
# graph_obj = RandomGraph(nodes, sparse)
# mst_obj = MST(graph_obj.graph)
#
# mst_prim, _ = mst_obj.run_prim()
# drawer = GraphDrawer(graph_obj.graph, mst_prim, "Prim's Algorithm")
# drawer.draw()
#
# mst_kruskal, _ = mst_obj.run_kruskal()
# drawer = GraphDrawer(graph_obj.graph, mst_kruskal, "Kruskal's Algorithm")
# drawer.draw()
#
# sparse = True
#
# graph_obj = RandomGraph(nodes, sparse)
# mst_obj = MST(graph_obj.graph)
#
# mst_prim, _ = mst_obj.run_prim()
# drawer = GraphDrawer(graph_obj.graph, mst_prim, "Prim's Algorithm Spare")
# drawer.draw()
#
# mst_kruskal, _ = mst_obj.run_kruskal()
# drawer = GraphDrawer(graph_obj.graph, mst_kruskal, "Kruskal's Algorithm Spare")
# drawer.draw()

import time
import matplotlib.pyplot as plt
import networkx as nx

# Implementation of Prim's algorithm
def prim(graph):
    mst = []
    visited = set()
    nodes = list(graph.nodes)
    visited.add(nodes[0])

    while len(visited) < len(nodes):
        min_edge = None
        min_weight = float('inf')

        for node in visited:
            for neighbor in graph.neighbors(node):
                edge_data = graph.get_edge_data(node, neighbor)
                weight = edge_data['weight']
                if neighbor not in visited and weight < min_weight:
                    min_edge = (node, neighbor)
                    min_weight = weight

        edge = min_edge
        mst.append(edge)
        visited.add(edge[1])

    return mst



# Implementation of Kruskal's algorithm
def kruskal(graph):
    mst = []
    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    uf = {node: node for node in graph.nodes}

    for edge in edges:
        u, v, weight = edge
        if uf[u] != uf[v]:
            mst.append((u, v))
            old_group = uf[v]
            for node, group in uf.items():
                if group == old_group:
                    uf[node] = uf[u]

    return mst

# Function to measure execution time
def measure_execution_time(func, graph):
    start_time = time.time()
    result = func(graph)
    end_time = time.time()
    execution_time = end_time - start_time

    return result, execution_time

def empirical_analysis(graph_sizes):
    prim_times = []
    kruskal_times = []

    for size in graph_sizes:
        graph = nx.complete_graph(size)
        for (u, v) in graph.edges():
            graph[u][v]['weight'] = float(1)

        prim_mst, prim_time = measure_execution_time(prim, graph)
        prim_times.append(prim_time)
        draw_graph_with_mst(graph, prim_mst, "Prim's Algorithm")  # Draw the graph with minimum spanning tree using Prim's algorithm

        kruskal_mst, kruskal_time = measure_execution_time(kruskal, graph)
        kruskal_times.append(kruskal_time)
        draw_graph_with_mst(graph, kruskal_mst, "Kruskal's Algorithm")  # Draw the graph with minimum spanning tree using Kruskal's algorithm

    return prim_times, kruskal_times

# Function to draw the graph with the minimum spanning tree
def draw_graph_with_mst(graph, mst, algorithm_name):
    pos = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos, with_labels=True, node_color='lightblue')
    nx.draw_networkx_edges(graph, pos, edgelist=mst, edge_color='red', width=2)
    plt.title(f"Graph with Minimum Spanning Tree ({algorithm_name})")
    plt.show()

# Example usage
graph_sizes = [20, 40, 80, 100, 120]
prim_times, kruskal_times = empirical_analysis(graph_sizes)
plt.plot(graph_sizes, prim_times, label="Prim's Algorithm")
plt.plot(graph_sizes, kruskal_times, label="Kruskal's Algorithm")
plt.xlabel('Graph Size')
plt.ylabel('Execution Time (s)')
plt.title('Empirical Analysis of Prim and Kruskal Algorithms')
plt.legend()
plt.show()