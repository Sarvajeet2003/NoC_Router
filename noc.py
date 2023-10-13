class Router:
    def __init__(self, router_id):
        self.router_id = router_id
        self.input_buffer = None
        self.crossbar = None
        self.switch_allocator = None

    def isempty(self):
        if((self.input_buffer == None) and (self.crossbar== None) and (self.switch_allocator == None)):
            return True
        return False

    def __str__(self):
        s = ""
        s += f"Router ID : {self.router_id} \n"
        if(self.input_buffer != None):
            s += f"Input Buffer Value : {self.input_buffer[2]} \n "
        if(self.input_buffer == None):
            s += f"Input Buffer Value : None \n"
        if(self.switch_allocator != None):
            s += f"Switch Allocator Value : {self.switch_allocator[2]} \n "
        if(self.switch_allocator == None):
            s += f"Switch Allocator Value : None \n "
        if(self.crossbar != None):
            s += f"CrossBar Value : {self.crossbar[2]} \n"
        if(self.crossbar == None):
            s += f"CrossBar Value : None \n"

        return s

    def inject(self,flit_details):
        self.input_buffer = flit_details

    def receive(self):
        self.crossbar = self.switch_allocator
        self.switch_allocator = self.input_buffer
        self.input_buffer = None

    def is_ready_to_receive(self,des):
        if(self.router_id == des and self.crossbar != None):
            return True
        return False

    def getflit(self): #returns flit details
        if(self.crossbar != None):
            return self.crossbar
        if(self.switch_allocator != None):
            return self.switch_allocator
        if(self.input_buffer != None):
            return self.input_buffer

    # def update1(self,nextrouter):
    #     if(not self.crossbar):
    #         nextrouter.input_buffer = self.crossbar
    #     if(not self.switch_allocator):
    #         self.crossbar = self.switch_allocator
    #     if(not self.input_buffer):
    #         self.switch_allocator = self.input_buffer

    #     self.input_buffer = None

    def update(self,next_id,allrouter):
        nextrouter = allrouter[next_id]
        nextrouter.input_buffer = self.crossbar
        self.crossbar = self.switch_allocator
        self.switch_allocator = self.input_buffer
        self.input_buffer = None

    # def clear(self):
    #     self.input_buffer = None
    #     self.switch_allocator = None
    #     self.crossbar = None

if __name__ == '__main__':

    def xy(flit_details,curr):
        #print(flit_details,len(flit_details),type(flit_details))
        src = int(flit_details[0])
        des = int(flit_details[1])
        flit = flit_details[2]

        #print(f"{src} + {des}")

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
        
        next_id = (3 * i_next) + j_next
        if(next_id not in range(0,9)):
            print(f"Out of range : {next_id} , where Current = {curr}")
        return next_id
    
    def xy1(flit_details,curr):
        dest=int(flit_details[1])
        curr_row=curr//3
        dest_row=dest//3
        curr_col=curr%3
        dest_col=dest%3
        next_id=0
        if(curr_col==dest_col):
            if(curr_row==dest_row):
                next_id= dest
            elif(curr_row<dest_row):
                next_id= (curr+3)
            else:
                next_id= (curr-3)
        else:
            if(curr_col<dest_col):
                next_id= (curr+1)
            else:
                next_id= curr-1
                
        print(f"{curr} {dest} {next_id}")
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

    all_routers = {i : Router(i) for i in range(0,9)}

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
                    curr_flit_details = r.getflit()
                    next_r = xy1(curr_flit_details,i)
                    r.update(next_r,all_routers)

            else:
                if(not r.isempty()):
                    next_r = xy1(flit_details,i)
                    r.update(next_r,all_routers)
                    r.inject(flit_details)
                else:
                    r.inject(flit_details)
   
            i -= 1

        j = 8
        while(j >= 0):
            print(f"At clock cycle : {clock} = {all_routers[j]}") 
            j -= 1

        clock += 1
        total += period

    print("Traffic file finished")

    while(not all_empty(all_routers)):
        i = 8
        while(i >= 0):
            r = all_routers[i]
            if(not r.isempty()):
                flit_details = r.getflit() #returns a list
                if(r.is_ready_to_receive(flit_details[1])):
                    r.receive()
     
                else:
                    next_r = xy1(flit_details,i)
                    r.update(next_r,all_routers)
             
            i -= 1
                
        j = 8 
        while(j >= 0):
            print(f"At clock cycle : {clock} = {all_routers[j]}") 
            j -= 1

        clock += 1
        total += period

        if(clock == 16):
            print("breaking !")
            break

        # mind fucked from here
    print(f"Total Time Taken = {total} & Clock Frequency = {1/period}")