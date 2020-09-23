import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    sdata=str(input())
    s.sendto(sdata,("127.0.0.1",5555)) #address("ip client 0.0.0.0",port 3256)
    sdata=sdata.encode("UTF-8") #encode encryption
    Rdata,address=s.recvfrom(1024) #SIZE DATA
    Rdata=Rdata.decode("UTF-8") #decode decryaption
    print("data recived from {}:\n {} ".format(address,Rdata))
