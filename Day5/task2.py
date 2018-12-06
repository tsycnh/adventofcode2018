f = open("input.txt",mode='r')
data = f.readline()[:-1]
def react(data):
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
            return current_len
        else:
            last_len = current_len

def remove_letter(data,letter):
    finished_index = 0#表示已经完全反应的字符串长度
    last_len = -1
    while True:
        for i in range(finished_index,len(data)):

            if data[i]==letter:
                front_half = data[:i]
                last_half = data[i+1:]
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
            return data
        else:
            last_len = current_len

winner_letter =""
winner_length = 1e10
for i in range(65,90+1):
    lower_letter = chr(i)
    upper_letter = chr(i+32)
    dataA = remove_letter(data,lower_letter)
    dataB = remove_letter(dataA,upper_letter)
    reaction_len = react(dataB)
    if reaction_len < winner_length:
        winner_length = reaction_len
        winner_letter = lower_letter
print(winner_letter,winner_length)
pass