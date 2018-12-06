import numpy as np

f = open('input.txt',mode='r')
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
canvas = np.zeros(shape=(1000,1000))
def calc_M_distance(pointA,pointB):
    return abs(pointA.x - pointB.x) + abs(pointA.y - pointB.y)
for i in range(0,1000):
    print('i:', i)
    for j in range(0,1000):
        tmpPoint = Point(-1,j,i)#i为行，j为列。
        distances = []
        for p in all_points:
            distance = calc_M_distance(tmpPoint,p)
            distances.append({'ID':p.ID,'distance':distance})
        distances.sort(key=lambda x:x['distance'])

        if i == 0 or j==0:#靠边的点,确认无限
            for k in range(len(all_points)):
                if all_points[k].ID == distances[0]['ID']:
                    all_points[k].infinite = True#无限点
        if distances[0]['distance'] == distances[1]['distance']:
            pass#中立点，0
        else:
            canvas[i,j] = distances[0]['ID']
            for k in range(len(all_points)):
                if all_points[k].ID == distances[0]['ID']:
                    all_points[k].area += 1

largest_area = 0

for p in all_points:
    print(p.ID,p.area,p.infinite)
    if p.infinite == False:
        if p.area > largest_area:
            largest_area = p.area
print(largest_area+1)


