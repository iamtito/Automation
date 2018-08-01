###########################
#Author: Kabir Bolatito
#Version: 1.0
#Description: This is a python file that login to a <dockerServer>,
#             run some commands and print them on the terminal
#               
###########################

from pexpect import pxssh
#import docker
import getpass
import datetime

try:
	s = pxssh.pxssh()
        hostname = "dockerServer"
        username = "username"
        password = getpass.getpass('baba oya enter your password: ')
        #password = "<password>" #You can uncomment this section if you want to hardcode password 
        s.login (hostname, username, password)
        s.sendline ('uptime')  # run a command
        s.prompt()             # match the prompt
        print (s.before)        # print everything before the prompt.)
        s.sendline ('ls -l')
        s.prompt()
        print (s.before)
        s.sendline ('df')
        s.prompt()
        print (s.before)
        s.sendline('uname')
        s.prompt()        
        os = (s.before)
        if "Linux" in os:
        	print ("This one na Linux")
        	s.sendline('docker ps')
        	s.prompt()
        	checkprocess = (s.before)
        	if 'wordpress' in checkprocess:
        		print ("Wordpress is running")
        	else:
        		print ("Wordpress is not running")
        	if 'chartserver' in checkprocess:
        		print("chartserver is running")
        	else:
        		print ("chartserver is not running")
        	
        	s.sendline("docker images --format '{{.Size}} - {{.Repository}} - {{.Tag}} - {{.ID}}' | sort -h -r | column -t")
        	s.prompt()
        	print (s.before)
        else:
        	print ("No be Linux")

        
        s.logout()
except pxssh.ExceptionPxssh, e:
    print ("pxssh failed on login.")
    print (str(e))

# ###   Output  ####
# baba oya enter your password: 
# uptime
#  20:18:52 up 1 day,  1:56,  1 user,  load average: 0.24, 0.34, 0.38

# ls -l
# total 525536
# -rw------- 1 tito            tito             268105216 Jun  6 22:18 apacheserver
# -rw------- 1 tito            tito             268105216 Jun  6 22:20 apacheserver.tar
# drwxrwxr-x 2 tito            tito                  4096 Jul 27 21:23 charts
# -rwxrwxr-x 1 tito            tito                   218 May  4 21:03 container.py
# drwxrwxr-x 2 tito            tito                  4096 Jul 27 21:23 data
# -rwxrwxr-x 1 tito            tito                  1067 Mar 16 23:25 Dockerfile
# -rwxrwxr-x 1 tito            tito                   410 Mar 14 01:29 Dockerfile1.0
# -rwxrwxr-x 1 tito            tito                   409 Mar 13 01:30 DockerfileENV
# drwxrwxr-x 5 systemd-resolve systemd-timesync      4096 Mar 16 21:25 elasticSearchData
# drwxrwxr-x 2 tito            tito                  4096 Mar 14 04:20 files
# -rw-rw-r-- 1 tito            tito               1642329 May  4 20:22 get-pip.py
# -rw-rw-r-- 1 tito            tito                     0 Mar 13 19:13 grep
# -rw-rw-r-- 1 tito            tito                 21959 Mar 14 04:40 ipmoody.json
# -rw-rw-r-- 1 tito            tito                 16092 May 10 22:34 list-containers.json
# -rw-rw-r-- 1 tito            tito                   180 May 10 22:34 list-containers.pl
# drwxrwxr-x 2 tito            tito                  4096 Mar 15 23:24 logbackup
# -rw-rw-r-- 1 tito            tito                    76 Mar 16 23:49 logstashconf.conf
# -rw-rw-r-- 1 tito            tito                  1367 Mar 14 05:10 pointer.html
# -rw-rw-r-- 1 tito            tito                  9691 May  4 19:36 running.json
# -rw-rw-r-- 1 tito            tito                  4001 May 14 06:02 t0.json
# -rw-rw-r-- 1 tito            tito                163773 Jun  4 14:45 time.json
# -rw-rw-r-- 1 tito            tito                 16093 May 14 01:26 t.json
# -rw-rw-r-- 1 tito            tito                  4001 May 14 01:27 tt.json

# df
# Filesystem     1K-blocks     Used Available Use% Mounted on
# udev             1014712        0   1014712   0% /dev
# tmpfs             204808    21548    183260  11% /run
# /dev/vda1       25227048 12139696  13070968  49% /
# tmpfs            1024036        4   1024032   1% /dev/shm
# tmpfs               5120        0      5120   0% /run/lock
# tmpfs            1024036        0   1024036   0% /sys/fs/cgroup
# /dev/vda15        106858     3437    103421   4% /boot/efi
# tmpfs             204808        0    204808   0% /run/user/1000

# This one na Linux
# Wordpress is running
# chartserver is running
# D}}' | sort -h -r | column -tze}} - {{.Repository}} - {{.Tag}} - {{.I 
# 1.46GB  -  gitlab/gitlab-ce     -  latest    -  01d449655e58
# 954MB   -  rancher/server       -  v1.6.1    -  e96eab16bd1e
# 581MB   -  elasticsearch        -  latest    -  ab4f2bb7461f
# 441MB   -  tito/fedora          -  latest    -  5ba3c5f08347
# 407MB   -  wordpress            -  latest    -  9ce0dc63b7ed
# 407MB   -  wordpress_commit     -  latest    -  f2131883651e
# 371MB   -  jpetazzo/nsenter     -  latest    -  c16fe938c1a5
# 317MB   -  loginspector_server  -  snapshot  -  f59ea1b60b6e
# 286MB   -  ubuntussh            -  latest    -  acbb786cc01c
# 262MB   -  ubuntukibana         -  latest    -  bdbb8110879a
# 258MB   -  apacheserver         -  latest    -  facae7db16e0
# 253MB   -  fedora               -  latest    -  cc510acfcd70
# 222MB   -  ubuntu               -  14.04     -  a35e70164dfb
# 205MB   -  mysql                -  5.5       -  016bbb6bd994
# 112MB   -  ubuntu               -  latest    -  f975c5035748
# 109MB   -  nginx                -  latest    -  e548f1a579cf

