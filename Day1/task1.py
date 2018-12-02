f = open('./task1input.txt',mode='r')
all = 0
while True:
    r = f.readline()
    if r:
        pass
    else:
        break
    num = int(r[1:-1])
    if r[0]=="-":
        num = -num
    all += num
    # print(r)

print(all)