# graph https://medium.com/@anil.goyal0057/understanding-graph-data-structures-concepts-types-and-java-implementations-71771ea60707

# graph adjacency list and adjacency matrix 
# searching adjacency matrix (2D array), search row first and search column after that  
# graph traversal algorithm
# Depth First Search 
# Each node should only visit pme time(do dfs one time)
# Each Edge with go twice (two way)

# example of graph
#      A
#     / \
#    B---C
#   / \   \
#  D   E   F

# graph_adjancency_list = {
#     'A': ['B', 'C'],
#     'B': ['A', 'C', 'D', 'E'],
#     'C': ['A', 'B', 'F'],
#     'D': ['B'],
#     'E': ['B'],
#     'F': ['C']
# }

# # Iterate over all edges
# for node in graph_adjancency_list:
#     for neighbor in graph_adjancency_list[node]:
#         print(f"Edge: {node} -> {neighbor}")

# graph_adjancency_matrix = [
#     [0, 1, 1, 0, 0, 0],  # A
#     [1, 0, 1, 1, 1, 0],  # B
#     [1, 1, 0, 0, 0, 1],  # C
#     [0, 1, 0, 0, 0, 0],  # D
#     [0, 1, 0, 0, 0, 0],  # E
#     [0, 0, 1, 0, 0, 0]   # F
# ]

# # Iterate over all edges
# for i in range(len(graph_adjancency_matrix)):
#     for j in range(len(graph_adjancency_matrix[i])):
#         if graph_adjancency_matrix[i][j] == 1:
#             print(f"Edge: {chr(65 + i)} -> {chr(65 + j)}")

# same results for both storing emthod
# Edge: A -> B
# Edge: A -> C
# Edge: B -> A
# Edge: B -> C
# Edge: B -> D
# Edge: B -> E
# Edge: C -> A
# Edge: C -> B
# Edge: C -> F
# Edge: D -> B
# Edge: E -> B
# Edge: F -> C

#      A
#     / \
#    B   C
#   / \   \
#  D   E   F


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in reversed(graph[node]):  # Reverse to match recursive order
                stack.append(neighbor)

# dfs_iterative(graph, 'A')  # Output: A B D E C F

# https://leetcode.com/problems/number-of-islands/description/
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:

# Input: grid = [
#  ["1","1","0","0","0"],
#  ["1","1","0","0","0"],
#  ["0","0","1","0","0"],
#  ["0","0","0","1","1"]
# ]
# Output: 3

def find_island(grid):
    if not grid or not grid[0]:
        print(0)
        return 0
    n, m = len(grid), len(grid[0])
    count = 0 
    # array version: [[-1, 0], [1, 0], [0, -1], [0, 1]]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right :  list of tuples.
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":



def numIslands(grid):
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                stack = [(i, j)]
                grid[i][j] = '0'  # Mark as visited
                while stack:
                    x, y = stack.pop()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                            grid[nx][ny] = '0'  # Mark as visited
                            stack.append((nx, ny))
    print(count)
    return count

numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])



    
