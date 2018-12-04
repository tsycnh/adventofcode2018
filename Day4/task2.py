import datetime,time
import numpy as np
f = open('input.txt',mode='r')
data = f.readlines()
order_data = []

class D():
    def __init__(self,time,data):
        self.time = time
        self.data = data
def parse_line(d):
    date_start = d.find('[')
    date_end = d.find(']')
    raw_date = d[date_start+1:date_end]
    dt = datetime.datetime.strptime(raw_date,"%Y-%m-%d %H:%M")
    ts = dt.timestamp()
    d = D(ts,d)
    order_data.append(d)
for i in range(len(data)):
    parse_line(data[i])

order_data.sort(key=lambda x:x.time)
#完成排序

class E():
    def __init__(self,date,ID,sleep_info):
        self.date = date
        self.ID = ID
        self.sleep_info = sleep_info
alldays = []
tmpday = E(0,0,np.zeros(shape=(60,)))
last_time = None
for line in order_data:
    current_date = line.data[1:11]
    current_time = int(line.data[15:17])
    if "begins" in line.data:
        if tmpday.ID != 0:
            alldays.append(tmpday)#推入上一天信息
        tmpday = E(0, 0, np.zeros(shape=(60,)))
        #开始巡逻
        guard_ID = line.data.split("#")[1].split(" ")[0]
        tmpday.date = current_date
        tmpday.ID = int(guard_ID)
        last_time = 0#从0点开始

    if "asleep" in line.data:
        tmpday.sleep_info[last_time:current_time] = 0
        last_time = current_time
    if "wakes" in line.data:
        tmpday.sleep_info[last_time:current_time] = 1
        last_time = current_time
# 睡眠信息统计完毕

ID_info = []
sleep_info = []

for day in alldays:
    if day.ID not in ID_info:
        ID_info.append(day.ID)
        sleep_info.append(day.sleep_info)
    else:
        ID_index = ID_info.index(day.ID)
        update = np.row_stack((sleep_info[ID_index],day.sleep_info))
        sleep_info[ID_index] = update

god_sleepy_minute = 0# 在第几分钟
god_sleepy_times = 0#睡了几次
god_sleepy_ID = 0#ID多少

for i in range(len(ID_info)):
    result = np.sum(sleep_info[i], axis=0)#在每一分钟睡了几次
    current_sleep_times = int(result.max())#最能睡的一分钟睡了几次
    current_sleepy_minute = int(result.argmax())#在哪一分钟睡的最多
    # print(current_sleep_times,current_sleepy_minute)

    if current_sleep_times > god_sleepy_times:
        god_sleepy_times = current_sleep_times
        god_sleepy_ID = ID_info[i]
        god_sleepy_minute = current_sleepy_minute

print(god_sleepy_ID, god_sleepy_minute, god_sleepy_times)
print(god_sleepy_ID * god_sleepy_minute)
pass