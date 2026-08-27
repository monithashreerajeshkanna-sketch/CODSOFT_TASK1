# CODSOFT_TASK1
Python tool using Scapy to capture and analyze live network packets — displays source IP, destination IP, protocol, and port details in real-time.
Network Packet Analyzer

 What is this?
A Python application that captures live network packets travelling through your system and displays important details about each packet in real-time — like a mini Wireshark built from scratch.

 What it does
- Captures live packets flowing through the network
- Identifies the protocol used (TCP / UDP / ICMP)
- Extracts and displays:
  - Source IP address
  - Destination IP address
  - Source Port & Destination Port (for TCP/UDP)
  - Protocol type
- Displays everything in a clean, readable format in the terminal

Tools & Technologies Used
Tool      Purpose 
Python 3 - Programming language 
Scapy (library) - Packet capturing & analysis 
 Npcap - Windows driver required for packet sniffing 

 Requirements
- Python 3.x installed
- Scapy library
- Npcap installed (Windows only)
- Administrator/root access (mandatory for packet sniffing)

 How it Works
- The script uses Scapy's `sniff()` function to capture packets passing through the network interface
- Each captured packet is passed to a callback function
- The function checks the packet's protocol layer (TCP/UDP/ICMP) and extracts the relevant IP addresses and port numbers
- The extracted information is printed to the console in real-time

