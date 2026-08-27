from scapy.all import sniff, IP, TCP, UDP, ICMP

packet_count = 0

def packet_callback(packet):
    global packet_count
    if IP in packet:
        packet_count += 1
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            print(f"[{packet_count}] [TCP] {src_ip}:{sport} -> {dst_ip}:{dport}")

        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            print(f"[{packet_count}] [UDP] {src_ip}:{sport} -> {dst_ip}:{dport}")

        elif ICMP in packet:
            print(f"[{packet_count}] [ICMP] {src_ip} -> {dst_ip}")

        else:
            print(f"[{packet_count}] [OTHER] {src_ip} -> {dst_ip} | Protocol: {proto}")

print("="*60)
print("Starting Network Packet Analyzer...")
print("Press Ctrl+C to stop")
print("="*60)

try:
    sniff(prn=packet_callback, store=False)
except KeyboardInterrupt:
    print(f"\n{'='*60}")
    print(f"Capture stopped. Total packets analyzed: {packet_count}")
    print(f"{'='*60}")
