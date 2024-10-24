import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val, color=node.color)
        if node.left:
            graph.add_edge(node.val, node.left.val)
            l = x - 1 / 2 ** layer
            pos[node.left.val] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            r = x + 1 / 2 ** layer
            pos[node.right.val] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    node_colors = [colors[node] for node in tree.nodes]
    
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, with_labels=True, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def array_to_heap(arr):
    if not arr:
        return None

    nodes = [Node(key) for key in arr]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]

    return nodes[0]

def dfs(node, visited=None):
    if visited is None:
        visited = []
    if node:
        visited.append(node.val)
        dfs(node.left, visited)
        dfs(node.right, visited)
    return visited

def bfs(node):
    visited = []
    queue = [node]
    while queue:
        current = queue.pop(0)
        if current:
            visited.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
    return visited

def assign_colors(traversal, color_map):
    colors = {}
    num_nodes = len(traversal)
    for i, node in enumerate(traversal):
        colors[node] = color_map((num_nodes - i - 1) / num_nodes)
    return colors

# Create a colormap that goes from dark green to light green
cmap = plt.colormaps.get_cmap('Greens')

# Example array representing a binary heap
binary_heap_array = [100, 45, 34, 10, 5, 3, 2, 4, 1]

# Convert the array into a binary heap
heap_root = array_to_heap(binary_heap_array)

# DFS Traversal
dfs_traversal = dfs(heap_root)
dfs_colors = assign_colors(dfs_traversal, cmap)

# Visualize DFS Traversal
print("DFS Traversal:", dfs_traversal)
draw_tree(heap_root, dfs_colors)

# BFS Traversal
bfs_traversal = bfs(heap_root)
bfs_colors = assign_colors(bfs_traversal, cmap)

# Visualize BFS Traversal
print("BFS Traversal:", bfs_traversal)
draw_tree(heap_root, bfs_colors)