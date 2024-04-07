from scapy.all import IP, ICMP, send
import time

def send_timing_channel_message(message, target_ip, interval=0.5):
    """Send a message using timing intervals encoded in ICMP packets."""
    for char in message:
        if char == '1':
            time.sleep(interval * 2)  # Wait longer for '1'
        else:
            time.sleep(interval)  # Shorter wait for '0'
        # Send an ICMP packet to represent a 'bit'
        send(IP(dst=target_ip)/ICMP())

def covert_message_to_binary(message):
    """Convert a message to binary."""
    return ''.join(format(ord(c), '08b') for c in message)

msg = covert_message_to_binary('hi')
send_timing_channel_message(msg,'192.168.1.195')