# 找到第一个重复出现的频率
f = open('./task1input.txt',mode='r')
all = 0
frequency_list = []
for i in range(1000000):
    print("loop",i)
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
        if all in frequency_list:
            print("duplicated frequency:",all)
            exit()
        # if all == 100:
        #     print("100")
        frequency_list.append(all)
    f = open('./task1input.txt', mode='r')
