from scapy.all import *

def process_packet(packet):

    if packet.haslayer(IP):

        print("\n========== Packet Captured ==========")

        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

        protocol = packet[IP].proto

        if protocol == 6:
            print("Protocol: TCP")

        elif protocol == 17:
            print("Protocol: UDP")

        elif protocol == 1:
            print("Protocol: ICMP")

        else:
            print("Protocol Number:", protocol)

sniff(prn=process_packet, store=False, count=10)