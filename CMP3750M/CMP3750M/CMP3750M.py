import os
from win10toast import ToastNotifier
import time
#initialisation 
ICMPWarning = "\nThis network is vulnerable to ICMP attacks, please disable ICMP unless it is needed"
notif = ToastNotifier()
running = 1
#get hostname
print("Enter a hostname:\nEG: youtube.com")
hostname = input()

while running == 1: #loop forever
    response = os.system("ping " + hostname)#ping hostname

    if response == 0:
        print(ICMPWarning)#warn user about ICMP vulnerabilities  
        time.sleep(300) #wait 5 mins
    else:
        notif.show_toast("Server Downtime detected!","Potential DDOS attack")#notify user of downtime


