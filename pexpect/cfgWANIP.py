#!/usr/bin/python3

'''
This script could automatically configure WAN IP after UTM is factory default reset.
Written by: Alex (Qing) Xia
Version: 0.2
Date: 3/21/2017
This script doesn't work if UTM is not in non-conf t mode.
!!! Using python3 !!!
Tested on Ubuntu16.04
'''

import pexpect
import time
import sys

# get port number
ipDict = {
'10.0.0.20':'2043',
'10.0.0.24':'2010',
'10.0.0.25':'2011',
'10.0.0.61':'2022',
'10.0.0.64':'2025',
'10.0.0.66':'2029',
'10.0.0.67':'2026',
'10.0.0.68':'2027'}

def usage():
    print('''Usage: command WANIP
e.g. ./cfgWANIP.py 10.0.0.25''')

def checkPara():
    while True:
        if len(sys.argv) == 1:
            usage()
            sys.exit()
        elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
            usage()
            sys.exit()
        elif len(sys.argv) != 2:
            usage()
            sys.exit()
        else:
            break

def cfgWANIP(wanip):
    # telnet login (console login)
    port = ipDict[wanip]
    
    # start to telnet
    child = pexpect.spawn("telnet 10.103.64.8 %s" % port, encoding = 'utf-8')
    child.logfile = sys.stdout
    child.expect("login:")
    child.sendline("admin")
    child.expect("Password:")
    child.sendline("password")
    time.sleep(1)
    child.sendline("")
    
    index = child.expect(["User", "admin@[A-Z0-9]{12}>"])
    if index == 0:
        child.sendline("admin")
        child.expect("Password:")
        child.sendline("password")
    elif index == 1:
        pass
    else:
        print("Program error! Exit.")
        sys.exit()
    
    # login to UTM console, starting to configure WAN IP
    child.sendline("configure terminal")
    
    child.expect("config\([A-Z0-9]{12}\)#")
    child.sendline("interface X1")
    
    child.expect("\(edit-interface\[X1\]\)#")
    child.sendline("ip-assignment WAN static")
    
    child.expect("\(edit-WAN-static\[X1\]\)#")
    child.sendline("ip %s netmask 255.255.255.0" % wanip)
    
    child.expect("\(edit-WAN-static\[X1\]\)#")
    child.sendline("gateway 10.0.0.1")
    
    child.expect("\(edit-WAN-static\[X1\]\)#")
    child.sendline("dns primary 10.217.131.101")
    
    child.expect("\(edit-WAN-static\[X1\]\)#")
    child.sendline("exit")
    
    child.expect("\(edit-interface\[X1\]\)#")
    child.sendline("management https")
    
    child.expect("\(edit-interface\[X1\]\)#")
    child.sendline("management ssh")
    
    child.expect("\(edit-interface\[X1\]\)#")
    child.sendline("management ping")
    
    child.expect("\(edit-interface\[X1\]\)#")
    child.sendline("commit")

    child.expect("\(edit-interface\[X1\]\)#")
    child.sendline("exit")

    child.expect("config\([A-Z0-9]{12}\)#")
    child.sendline("exit")
    
    time.sleep(2)
    child.close()

if __name__ == '__main__':
    checkPara()
    cfgWANIP(wanip = sys.argv[1])
