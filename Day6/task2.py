import numpy as np

f = open('input.txt',mode='r')
canvas_width = 1000
data = f.readlines()
class Point():
    def __init__(self,ID,x,y):
        self.ID = ID
        self.x = x
        self.y = y
        self.infinite = False
        self.area = 0
all_points = []
for i in range(len(data)):
    d = data[i]
    x,y = d.split(',')
    y = y[1:-1]
    p = Point(i,int(x),int(y))
    all_points.append(p)
canvas = np.zeros(shape=(canvas_width,canvas_width))
def calc_M_distance(pointA,pointB):
    return abs(pointA.x - pointB.x) + abs(pointA.y - pointB.y)
for i in range(0,canvas_width):
    print('i:', i)
    for j in range(0,canvas_width):
        tmpPoint = Point(-1,j,i)#i为行，j为列。
        distances = []
        total_distance = 0
        for p in all_points:
            distance = calc_M_distance(tmpPoint,p)
            total_distance += distance
        if total_distance < 10000:
            canvas[i,j] = 1

print(np.sum(canvas))