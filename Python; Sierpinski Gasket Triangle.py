import timeit
import matplotlib.pyplot as plt

def midpoint(point_1,point_2):
    return ((point_1[0]+point_2[0])/2,(point_1[1]+point_2[1])/2)

def draw(iteration, left_node,top_node,  right_node):
    if iteration == 1:
        x,y = zip(left_node, top_node,  right_node,left_node)
        plt.plot(x,y, 'black')
    else:
        left_top_mid, top_right_mid, left_right_mid = midpoint(left_node,top_node), midpoint(top_node, right_node), midpoint(left_node, right_node)
        draw(iteration - 1,left_node,left_top_mid,left_right_mid)
        draw(iteration - 1,left_top_mid,top_node,top_right_mid)
        draw(iteration - 1,left_right_mid, top_right_mid,right_node)

def SGT(iteration):
    left_node, top_node,  right_node = (0, 0), (1000,2000), (2000,0)   # bottom left, top, bottom left
    draw( iteration, left_node, top_node,  right_node)

level = int(input("Enter the number of iteration: "))
i = level + 1
start = timeit.timeit()
num_tri = 3**(i-1) if i > 1 else 1
num_ver = (3 + sum(3**(n) for n in range(1,i))) if i > 1 else 3
print('Number of Triangles = {},Number of Nodes = {}'.format(num_tri,num_ver)) 
plt.figure()
SGT(i)
end = timeit.timeit()
print("Time to run code = {}".format(end-start))
plt.show()