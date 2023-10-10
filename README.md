# Network on Chip (NoC) Simulator

## Project Description
This project is a Network on Chip (NoC) simulator that models and simulates the behavior of a NoC architecture. It includes the simulation of NoC routers, packet routing algorithms, and various components of the network.

## Components

### Router
The Router class represents a router in the NoC. It is initialized as Follows

**Router( router ID, Buffer Delay, Switch Allocator delay, Corssbar delay)**

A router will have  :-
- Router ID
- An Input buffer 
- A crossbar 
- A Switch allocator.

```python
class Router:
    def __init__(self, router_id,buffer_delay,sa_delay,xbar_delay):
        self.router_id = router_id
        self.input_buffer = InputBuffer(buffer_delay)
        self.crossbar = Crossbar(xbar_delay)
        self.switch_allocator = SwitchAllocator(sa_delay)

    def __str__(self):
        return f"Router ID : {self.router_id} \n Input Buffer Value : {self.input_buffer.value} \n CrossBar Value : {self.crossbar.value} \n Switch Allocator Value : {self.switch_allocator.value} \n"

    def update(self,nextrouter,new_flit): #this is function that determines how the data will flow inside a router as well as between 2 routers
        nextrouter.input_buffer.value = self.crossbar.value
        self.crossbar.value = self.switch_allocator.value
        self.switch_allocator.value = self.input_buffer.value
        self.input_buffer.value = new_flit
```

### Input Buffer
* The InputBuffer class represents the input buffer component of a router. 
* It has a **delay** parameter.
* It also represents as a stage in our pipelining containing value in **self.value**.
* In a clock cycle if it contain some data , it should be transferred to the **Switch Allocator of the same Router** & contain a value from **Crossbar of the Previous Router**.

```python
class InputBuffer:
    def __init__(self, delay):
        self.delay = delay
        self.value = None
```

### Switch Allocator
* The SwitchAllocator class represents the switch allocator component of a router. 
* It has a **delay** parameter and tracks **input** and **output** ports.
* It also represents as a stage in our pipelining containing value in **self.value**.
* In a clock cycle if it contain some data , it should be transferred to the **Crossbar of the same Router** & contain a value from **Buffer of the same Router**.

```python
class SwitchAllocator:
    def __init__(self, delay):
        self.delay = delay
        self.value = None
        self.input_port = None
        self.output_port = None
```
### Crossbar
 * The Crossbar class represents the crossbar component in each router. 
 * It is responsible for configuring connections between **input** and **output** ports and has a **delay** parameter.
 * It also represents as a stage in our pipelining containing value in **self.value**.
 * In a clock cycle if it contain some data , it should be transferred to the **Buffer of the next determined router** & contain a value from **Switch Allocator of the same Router**.

```python
class Crossbar:
    def __init__(self, delay):
        self.delay = delay
        self.value = None
```

## Noc (Network on Chip)
The Noc file contains the simulation logic for the NoC, including the XY routing algorithm implementation and the main simulation loop.

* The lines of code implements the logic for the **XY** routing algorithm which includes a **ID of current Router** , **ID of source Router** and **ID of Destination Router**.

```python
def xy(curr_id,src,des):
    curr = curr_id

    i_curr = curr // 3 #Packing 1D indexes into 2D indexes
    j_curr = curr % 3

    i_src = src // 3
    j_src = src % 3
    
    i_des = des // 3
    j_des = des % 3
    # for eg if destination is 8 then 8%3=2 and 8//3=2 hence it denotes the coordinates of the last router.

    if(j_des > j_src and j_curr + 1 < 3): #if the dest id is greater than the source id in x-direction, the packet moves right and the value of i remains unchanged
        i_next = i_curr
        j_next = j_curr + 1
    elif(j_des > j_src and j_curr + 1 == 3): #if packet cannot move in X-axis anymore , we will move in Y-axis
        i_next = i_curr + 1
        j_next = j_curr
    elif(j_des < j_src and j_curr - 1 >= 0 ): #if the dest id is lesser than the source id in x-direction, the packet moves left and the value of i remains unchanged
        i_next = i_curr
        j_next = j_curr - 1
    elif(j_des < j_src and j_curr - 1 < 0): #if packet cannot move in X-axis anymore , we will move in Y-axis
        i_next = i_curr - 1
        j_next = j_curr

    next_id = 3 * i_next + j_next
    return next_id
# Similarly we have made the two cases where the dest is greater than source and vice-versa. if we wish to visualise both the cases. Firstly it is moving rightways then down and in the other case, it is moving leftways and then up.


with open('traffic.txt','r') as file: # this is the basic code to read the traffic
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

with open('delays.txt','r') as file1: # this is the basic code to read the delay file.
    line1 = file1.readline()
    line1 = line1.split()
    line2 = []
    for i in range(0,len(line1)):
        line2.append(int(line1[i]))

traffic_file = eachline2 # It contain values of traffic file in an iteratable format
delay_file = line2 # It contain Values of Delay file in an iteratable format

buffer_delay = delay_file[0]
sa_delay = delay_file[1]
xbar_delay = delay_file[2]


all_routers = {i : Router(i,buffer_delay,sa_delay,xbar_delay) for i in range(0,9)} 
# we are storing all the routers and map them with their ID so that whenever we need them, we can call from here.
# {Router ID : Router Object}

clock = 1 #defining the clock

for i in range(0,len(traffic_file)): #traversing traffic file

    clk_cycle = int(traffic_file[i][0])
    src = int(traffic_file[i][1])
    des = int(traffic_file[i][2])
    flit = traffic_file[i][3]

    # we have a doubt afterwards , how can we implement pipeline , update all the routers and inject new packets on different routers on the same clock cycle.

    next_id = xy(i,src,des)

    all_routers[i].update(next_id,flit)


    flit_type = flit[-2::]
    if(flit_type == '00'):
        print("Header")
    elif(flit_type == '01'):
        print("Body")
    elif(flit_type == '10'):
        print("Tail")
```

# Usage
Input Files:

1. We have created a traffic.txt file with packet insertion details, including clock cycle, source, destination, and flit type.
2.  We have also created a delays.txt file containing delays for router elements.

# Run the Simulator:
Execute the Noc file(which is our main file) to run the simulator. It will read input files and perform NoC simulations.
