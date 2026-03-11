import socket
import args

arguments = args.args()
ports = args.parse_ports(arguments)

def grabber(dest):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.settimeout(5)
        s.connect((dest["host"],dest["port"]))
        banner = s.recv(1024).decode()
        print(f"{banner}")

    
for port in ports:
    grabber({"host":arguments["host"],"port":port})