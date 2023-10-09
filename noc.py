from Router import Router

def xy(curr_id,src,des):
    curr = curr_id

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

    next_id = 3 * i_next + j_next
    return next_id

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

clock = 1 #defining the clock

for i in range(0,len(traffic_file)): #traversing traffic file

    clk_cycle = int(traffic_file[i][0])
    src = int(traffic_file[i][1])
    des = int(traffic_file[i][2])
    flit = traffic_file[i][3]

    #mind fucked from here

    next_id = xy(i,src,des)

    all_routers[i].update(next_id,flit)


    flit_type = flit[-2::]
    if(flit_type == '00'):
        print("Header")
    elif(flit_type == '01'):
        print("Body")
    elif(flit_type == '10'):
        print("Tail")

    
    '''flit_transfer = False
    while(flit_transfer != True):
        if(flit_type == 'tail'):
            clock += 1'''
    








