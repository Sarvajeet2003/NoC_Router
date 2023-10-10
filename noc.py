from Router import Router

def xy(flit_details,curr):

    src = int(flit_details[0])
    des = int(flit_details[1])
    flit = flit_details[2]

    print(f"{src} + {des}")

    i_curr = curr // 3
    j_curr = curr % 3

    i_src = src // 3
    j_src = src % 3

    i_des = des // 3
    j_des = des % 3

    if(j_des > j_src and j_curr + 1 < 3):
        i_next = i_curr
        j_next = j_curr + 1
    elif(j_des > j_src and j_curr + 1 == 3):
        i_next = i_curr + 1
        j_next = j_curr
    elif(j_des < j_src and j_curr - 1 >= 0 ):
        i_next = i_curr
        j_next = j_curr - 1
    elif(j_des < j_src and j_curr - 1 < 0):
        i_next = i_curr - 1
        j_next = j_curr
    else:
        print("yoyo")

    next_id = 3 * i_next + j_next
    return next_id

def all_empty(all_routers):
    i = 0
    while(i < len(all_routers)):
        if(not all_routers[i].isempty()):
            return False
        
        i += 1

    return True

with open('traffic.txt','r') as file:
    line = file.readlines()
    eachline = []
    for i in range(0,len(line)):
        eachline.append(line[i].split())

    eachline2 = []
    for i in range(0,len(eachline)):
        temp = []
        for j in range(0,len(eachline[i])):
            temp.append(eachline[i][j])
        eachline2.append(temp)

with open('delays.txt','r') as file1:
    line1 = file1.readline()
    line1 = line1.split()
    line2 = []
    for i in range(0,len(line1)):
        line2.append(int(line1[i]))

traffic_file = eachline2
delay_file = line2

buffer_delay = delay_file[0]
sa_delay = delay_file[1]
xbar_delay = delay_file[2]

#print("file reading done")

all_routers = {i : Router(i,buffer_delay,sa_delay,xbar_delay) for i in range(0,9)}

#print("Router Creation Done")

period = max(buffer_delay,sa_delay,xbar_delay)
clock = 1 #defining the clock

total = 0
for i in range(0,len(traffic_file)): #traversing traffic file

    clk_cycle = int(traffic_file[i][0])
    src = int(traffic_file[i][1])
    des = int(traffic_file[i][2])
    flit = traffic_file[i][3]

    flit_details = [src,des,flit]

    i = 8
    while(i >= 0):
        r = all_routers[i]

        if(i != src):
            if(not r.isempty()):
                next_r = xy(flit_details,i)
                r.update(all_routers[next_r])

        else:
            next_r = xy(flit_details,i)
            r.update(all_routers[next_r])
            r.inject(flit)

        print(f"At clock cycle : {clock} = {all_routers[i]}")    
        i -= 1

    clock += 1
    total += period

while(not all_empty(all_routers)):
    i = 8
    while(i >= 0):
        r = all_routers[i]
        if(not r.isempty()):
            flit_details = r.getflit()
            next_r = xy(flit_details,i)
            r.update(all_routers[next_r])
        
        print(f"At clock cycle : {clock} = {all_routers[i]}") 
        i -= 1

    clock += 1
    total += period

    # mind fucked from here
print(f"Total Time Taken = {total} & Clock Frequency = {1/period}")

