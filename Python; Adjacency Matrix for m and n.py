"""
'm' is the outter level SGT and 'n' is the inner level SGT.
Input: m,n are non-zero positive integers; m < n
Output: Matrix: "adjacency_matrix matrix" for the combination of m and n
"""


import numpy as np
import matplotlib.pyplot as plt

cache_triangles_m = {}
cache_nodes_n = {}
list_nodes = []

def midpoint(point_1,point_2):
    return ((point_1[0]+point_2[0])/2,(point_1[1]+point_2[1])/2)

def draw_m(level, left_node,top_node,  right_node, color):
    if level == 1: # if the level value is 1 draw the triangle
        x,y = zip(left_node, top_node, right_node,left_node) # separate the x and y values of the points
        plt.plot(x,y,color) # plot the data in a graph
        cache_triangles_m[len(cache_triangles_m.values())+1] = left_node, top_node, right_node
            
    else:
        left_top_mid, top_right_mid, left_right_mid = midpoint(left_node,top_node), midpoint(top_node,right_node), midpoint(left_node,right_node)

        draw_m(level - 1, left_node, left_top_mid, left_right_mid, color) # draw the left traingle of the level
        draw_m(level - 1, left_top_mid, top_node, top_right_mid, color) # draw the top traingle of the level
        draw_m(level - 1, left_right_mid, top_right_mid, right_node, color) # draw the right traingle of the level

def draw_n(level, left_node,top_node,  right_node, color, i):
    if level == 1: # if the level value is 1 draw the triangle
        x,y = zip(left_node, top_node, right_node,left_node) # separate the x and y values of the points
        plt.plot(x,y,color) # plot the data in a graph

        if i not in cache_nodes_n: cache_nodes_n[i] = [left_node, top_node, right_node]
        else:
            if left_node not in cache_nodes_n[i]: cache_nodes_n[i].append(left_node)
            if top_node not in cache_nodes_n[i]: cache_nodes_n[i].append(top_node)
            if right_node not in cache_nodes_n[i]: cache_nodes_n[i].append(right_node)

    else:
        left_top_mid, top_right_mid, left_right_mid = midpoint(left_node,top_node), midpoint(top_node,right_node), midpoint(left_node,right_node)

        draw_n(level - 1, left_node, left_top_mid, left_right_mid, color, i) # draw the left traingle of the level
        draw_n(level - 1, left_top_mid, top_node, top_right_mid, color, i) # draw the top traingle of the level
        draw_n(level - 1, left_right_mid, top_right_mid, right_node, color, i) # draw the right traingle of the level

def adjacency_matrix(n):
    a = np.zeros((n,n), dtype=int)
    # go over every vertex in cache_nodes_n and add them to a[1][0] to a[1][-1]
    list_nodes = cache_nodes_n[1].copy()
    for i in range(2,len(cache_nodes_n.values())+1):
        for j in range(len(cache_nodes_n[i])):
            if cache_nodes_n[i][j] not in list_nodes: list_nodes.append(cache_nodes_n[i][j]) 
    #print(list_nodes) [(750.0, 1500.0), (1000, 2000), (1250.0, 1500.0), (500.0, 1000.0), (1000.0, 1000.0), (1500.0, 1000.0), (250.0, 500.0), (750.0, 500.0), (0, 0), (500.0, 0.0), (1000.0, 0.0), (1250.0, 500.0), (1750.0, 500.0), (1500.0, 0.0), (2000, 0)]
    
    for i in range(len(list_nodes)):
        for j in range(len(list_nodes)):
            if list_nodes[i]==list_nodes[j]: continue
            for values in cache_nodes_n.values():
                if list_nodes[i] in values: 
                    if list_nodes[j] in values:
                        a[i][j] = 1
                        break
    print(a)


if __name__== "__main__":

    n = int(input("Enter value n: "))
    m = int(input("Enter value m(0-{}): ".format(n-1)))

    left_node, top_node,  right_node = (0, 0), (1000,2000), (2000,0)

    plt.figure()

    #draw(n+1, left_node, top_node,  right_node, 'green')
    draw_m(m+1, left_node, top_node,  right_node, 'red')

    for i in range(len(cache_triangles_m.values())): 
        #print(cache_triangles_m[i+1][0], cache_triangles_m[i+1][1],  cache_triangles_m[i+1][2])
        draw_n(n-m+1, cache_triangles_m[i+1][0], cache_triangles_m[i+1][1],  cache_triangles_m[i+1][2], 'black', i+1)

    print("\nm")
    i = m + 1
    num_tri_m = 3**(i-1) if i > 1 else 1
    num_ver_m = (3 + sum(3**(n) for n in range(1,i))) if i > 1 else 3
    print('Number of Triangles = {},Number of Nodes = {}'.format(num_tri_m,num_ver_m))

    print("\nn")
    i = n + 1 
    num_tri_n = 3**(i-1) if i > 1 else 1
    num_ver_n = (3 + sum(3**(n) for n in range(1,i))) if i > 1 else 3
    print('Number of Triangles = {},Number of Nodes = {}'.format(num_tri_n,num_ver_n))

    #print(cache_triangles_m)
    #[print(values) for values in cache_nodes_n.values()]

    # making the adjacency matrix
    # make the matrix dimensions num_ver_n + 1 for both columns and rows, and make the a[1][0] to a[-1][0] the vertice x,y values do the same for a[0][1] to a[0][-1]
    # make sure that the vertices aren't repeated
    # Next starting from a[i][0] and a[0][j] if they are both in the same dictionary value of cache_nodes_n, if so make a[i][j] = 1 else 0

    adjacency_matrix(num_ver_n)

    plt.show()