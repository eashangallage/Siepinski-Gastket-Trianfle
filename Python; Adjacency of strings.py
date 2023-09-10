import matplotlib.pyplot as plt
import numpy as np

cache1 = {}
cache2 = {}

def plot(main, left_node,top_node,right_node):
    x,y = zip(left_node, top_node, right_node,left_node) # separate the x and y values of the points
    if main:
        plt.plot(x,y,'black') # plot the data in a graph
    else:
        plt.plot(x,y,'red') # plot the data in a graph
    
def final_plot(n,node):
    x,y = zip(node) # separate the x and y values of the points
    plt.scatter(x,y) # plot the data in a graph
    cache2[n] = node

def midpoint(point_1,point_2):
    return ((point_1[0]+point_2[0])/2,(point_1[1]+point_2[1])/2)

def select_triangle(main, n,current_triangle,previous_triangle, left_node,top_node,  right_node):
    if len(current_triangle) == 1: 
        final_node = current_triangle[0]
        y_down = left_node[1]-(top_node[1]-left_node[1])
        if final_node == 0: 
            x_right = top_node[0] + (right_node[0]-left_node[0])
            x_left = top_node[0] - (right_node[0]-left_node[0])
            if previous_triangle[0] == 1:
                final_plot(n,top_node)
                cache1[n] = [left_node,top_node,right_node,(x_right,top_node[1])]
            elif previous_triangle[0] == 2:
                final_plot(n,top_node)
                cache1[n] = [left_node,top_node,right_node,(x_left,top_node[1])]
            else:
                final_plot(n,top_node)
                cache1[n] = [left_node,top_node,right_node]
        elif final_node == 1:
            x_right = top_node[0]
            x_left = left_node[0]-(top_node[0]-left_node[0])
            if previous_triangle[0] == 1 or previous_triangle[0] == 0: 
                final_plot(n,left_node)
                cache1[n] = [left_node,top_node,right_node,(x_left,y_down),(x_right,y_down)]
            else:
                final_plot(n,left_node)
                cache1[n] = [left_node,top_node,right_node,(x_left,left_node[1])]
        elif final_node == 2:
            x_right = right_node[0]+(right_node[0]-top_node[0])
            x_left = top_node[0]
            if previous_triangle[0] == 2 or previous_triangle[0] == 0:
                final_plot(n,right_node)
                cache1[n] = [left_node,top_node,right_node,(x_left,y_down),(x_right,y_down)]
            else: 
                final_plot(n,right_node)
                cache1[n] = [left_node,top_node,right_node,(x_right,right_node[1])]
        return -1
    
    triangle = current_triangle[0]  #001    current_triangle[0]= 0
    previous_triangle = list.copy(current_triangle)
    current_triangle.pop(0)

    left_top_mid, top_right_mid, left_right_mid = midpoint(left_node,top_node), midpoint(top_node,right_node), midpoint(left_node,right_node)

    if triangle == 0:
        plot(main,left_top_mid,top_node,top_right_mid)
        select_triangle(main,n,current_triangle,previous_triangle,left_top_mid,top_node,top_right_mid)
    
    elif triangle == 1:
        plot(main,left_node,left_top_mid,left_right_mid)
        select_triangle(main,n,current_triangle,previous_triangle,left_node,left_top_mid,left_right_mid)
        
    elif triangle == 2:
        plot(main,left_right_mid,top_right_mid,right_node)
        select_triangle(main,n,current_triangle,previous_triangle,left_right_mid,top_right_mid,right_node)


def draw_main(main,iteration, left_node,top_node,  right_node):
    if iteration == 1:
        plot(main, left_node,top_node,right_node)
    else:
        left_top_mid, top_right_mid, left_right_mid = midpoint(left_node,top_node), midpoint(top_node, right_node), midpoint(left_node, right_node)
        draw_main(main,iteration - 1,left_node,left_top_mid,left_right_mid)
        draw_main(main,iteration - 1,left_top_mid,top_node,top_right_mid)
        draw_main(main,iteration - 1,left_right_mid, top_right_mid,right_node)


def check_node():
    x = list(cache2.values())
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i] == x[j]: print('\nnode of string {} and node of string {} are equal to {}'.format(i+1,j+1,x[i]))
                

def check_adjacency_nodes():
    x, y = list(cache1.values()), list(cache2.values())
    for i in range(len(x)):
        for j in range(len(y)):
            if j == i: a_matrix[i,j] ,0
            elif y[j] in x[i]: a_matrix[i,j], a_matrix[j,i] = 1,1
                

def main_sgt(n,left_node,top_node,  right_node):
    left_node, top_node,  right_node = (0, 0), (1000,2000), (2000,0)   # left, top, right (nodes of the outter traingle)
    main = True
    draw_main(main,n,left_node,top_node,right_node)

if __name__ == "__main__":
    number_of_points = int(input("Enter number of points: \n"))

    plt.figure()

    left_node, top_node,  right_node = (0, 0), (1000,2000), (2000,0)
    a_matrix = np.zeros((number_of_points,number_of_points),dtype=int)
    main = False
    for n in range(1,number_of_points + 1):
        str = input("Enter required string: ") 
        triangles = [int(value) for value in str]
        if n == 1:
            main_sgt(len(triangles),left_node,top_node,  right_node)
        select_triangle(main,n, triangles,triangles, left_node,top_node,  right_node)

    if n > 1: check_node(), check_adjacency_nodes()
    print("String and its adjacent nodes to check")
    print("\nEach node and their adjacent vertices:")
    print(cache1)
    print("\nStrings of nodes entered:")
    print(cache2)
    print("\nAdjacency Matrix for the Nodes")
    print(a_matrix)
    plt.show()