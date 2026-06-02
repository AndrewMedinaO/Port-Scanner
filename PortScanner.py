import socket
import concurrent.futures
import time
#Local IP
ip = "127.0.0.1"





def ScannerFunc(port):
    #Create Socket Object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    #Connect to ip with port
    result = s.connect_ex((ip, port))
    #Close port
    s.close()
    if result == 0: #0 means open
        return port
    

def Grab_Banner(ip, port):
    try:
        #Create Socket Object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip,port))
        #Send bytes to service
        s.send(b"hi")
        #Recieve bytes from service
        banner = s.recv(1024)
        #Decode response
        banner = banner.decode("utf-8", errors="ignore").strip()
        s.close()

        return banner
    except: 
        return None




Open_Ports = []
start = time.time()
print(f"-- Scanning for Ports --")

with concurrent.futures.ThreadPoolExecutor() as executor:

    results = executor.map(ScannerFunc, range(1,9000))

    for result in results:
        if result is not None:
            print(f"{ip}:{result} is open")
            Open_Ports.append(result)

end = time.time()

print(f"Scan finished in {end - start:.2f} seconds")


print(f"-- Begining Banner fetch --")

startnew = time.time()
for port in Open_Ports:
    banner = Grab_Banner(ip, port)
    if banner:
        print(f"{ip}:{port} is open: {banner}")
    else:
        print(f"{ip}:{port} is open: (no banner sad)")


endnew = time.time()

print(f"Banner Fetch finished in {endnew - startnew:.2f} seconds")