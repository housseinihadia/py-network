import socket
from datetime import datetime
                   #ipv4        #udp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",5555)) #bind(ip,port namber)
while True:
    Rdata,address=s.recvfrom(1024) #SIZE DATA
    Rdata=Rdata.decode("UTF-8") #decode decryaption
    print("data recived from {}:\n {} ".format(address,Rdata))
    sdata=str(datetime.now())
    sdata=sdata.encode("UTF-8") #encode encryption
    s.sendto(sdata,address) #address("ip client 0.0.0.0",port 3256)