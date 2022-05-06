import matplotlib.pyplot as plt

def draw(iteration, left_node,top_node,  right_node):
    if iteration == 1: # if the iteration value is 1 draw the triangle
        x,y = zip(left_node, top_node, right_node,left_node) # separate the x and y values of the points
        plt.plot(x,y,'black') # plot the data in a graph
    else:
        left_top_mid = ((left_node[0] + top_node[0])/2, (left_node[1] + top_node[1])/2) # finding the mid point of the left and top node
        top_right_mid = ((top_node[0] + right_node[0])/2, (top_node[1] + right_node[1])/2) # finding the mid point of the top and right node
        left_right_mid = ((left_node[0] + right_node[0])/2, (left_node[1] + right_node[1])/2) # finding the mid point of the left and right node

        draw(iteration - 1, left_node, left_top_mid, left_right_mid) # draw the left traingle of the iteration
        draw(iteration - 1, left_top_mid, top_node, top_right_mid) # draw the top traingle of the iteration
        draw(iteration - 1, left_right_mid, top_right_mid, right_node) # draw the right traingle of the iteration

if __name__ == "__main__":
    i = int(input("Enter the number of iteration: ")) # iteration value
    num_tri = 3**(i-1) if i > 1 else 1 # calculate the number of triangles
    num_ver = (3 + sum(3**(n) for n in range(1,i))) if i > 1 else 3
    print('Number of Triangles = {},Number of Nodes = {}'.format(num_tri,num_ver)) 
    plt.figure() # initiate the plot function
    left_node, top_node,  right_node = (0, 0), (1000,2000), (2000,0)   # left, top, right (nodes of the outter traingle)
    draw( i, left_node, top_node,  right_node) # draw the Sierpinski Triangle
    plt.show() # show the plotted graph
