# Siepinski-Gastket-Triangle

import matplotlib.pyplot as plt

def midpoint(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def ST_Recur(level, p1, p2, p3):
    if level == 1:
        x,y = zip(p1,p2,p3,p1)
        plt.plot(x,y,'black')
    else:
        p4, p5, p6 = midpoint(p1, p2), midpoint(p2, p3), midpoint(p1, p3)
        ST_Recur(level - 1,p1,p4,p6)
        ST_Recur(level - 1,p4,p2,p5)
        ST_Recur(level - 1,p6, p5,p3)

def DrawSierpinskiTriangle(iteration):
    p1, p2, p3 = (0, 0), (1000,2000), (2000,0)   # bottom left, top, bottom left
    ST_Recur( iteration, p1, p2, p3)

i = int(input("Enter the number of iteration: "))
num_tri = 3**(i-1) if i > 1 else 1
num_ver = (3 + sum(3**(n) for n in range(1,i))) if i > 1 else 3
print('Number of Triangles = {},Number of Vertices = {}'.format(num_tri,num_ver)) 
plt.figure()
DrawSierpinskiTriangle(i)
plt.show()
