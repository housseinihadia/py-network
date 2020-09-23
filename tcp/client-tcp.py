#client-tcp
import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',6665))
request="hi srever i want to know time"
request=request.encode("UTF-8")
client.send(request)
time=client.recv(1024)
time=time.decode("UTF-8")
print("the time now is : >{}".format(time))
client.close()