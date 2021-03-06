#!/usr/bin/python3

'''
This script configures WAN IP after FW is factory default reset.
Written by: Qing Xia
Init Date: Nov 2016
Tested on Ubuntu 16.04 and Python 3.5.x
'''

import argparse
import pexpect
import sys
import time

# get port number
ipDict = {
    '10.0.0.20': '2043',  # NSA4600
    '10.0.0.23': '2046',  # NSA2600
    '10.0.0.24': '2010',  # NSA3600
    '10.0.0.25': '2011',  # NSA4600
    '10.0.0.27': '2014',  # NSA3600
    '10.0.0.54': '2040',  # NSA5600
    '10.0.0.61': '2022',  # TZ300
    '10.0.0.64': '2025',  # TZ400
    '10.0.0.66': '2029',  # TZ400
    '10.0.0.67': '2026',  # SM9800
    '10.0.0.68': '2027',  # SM9800
}


def checkPara():
    '''check input parameters'''
    usage = '''e.g. ./cfgWANIP.py 10.0.0.20'''
    parser = argparse.ArgumentParser(description=usage)
    parser.add_argument('wanip',
                        help='firewall WAN IP')
    args = parser.parse_args()

    global wanIp
    wanIp = args.wanip


def cfgWANIP(wanip):
    # telnet login (console login)
    port = ipDict[wanip]

    # start to telnet
    child = pexpect.spawn("telnet 10.103.64.8 %s" % port, encoding='utf-8')
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
    cfgWANIP(wanIp)
