#port scanner

import socket
target= str(input("Enter IP "))
ports=[12,20,22,23,24,25,80,443]
for p in ports :
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    r=s.connect_ex((target,p))
    if r == 0 :
        service=socket.getservbyport(p)
        print("--[ * {} * is open --> {} ]".format(p,service))
s.close()        