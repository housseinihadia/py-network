from scapy.all import ARP,Ether,srp
def scan(ip):
    arp_req=ARP(pdst=ip) #ip
    brodcast=Ether(dst="FF:FF:FF:FF:FF:FF") #brodcast
    arp_brodcast=brodcast/arp_req
    reslut=srp(arp_brodcast,timeout=3,verbose=False)[0]
    print(reslut)
    lst=[]
    for element in reslut:
        clients={"ip": element[1].psrc,"mac":element[1].hwsrc}
        lst.append(clients)
    print("IP \t\t\t\t\t MAC")
    print("-------------------------")
    for i in lst:
        print("{} \t\t\t\t {}".format(i["ip"],i["mac"]))
ip="192.168.1.1"
scan(ip)        