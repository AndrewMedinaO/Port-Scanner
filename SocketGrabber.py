import socket


ip = "127.0.0.1"





for port in range(1,9000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.001)
    result = s.connect_ex((ip, port))
    
    if result == 0:
        print(f"Port {port} open on {ip}")
    
    
    s.close()