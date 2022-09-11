import subprocess
from colorama import init, Fore, Back

a=[]
try:
    for ping in range(1,255):
        address = "192.168.1." + str(ping)
        res = subprocess.call(['ping', '-c', '3', address])
    
    
        if res == 0:
            print(Fore.GREEN + "ping to "+ address+ " OK" +Fore.WHITE)
            a.append(address)
        elif res == 2:
            print(Fore.GREEN + "no response from "+ address+Fore.WHITE)
        else:
            print(Fore.GREEN + "ping to "+ address+ " failed!"+Fore.WHITE)
        
except KeyboardInterrupt:
    print(Fore.GREEN+ "Software Stoped By User...")
    print(Fore.GREEN+ "IP List")
    for i in a:
        print(Fore.RED+" - "+ i)
