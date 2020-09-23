from scapy.all import ARP,Ether,srp
import sys
exist=[]
def scan(ip):
    while True:
            try:
                arp_req=ARP(pdst=ip) 
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
                    if i["mac"] not in exist:
                        print("{} \t\t\t\t {}".format(i["ip"],i["mac"]))
                        exist.append(i['mac'])
            except:
                 print("/Exit..!")
                 sys.exit()              
ip=str(input("Enter ip & prefix "))
scan(ip)        