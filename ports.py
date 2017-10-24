#! /usr/bin/env python
# Created by Zachary Knibb, Fall 2017
# IT 567 at Brigham Young University

# POINT DISTRIBUTION
# 40
#	1. Allow command-line switches to specify a host and port.
#	2. Present a simple response to the user.
# 10
#	Allow multiple ports to be specified.
# 15
#	ICMP - 5
#	UDP (to complement TCP already provided) - 10

import sys
from scapy.all import sr1, IP, TCP, UDP, ICMP

# User must supply host and port
if len(sys.argv) < 3:
    print "Invalid syntax: ps.py [-u -t -i] <target IP> <p1[ p2 p3 ...]>"
else:
    # TCP SYN
    if sys.argv[1] == "-t":
        print "TCP SYN scan on host " + sys.argv[2] + "\n"

        ip = IP()
        tcp = TCP()

        # cast as str and int to avoid issues caused by periods
        ip.dst = str(sys.argv[2])
        # loop iterates through as many commandline arguments were given
        for port in range(len(sys.argv)-3):
            print "Scanning port " + str(sys.argv[port+3])
            # port+3 is start of ports
            tcp.dport = int(sys.argv[port+3])
            # send SYN packet
            tcp.flags = "S"
            packet = (ip/tcp)
            # verbose=0 to limit console output; timeout 1s
            status = sr1(packet, verbose=0, timeout=1)
            if status:
                print str(packet.dport) + " is open\n"
    # UDP
    elif sys.argv[1] == "-u":
        print "UDP scan on host " + sys.argv[2] + "\n"

        ip = IP()
        udp = UDP()

        # cast as str and int to avoid issues caused by periods
        ip.dst = str(sys.argv[2])
        # loop iterates through as many commandline arguments were given
        for port in range(len(sys.argv)-3):
            print "Scanning port " + str(sys.argv[port+3])
            # port+3 is start of ports
            udp.dport = int(sys.argv[port+3])
            packet = (ip/udp)
            # verbose=0 to limit console output; timeout 1s
            status = sr1(packet, verbose=0, timeout=1)
            if status:
                print str(packet.dport) + " is open\n"
    # ICMP
    elif sys.argv[1] == "-i":
        print "PING scan on host " + sys.argv[2] + "\n"

        ip = IP()
        ping = ICMP()

        # cast as str and int to avoid issues caused by periods
        ip.dst = str(sys.argv[2])
        packet = (ip/ping)
        # verbose=0 to limit console output; timeout 1s
        status = sr1(packet, verbose=0, timeout=1)
        if status:
            print str(packet.dst) + " is online"
    # assume TCP SYN if no flag is specified
    else:
        print "TCP SYN scan on host " + sys.argv[1] + "\n"

        ip = IP()
        tcp = TCP()

        # cast as str and int to avoid issues caused by periods
        ip.dst = str(sys.argv[1])
        # loop iterates through as many commandline arguments were given
        for port in range(len(sys.argv)-2):
            print "Scanning port " + str(sys.argv[port+2])
            # port+2 is start of ports
            tcp.dport = int(sys.argv[port+2])
            # send SYN packet
            tcp.flags = "S"
            packet = (ip/tcp)
            # verbose=0 to limit console output; timeout 1s
            status = sr1(packet, verbose=0, timeout=1)
            if status:
                print str(packet.dport) + " is open\n"