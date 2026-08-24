from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            print(f"[TCP] {src_ip}:{sport} -> {dst_ip}:{dport}")

        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            print(f"[UDP] {src_ip}:{sport} -> {dst_ip}:{dport}")

        elif ICMP in packet:
            print(f"[ICMP] {src_ip} -> {dst_ip}")

        else:
            print(f"[OTHER] {src_ip} -> {dst_ip} | Protocol: {proto}")

print("Starting Network Packet Analyzer... (Press Ctrl+C to stop)")
sniff(prn=packet_callback, store=False)