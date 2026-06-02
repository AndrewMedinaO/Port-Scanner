import socket
import concurrent.futures
import time
ip = "127.0.0.1"





def ScannerFunc(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    result = s.connect_ex((ip, port))
    s.close()
    if result == 0:
        return port
    

def Grab_Banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip,port))
        s.send(b"hi")
        banner = s.recv(1024)
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
        print(f"{ip}:{port} is open: (no banner sad  ))")


endnew = time.time()

print(f"Banner Fetch finished in {endnew - startnew:.2f} seconds")