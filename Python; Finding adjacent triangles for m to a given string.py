from operator import le
import matplotlib.pyplot as plt
import sys

cache_nodes_n = {}
cache_nodes_m = {}
cache_neighbours = {}
cache_neighbour_strings = {}

def midpoint(point_1,point_2):
    return ((point_1[0]+point_2[0])/2,(point_1[1]+point_2[1])/2)

def draw_n(level, left_node,top_node,  right_node):
    if level == 1: # if the level value is 1 draw the triangle
        x,y = zip(left_node, top_node, right_node,left_node) # separate the x and y values of the points
        plt.plot(x,y,'black') # plot the data in a graph
        if left_node not in cache_nodes_n.values(): cache_nodes_n[len(cache_nodes_n.values())+1] = left_node
        if top_node not in cache_nodes_n.values(): cache_nodes_n[len(cache_nodes_n.values())+1] = top_node
        if right_node not in cache_nodes_n.values(): cache_nodes_n[len(cache_nodes_n.values())+1] = right_node
    else:
        left_top_mid, top_right_mid, left_right_mid = midpoint(left_node,top_node), midpoint(top_node,right_node), midpoint(left_node,right_node)

        draw_n(level - 1, left_node, left_top_mid, left_right_mid) # draw the left traingle of the level
        draw_n(level - 1, left_top_mid, top_node, top_right_mid) # draw the top traingle of the level
        draw_n(level - 1, left_right_mid, top_right_mid, right_node) # draw the right traingle of the level

def draw(address, left_node,top_node,  right_node, main):
        if not address:
            x,y = zip(left_node, top_node, right_node,left_node) # separate the x and y values of the points
            if main: 
                plt.plot(x,y,'red') # plot the data in a graph
                if left_node not in cache_nodes_m.values(): cache_nodes_m[1] = left_node
                if top_node not in cache_nodes_m.values(): cache_nodes_m[0] = top_node
                if right_node not in cache_nodes_m.values(): cache_nodes_m[2] = right_node
            else: plt.plot(x,y,'green') # plot the data in a graph
            return -1
        triangle = address[0]
        address.pop(0)

        left_top_mid, top_right_mid, left_right_mid = midpoint(left_node,top_node), midpoint(top_node,right_node), midpoint(left_node,right_node)

        if triangle == 0:
            draw(address,left_top_mid,top_node,top_right_mid, main)
        
        elif triangle == 1:
            draw(address,left_node,left_top_mid,left_right_mid, main)
            
        elif triangle == 2:
            draw(address,left_right_mid,top_right_mid,right_node, main)

def nodes_adjacent_triangles(address):
    cm = cache_nodes_m.copy()
    cn = cache_neighbours
    cnn = cache_nodes_n
    x_diff = cm[2][0] - cm[1][0]
    y_diff = cm[0][1] - cm[1][1]
    y_top = cm[0][1] + y_diff
    y_bottom = cm[1][1] - y_diff
    x_right_full = cm[2][0] + x_diff
    x_right_half = cm[0][0] + x_diff
    x_left_full = cm[1][0] - x_diff
    x_left_half = cm[0][0] - x_diff

    if address[-1] == 0:
        top_left = (cm[1][0],cm[0][1] + (cm[0][1]-cm[1][1]))
        if top_left in cnn.values(): cn[0] = (cm[1][0],y_top),(x_left_half,cm[0][1]),cm[0]
        else: cn[0] = (cm[2][0],y_top),cm[0],(x_right_half,cm[0][1])
        cn[1] = cm[1],(x_left_half,y_bottom),(cm[0][0],y_bottom)
        cn[2] = cm[2],(cm[0][0],y_bottom),(x_right_half,y_bottom)

    elif address[-1] == 1:
        direct_left = (x_left_full,cm[1][1])
        cn[0] = (cm[2][0],y_top),cm[0],(x_right_half,cm[0][1])
        if direct_left in cnn.values(): cn[1] = (x_left_half,cm[0][1]),direct_left,cm[1] 
        else: cn[1] = cm[1],(x_left_half,y_bottom),(cm[0][0],y_bottom)
        cn[2] = (x_right_half,cm[0][1]), cm[2],(x_right_full,cm[2][1])

    else:
        direct_right = (x_right_full,cm[2][1])
        cn[0] = (cm[1][0],y_top), (x_left_half,cm[0][1]),cm[0]
        cn[1] = (x_left_half,cm[0][1]), (x_left_full,cm[1][1]),cm[1]
        if (x_right_full,cm[2][1]) in cnn.values(): cn[2] = (x_right_half,cm[0][1]),cm[2],(x_right_full,cm[2][0])
        else: cn[2] = cm[2],(cm[0][0],y_bottom),(x_right_half,y_bottom)

def neighbour_string(length,top,left,right,neighbour_string_list):
    nbl = neighbour_string_list
    cnn = cache_nodes_n
    if len(nbl) == length: 
        cache_neighbour_strings[len(cache_neighbour_strings)] = nbl
        return -1
    if left not in cnn.values() or right not in cnn.values():
        return -1

    """plt.scatter(top[0],top[1])
    plt.scatter(left[0],left[1])
    plt.scatter(right[0],right[1])"""

    x_diff = right[0] - left[0]
    y_diff = top[1] - right[1]
    y_top = top[1] + y_diff
    y_bottom = left[1] - y_diff
    x_right_half = top[0] + x_diff
    x_right_full = right[0] + x_diff
    x_left_half = top[0] - x_diff
    x_left_full = left[0] - x_diff


    if (x_right_half,right[1]) in cnn.values() and (left[0],top[1]) not in cnn.values():
        nbl.insert(0,1)
        new_top = (right[0],y_top)
        new_right = (x_right_full,right[1])
        neighbour_string(length,new_top,left,new_right,nbl)

    elif (x_left_half,left[1]) not in cnn.values() and (x_right_half,right[1]) not in cnn.values(): 
        nbl.insert(0,0)
        new_left = (x_left_half,y_bottom)
        new_right = (x_right_half,y_bottom)
        neighbour_string(length,top,new_left,new_right,nbl)

    if (x_left_half,left[1]) in cnn.values() and (right[0],top[1]) not in cnn.values(): 
        nbl.insert(0,2)
        new_top = (left[0],y_top)
        new_left = (x_left_full,left[1])
        neighbour_string(length,new_top,new_left,right,nbl)


if __name__ == "__main__":
    plt.figure()
    node_address = input("Enter address of node: ")
    node_address_list = node_address_list = [int(value) for value in node_address]
    n_level = len(node_address_list)
    left_node, top_node,  right_node = (0, 0), (1000,2000), (2000,0)
    draw_n(n_level, left_node,top_node,  right_node)
    #print(cache_nodes_n)
    
    i = n_level
    num_tri = 3**(i-1) if i > 1 else 1
    num_ver = (3 + sum(3**(n) for n in range(1,i))) if i > 1 else 3
    #print('Number of Triangles = {},Number of Nodes = {}'.format(num_tri,num_ver)) 

    m_level = m_level = int(input("Enter level m between 1 and {}: ".format(n_level-2)))
    m_address = [node_address_list[value] for value in range(m_level)]
    draw(m_address.copy(), left_node,top_node,  right_node, True)
    print(cache_nodes_m)
    
    # findding strings of adjacent triangles to m
    # going to backtrack to find the strings
    # before that I have to find the nodes of the adjacent triangles 
    nodes_adjacent_triangles(m_address.copy())
    print(cache_neighbours)
    neighbour_string_list = []
    [neighbour_string(len(m_address),values[0],values[1],values[2],neighbour_string_list.copy()) for values in cache_neighbours.values()]
    print(cache_neighbour_strings)
    [draw(values, left_node,top_node,  right_node, False) for values in cache_neighbour_strings.values()]
    
    plt.show()