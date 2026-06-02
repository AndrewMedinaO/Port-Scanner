import socket
import concurrent.futures
import time
ip = "127.0.0.1"





def ScannerFunc(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    result = s.connect_ex((ip, port))
    
    if result == 0:
        return port
    
    
    s.close()
start = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:

    results = executor.map(ScannerFunc, range(1,1025))
    for result in results:
        if result != None:
            print(f"{ip}:{result} is open")


end = time.time()

print(f"Scan finished in {end - start:.2f} seconds")