from scapy.all import sniff, IP, ICMP
import time

def decode_timing_channel_message(packet, start_time, interval=0.5):
    """Decode a message from timing intervals between received ICMP packets."""
    # Calculate the time difference between packets
    time_diff = packet.time - start_time
    if time_diff >= interval * 1.5:
        return '1'
    else:
        return '0'

def listen_for_timing_channel_messages(filter_ip, interval=0.5):
    """Listen for ICMP packets and decode the timing channel message."""
    messages = []
    start_time = time.time()  # Record the start time
    def process_packet(packet):
        if packet[IP].src == filter_ip and packet.haslayer(ICMP):
            bit = decode_timing_channel_message(packet, start_time, interval)
            messages.append(bit)
            start_time = packet.time  # Update start time for next bit

    sniff(filter=f"icmp and src {filter_ip}", prn=process_packet, store=0)
    return ''.join(messages)

listen_for_timing_channel_messages('192.168.1.195')