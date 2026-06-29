import socket
def scan_port(ip,port):
     sock=socket.socket()   #From the socket module, take the socket class and create an object (instance) of that class.
     sock.settimeout(0.2)
    
     result=sock.connect_ex((ip,port))
     if result==0:
       print(f"Port {port} is OPEN")
     sock.close()

try:
     ip=input("Enter the IP: ")
     start_port=int(input("Enter the start port: "))
     end_port=int(input("Enter the end port: "))
     for port in range(start_port,end_port+1):
        scan_port(ip,port)

except socket.gaierror:
   print("Invalid IP address.")


   


