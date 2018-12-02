# 寻找仅差一位的两个字符串
import numpy as np
def compare_two(a,b):
    a1 = [ord(x) for x in a]
    b1 = [ord(x) for x in b]
    c1 = np.array(a1)-np.array(b1)
    # print(c1)
    nzeros = np.count_nonzero(c1)
    return nzeros # 返回非零数
f = open('./input.txt',mode='r')
r = f.readlines()
for i in range(len(r)):
    for j in range(i+1,len(r)):
        result = compare_two(r[i],r[j])
        if result == 1:
            print(r[i])
            print(r[j])
