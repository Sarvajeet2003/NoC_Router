# FileParser.py

def read_traffic_file(traffic_file_path):
    traffic_data = []
    
    try:
        with open(traffic_file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                parts = line.split()
                if len(parts) != 4:
                    print("Error: Invalid line in traffic file:", line)
                    continue
                
                cycle, source, destination, flit = int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])
                traffic_data.append((cycle, source, destination, flit))
    
    except FileNotFoundError:
        print("Error: Traffic file not found.")
        return None
    except Exception as e:
        print("Error:", str(e))
        return None
    
    return traffic_data

# def read_delays_file(delays_file_path):
#     delays = {}
    
#     try:
#         with open(delays_file_path, 'r') as file:
#             for line in file:
#                 line = line.strip()
#                 if not line:
#                     continue  # Skip empty lines
#                 parts = line.split()
#                 if len(parts) != 2:
#                     print("Error: Invalid line in delays file:", line)
#                     continue
                
#                 router_element, delay = parts[0], float(parts[1])
#                 delays[router_element] = delay
    
#     except FileNotFoundError:
#         print("Error: Delays file not found.")
#         return None
#     except Exception as e:
#         print("Error:", str(e))
#         return None
    
#     return delays
# FileParser.py

def read_delays_file(delays_file):
    delays_data = {}  # Create an empty dictionary to store delay information
    with open(delays_file, 'r') as file:
        for line in file:
            router_id, buffer_delay, sa_delay, xbar_delay = map(int, line.strip().split())
            delays_data[router_id] = {
                'buffer_delay': buffer_delay,
                'sa_delay': sa_delay,
                'xbar_delay': xbar_delay
            }
    return delays_data
