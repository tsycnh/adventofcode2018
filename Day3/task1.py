import numpy as np
# 求重叠区域面积
f = open('./input.txt',mode='r')
canvas = np.zeros(shape=[2000,2000])
# canvas-=1
def get_data(r):
    pos_a = r.find('@')
    pos_b = r.find(',')
    wd_a = r.find(":")
    wd_b = r.find("x")
    end = r.find('\n')

    x = int(r[pos_a+2:pos_b])
    y = int(r[pos_b+1:wd_a])
    w = int(r[wd_a+2:wd_b])
    h = int(r[wd_b+1:end])
    return x,y,w,h

while True:
    r = f.readline()
    if r:
        pass
    else:
        break
    x,y,w,h = get_data(r)
    canvas[y:y+h,x:x+w] += 1

unique,counts = np.unique(canvas,return_counts=True)
print(dict(zip(unique,counts)))
result = 0
for i in range(2,len(counts)):
    result+=counts[i]
print(result)