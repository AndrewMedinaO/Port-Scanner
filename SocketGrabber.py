import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
ip = "127.0.0.1"
port = 8000
result = s.connect_ex((ip, port))
if result == 0:
    print(f"Port {port} open on {ip}")
else:
    print(f"Port {port} closed on {ip} (code {result})")
s.close()