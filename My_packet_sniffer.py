from scapy.all import sniff

def capture(packet):
    if packet.haslayer("IP"):
        print(f"{packet['IP'].src}  -->  {packet['IP'].dst}")

print("Capturing Packets...\n")

sniff(prn=capture, store=False)
