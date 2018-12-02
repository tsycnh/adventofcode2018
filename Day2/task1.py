# readlines
f = open('./input.txt',mode='r')

def check_double(l):
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            if i-1 < 0 and l[i] != l[i+2]:#最左边
                return True
            if i+2 > len(l)-1 and l[i-1] != l[i]:#最右边
                return True
            if i-1 >=0 and i+2<=len(l)-1:# 中间
                if l[i]!=l[i-1] and l[i] != l[i+2]:# right bound
                    return True
    return False
def check_triple(l):
    for i in range(len(l)-2):
        if l[i] == l[i+1] and l[i+1] == l[i+2]:
            if i-1 < 0 and l[i] != l[i+3]:#最左边
                return True
            if i+3 > len(l)-1 and l[i-1] != l[i]:#最右边
                return True
            if i-1 >=0 and i+3<=len(l)-1:# 中间
                if l[i]!=l[i-1]  and l[i] != l[i+3]:# right bound
                    return True
    return False
ds = 0
ts = 0
while True:
    r = f.readline()
    if r:
        pass
    else:
        break
    c = r[0:-1]
    d=sorted(c)
    print(d)
    d_result = check_double(d)
    t_result = check_triple(d)
    print("d:",d_result,"t:",t_result)
    if d_result:
        ds +=1
    if t_result:
        ts +=1
print(ds,ts,ds*ts)
