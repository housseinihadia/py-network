import socket
#gethostbyname(" name ")
ip=socket.gethostname("www.google.com")
print(ip)
#gethostbyaddr(ip get me hostname)
host=socket.gethostbyaddr(str(ip))
print(host)
#getservbyname(get me portname)
port=socket.getservbyname("ftp.data")
#getservbyport (namber port) nameport
service_name=socket.getservbyport(21)