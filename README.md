# Timing Channel Communication

This Python script facilitates covert communication between two endpoints using timing channels. A timing channel is a covert communication channel where information is conveyed through variations in the timing of events. This method can be used for stealthy communication between systems.

## Prerequisites

- Python 3.x
- Basic understanding of socket programming

## Installation

Clone the repository:

```bash
git clone https://github.com/horahagh16/Convert-Channel.git
```

Navigate to the directory:

```bash
cd Convert-Channel
```

## Usage

1. Replace `target_ip` in `timing_channel_thread.py` with the IP address of the receiver.
2. Replace `target_port` with the desired port for communication.
3. Execute the script using the command:

```bash
python timing_channel_thread.py
```

## Example

```bash
python timing_channel_thread.py
```

## Guide

### Sender Function (`send_timing_channel_message`)

This function sends a message over the timing channel to the specified IP address and port. It uses threading to send the message efficiently.

```python
send_timing_channel_message(message, target_ip, target_port, interval=0.5)
```

- `message`: The message to be sent.
- `target_ip`: IP address of the receiver.
- `target_port`: Port number for communication.
- `interval`: Time interval between each bit (default is 0.5 seconds).

### Receiver Function (`listen_for_timing_channel_messages`)

This function listens for messages on the specified port and decodes them based on timing intervals.

```python
listen_for_timing_channel_messages(port, interval=0.5)
```

- `port`: Port number for communication.
- `interval`: Time interval between each bit (default is 0.5 seconds).

### Main Function (`main`)

The main function demonstrates an example usage of the sender and receiver functions. It initializes sender and receiver threads and starts them to send and receive messages concurrently.

### Conversion Function (`convert_message_to_binary`)

This function converts a regular text message into binary format.

## Notes

- Adjust the timing interval (`interval`) based on network latency and desired stealthiness.
- Ensure that the sender and receiver are using the same timing intervals for accurate communication.

## Disclaimer

This script is for educational purposes only. Any unauthorized or malicious use is not encouraged. Ensure compliance with legal and ethical guidelines while using this tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
