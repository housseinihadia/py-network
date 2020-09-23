#server-tcp
import socket
from datetime import datetime
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind('127.0.0.1',6665)
server.listen(10) #namber users used server
#while True:
client,address=server.accept()
request=client.recv(1024)
request=request.decode("UTF-8")
print("client {} , request --> {}",format(address,request))
time=str(datetime.now().time())
time=time.encode('UTF-8')
client.send(time)
print("send to {}",format(address))
print("done..!")
client.close()
