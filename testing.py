def bubble_sort(lst,n):
    for i in range(n):
        for j in range(n-i-1):
            if int(lst[j][0]) > int(lst[j+1][0]):
                lst[j], lst[j+1] = lst[j+1], lst[j]

def check_last_two_digits(temp1, temp2):
    return temp1[3][-2:] == temp2[3][-2:]
flagSarva = 0
with open('traffic.txt', 'r') as file:
    lines = file.readlines()
    eachline2 = []
    line_number = 1  

    for i in range(0, len(lines), 3):
        temp1 = lines[i].strip().split()
        temp2 = lines[i + 1].strip().split()
        temp3 = lines[i + 2].strip().split()


        src1, des1, flit1 = temp1[1], temp1[2], temp1[3]
        src2, des2, flit2 = temp2[1], temp2[2], temp2[3]
        src3, des3, flit3 = temp3[1], temp3[2], temp3[3]

        eachline2.extend([temp1, temp2, temp3])
        line_number += 3

try:
    with open('delays.txt','r') as file1:
        line1 = file1.readline()
        line1 = line1.split()
        line2 = []
        delay_dic = {0 : 'Input Buffer' , 1 : 'Switch Allocator' , 2 : 'CrossBar' }
        for i in range(0,len(line1)):
            line2.append(float(line1[i]))
            if line2[i] < 0:
                print(f"Error : You have provided a negative value in delays file at {delay_dic[i]}")
                exit()

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


period = max(buffer_delay,sa_delay,xbar_delay)
clock = 1 #defining the clock

total = 0
flit_time = []
bubble_sort(traffic_file,len(traffic_file))
print(traffic_file)
