# it-567-portscanner
Created by Zachary Knibb, Fall 2017

IT 567 at Brigham Young University

Usage: ps.py [-u -t -i] <target IP> <p1[ p2 p3 ...]>

  Any number of ports can be specified. Ports are separated by spaces. IP ranges and CIDR notation are not supported in this release.
  
  -u: UDP scan
  
  -t: TCP SYN scan (default)
  
  -i: ICMP ping scan

POINT DISTRIBUTION

40

  1. Allow command-line switches to specify a host and port.
  
  2. Present a simple response to the user.

10
  
  Allow multiple ports to be specified.

15

  ICMP - 5

  UDP (to complement TCP already provided) - 10

Resources:
  
  https://scapy.readthedocs.io/en/latest/usage.html
  
  https://scapy.readthedocs.io/en/latest/extending.html?highlight=sr1
  
  https://gist.github.com/TheZ3ro/7255052
