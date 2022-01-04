#!/bin/bash

mkdir /root/reboot ; mount >> /root/reboot/$(date '+%Y%m%d')-$(date '+%H%M')-mount.txt; df >> /root/reboot/$(date '+%Y%m%d')-$(date '+%H%M')-df.txt; iptables -L >> /root/reboot/$(date '+%Y%m%d')-$(date '+%H%M')-iptables.txt; firewall-cmd --list-all >> /root/$(date '+%Y%m%d')-$(date '+%H%M')-firewalld.txt; ps auxwww >> /root/reboot/$(date '+%Y%m%d')-$(date '+%H%M')-ps.txt; docker ps >> /root/reboot/$(date '+%Y%m%d')-$(date '+%H%M')-docker.txt ; lsof -i -n -P | grep LISTEN >> /root/reboot/$(date '+%Y%m%d')-$(date '+%H%M')-lsof.txt
