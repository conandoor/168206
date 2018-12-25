global avewait_time_at_bar 
avewait_time_at_bar = 0
global avewait_time_at_barbecue
avewait_time_at_barbecue= 0
class Consumer(object):
    def __init__(self,id):
        self.id = id
        self.tasks = []
        self.time = 0
        self.time_at_grill = 0
        self.roasting_time = 0
    def complete_task(self,task):
        self.tasks.append(task)
def Restaurant(people):
    index = 0
    for i in range(0,len(people)):
        queues[index].append(people[i])
        index += 1
        if index >=20 :
            index = 0
def Bar():
    sum = 0
    for i in range(0,20):
            sum += len(queues[i])
    if sum <= 0:
        return 0 
    a_queue = []
    for i in range(0,20):
        if len(queues[i]) <= 0:

            a_queue.append(-1)

            continue

        for j in range(len(queues[i])):

            queues[i][j].time += 10

        consumer = queues[i].pop(0)

        consumer.tasks.append(i)

        if len(consumer.tasks) >= 5:

            ready_roast.append(consumer)

            a_queue.append(-1)
            continue
        a_queue.append(consumer)

    for index in range(0,20):

        if a_queue[index] == -1:

            continue

        else:  
            queues[(index+1)%20].append(a_queue[index])

    return sum 

def barbecue():

    global avewait_time_at_bar

    global avewait_time_at_barbecue
    amount = 0

    if len(ready_roast) <= 0:

        return

    elif len(ready_roast) <= 8:

        for i in range(0,len(ready_roast)):

            ready_roast[i].roasting_time += 10

            if ready_roast[i].roasting_time >= 180:
                amount += 1
                continue
    else:
        for i in range(0,8):

           ready_roast[i].roasting_time += 10

            if ready_roast[i].roasting_time >= 180:

                amount += 1

                continue

        for i in range(8,len(ready_roast)):

            ready_roast[i].time_at_grill += 10


    if amount <= 0:

        return

    for i in range(0,amount):
        c_person = ready_roast.pop(0)
        avewait_time_at_bar = avewait_time_at_bar + c_person.time - 50
        avewait_time_at_barbecue+= c_person.time_at_grill
if __name__ == '__main__':
    total = int(input("请输入总人数："))
    interval = int(input("请输入时间间隔：")) 
    Time = 0 
    people = []    
    for i in range(0,total):
        person = Consumer(i)   

        people.append(person) 
    global queues  
    for i in range(0,20):
        queues[i] = []

    global ready_roast 

    ready_roast = []

    index = 0

    sum_at_bar = 0

   flag = True
    while True:
        if flag and interval == 0:
          index = total;
            Restaurant(people[0:])
            flag = False
        elif interval!= 0:
            if Time % interval == 0:
                if index < total:
                    Restaurant(people[index:index+1])
                    index += 1
        Time += 10
        print("time  ",Time)
        sum_at_bar = Bar()
        barbecue()
        if index >= total and sum_at_bar <= 0 and  len(ready_roast) <= 0:
           break
    print("吧台平均等待时间为：",avewait_time_at_bar/total)
    print("烤架平均等待时间为：",avewait_time_at_barbecue/total)
