This pyhton program is the implenation of a DOS protection firewall.
I imported libraries like scarpy and implemented its submodule sniff which allows the program to analyse network packets
I imported the time library to monitor time intervals which i used to determine a transfer rate for the packets 
The library defaultdict store/ manages packet count for each IP address
If an IP sends packets at a rate higher than the threshold the program blocks that IP source 
