import os, re
from netaddr import *

##import uuid
##
##print(hex( uuid.getnode()))




#print(os.system(mycmd))

mycmd = os.popen('ip link show wifi0').read()


p = re.compile(r'^[a-fA-F0-9:]{17}|[a-fA-F0-9]{12}$', re.IGNORECASE)

m= mycmd.split(' ')

for x in m:
    x=x.strip()
    #print(x)
    
        
    mac_addr= re.findall(p, x)
        

print(mac_addr)

mac= EUI(mac_addr[0]).oui


print(mac)

