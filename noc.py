import sys

try:
    with open('Log_File.txt', 'w') as output_file:
        sys.stdout = output_file
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
                    s += f"Input Buffer Value : {self.input_buffer[2]} \n"
                if(self.input_buffer == None):
                    s += f"Input Buffer Value : None \n"
                if(self.switch_allocator != None):
                    s += f"Switch Allocator Value : {self.switch_allocator[2]}  \n"
                if(self.switch_allocator == None):
                    s += f"Switch Allocator Value : None \n"
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
                if(int(self.router_id) == int(des) and self.crossbar != None):
                    return True
                return False

            def getflit(self): 
                if(self.crossbar != None):
                    return self.crossbar
                if(self.switch_allocator != None):
                    return self.switch_allocator
                if(self.input_buffer != None):
                    return self.input_buffer

            def update(self,next_id,allrouter):
                nextrouter = allrouter[next_id]
                nextrouter.input_buffer = self.crossbar
                self.crossbar = self.switch_allocator
                self.switch_allocator = self.input_buffer
                self.input_buffer = None

            def is_destination_flit(self,des):
                if(self.router_id == int(des)):
                    return True
                return False
            
            def is_valid_flit_type(flit):
                if len(flit) != 32:
                    return False
                return all(bit in '01' for bit in flit)


        if __name__ == '__main__':
            
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
                if(next_id not in range(0,9)):
                    print(f"Out of range : {next_id} , where Current = {curr}")
                    exit()
                return next_id
            
                
            
            def ispresent(clock,traffic_file):
                for i in range(0,len(traffic_file)):
                    if(clock == int(traffic_file[i][0])):
                        return traffic_file[i]
                    
                return []
            
            def is_valid_flit_type(flit):
                if len(flit) != 32:
                    return False
                
                return all(bit in '01' for bit in flit)
            
            def all_empty(all_routers):
                i = 0
                while(i < len(all_routers)):
                    if(not all_routers[i].isempty()):
                        return False
                    
                    i += 1

                return True
          
            try:
                with open('C:\\Users\\user\\Desktop\\NoC_Router-main\\NoC_Router-main\\traffic.txt', 'r') as file:
                    line = file.readlines()
                    eachline2 = []

                    line_number = 1  

                    for line_text in line:
                        temp = line_text.split()

                        print(temp)
                        if len(temp) != 4:
                            print(f"Error in line {line_number}: Invalid number of elements in the line.")
                            continue

                        src, des, flit = temp[1], temp[2], temp[3]

                        if src == des:
                            print(f"Error in line {line_number}: Source can't be the same as the destination.")
                            continue

            
                        if not is_valid_flit_type(flit):
                            print(f"Error in line {line_number}: Invalid flit type '{flit}'.")
                            continue

                        eachline2.append(temp)

                        line_number +=1

            except FileNotFoundError:
                print("Error: File 'traffic.txt' not found.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")


            try:
                with open('C:\\Users\\user\\Desktop\\NoC_Router-main\\NoC_Router-main\\delays.txt','r') as file1:
                    line1 = file1.readline()
                    line1 = line1.split()
                    line2 = []
                    for i in range(0,len(line1)):
                        line2.append(int(line1[i]))
                        if line2[i]<0:
                            print(f" Error : You have provided a negative value in delays file at {i}th element")

            except FileNotFoundError:
                print("Error: File 'delays.txt' not found.")
                exit()
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                exit()

            traffic_file = eachline2
            delay_file = line2

            buffer_delay = delay_file[0]
            sa_delay = delay_file[1]
            xbar_delay = delay_file[2]

            print("File reading done\n")

            all_routers = {i : Router(i) for i in range(0,9)}

            #print("Router Creation Done")

            period = max(buffer_delay,sa_delay,xbar_delay)
            clock = 1 #defining the clock

            total = 0

            while((not all_empty(all_routers)) or len(traffic_file) != 0):
                curr = ispresent(clock,traffic_file)
                flag=0
                if(curr != []):
                    traffic_file.remove(curr)
                    clk_cycle = int(curr[0])
                    src = int(curr[1])
                    des = int(curr[2])
                    flit = curr[3]
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

                else:
                    i = 8
                    while(i >= 0):
                        r = all_routers[i]
                        if(not r.isempty()):
                            flit_details = r.getflit() #returns a list
                            if(flit_details[0]>flit_details[1]):
                                i-=1
                                continue
                            
                            if(r.is_destination_flit(flit_details[1])):
                                r.receive()
                
                            else:
                                next_r = xy1(flit_details,i)
                                r.update(next_r,all_routers)
                                
                        
                        i -= 1
                    i = 0
                    while(i <= 8):
                        r = all_routers[i]
                        if(not r.isempty()):
                            flit_details = r.getflit() #returns a list
                            if(flit_details[0]<flit_details[1]):
                                i+=1
                                continue

                            if(r.is_destination_flit(flit_details[1])):
                                r.receive()
                
                            else:
                                next_r = xy1(flit_details,i)
                                r.update(next_r,all_routers)
                                
                        
                        i += 1
                        
                j = 8 
                while j >= 0:
                    try:
                        print(f"At clock cycle: {clock} = {all_routers[j]}\n")
                    except Exception as e:
                        print(f"Error printing router details: {str(e)}")
                    j -= 1

                clock += 1
                total += period

            try:
                print(f"Total Time Taken = {total} for {clock} cycles with Clock Frequency = {1 / period}")
            except Exception as e:
                print(f"Error printing total time: {str(e)}")
    sys.stdout = sys.__stdout__

except Exception as e:
    print(f"Error printing output location: {str(e)}")