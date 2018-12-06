f = open("input.txt",mode='r')
data = f.readline()[:-1]
finished_index = 0#表示已经完全反应的字符串长度
last_len = -1
while True:
    for i in range(finished_index,len(data)-1):
        # print(i)
        letter1 = ord(data[i])
        letter2 = ord(data[i+1])
        c=abs(letter1-letter2)
        if c == 32:
            front_half = data[:i]
            last_half = data[i+2:]
            data = front_half+last_half
            if finished_index < 0:
                finished_index = 0
            else:
                finished_index = i-1
            break
    current_len = len(data)
    print("current len",current_len)
    if (current_len == last_len):
        print("final len",current_len)
        break
    else:
        last_len = current_len

pass