
# Timing Channel Communication with Scapy and Cisco Packet Tracer

This repository contains Python scripts for covert communication between two endpoints using timing channels implemented with Scapy. Timing channels leverage variations in the timing of network packets to convey information covertly. Additionally, Cisco Packet Tracer is utilized for simulating network environments to test the functionality of these scripts.

## Prerequisites

- Python 3.x
- Scapy library (`pip install scapy`)
- Cisco Packet Tracer

## Usage

1. Ensure that Scapy is installed (`pip install scapy`).
2. Set up a network environment using Cisco Packet Tracer to simulate sender and receiver devices.
3. Run the sender script `timing_channel_sender.py` to send a message:

```bash
python timing_channel_sender.py
```

4. Run the receiver script `timing_channel_receiver.py` to listen for messages:

```bash
python timing_channel_receiver.py
```

## Sender Script (`timing_channel_sender.py`)

The sender script constructs ICMP packets to represent binary bits and sends them to the specified target IP address. Timing intervals are encoded in the transmission to convey the message.

```python
send_timing_channel_message(message, target_ip, interval=0.5)
```

- `message`: The message to be sent.
- `target_ip`: IP address of the receiver.
- `interval`: Time interval between each bit (default is 0.5 seconds).

## Receiver Script (`timing_channel_receiver.py`)

The receiver script listens for ICMP packets from a specified source IP address and decodes the timing intervals to reconstruct the original message.

```python
listen_for_timing_channel_messages(filter_ip, interval=0.5)
```

- `filter_ip`: IP address of the sender to filter packets.
- `interval`: Time interval between each bit (default is 0.5 seconds).

## Cisco Packet Tracer Setup

Use Cisco Packet Tracer to create a network environment consisting of sender and receiver devices. Configure the network interfaces, IP addresses, and connectivity between the devices.

## Example

```python
python timing_channel_sender.py
python timing_channel_receiver.py
```

## Notes

- Adjust the timing interval (`interval`) based on network latency and desired stealthiness.
- Ensure that the sender and receiver devices are correctly configured in the Cisco Packet Tracer environment.

## Disclaimer

This script is for educational purposes only. Any unauthorized or malicious use is not encouraged. Ensure compliance with legal and ethical guidelines while using this tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
