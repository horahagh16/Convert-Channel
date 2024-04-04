import os
import time

def write_covert_data(file_path, binary_data):
    """Write covert data using file modification times."""
    for bit in binary_data:
        if bit == '1':
            os.utime(file_path, None)  # Update file modification time
        time.sleep(1)  # Wait a second to distinguish between bits

def read_covert_data(file_path, data_length):
    """Read covert data from file modification times."""
    mod_times = []
    for _ in range(data_length):
        mod_time = os.path.getmtime(file_path)
        mod_times.append(mod_time)
        time.sleep(1)  # Matching the write delay

    binary_data = ''
    prev_time = mod_times[0]
    for mod_time in mod_times[1:]:
        if mod_time - prev_time >= 1:
            binary_data += '1'
        else:
            binary_data += '0'
        prev_time = mod_time

    return binary_data

# Example usage: Requires an actual file and adjustments based on your system's time resolution.
# file_path = "path_to_a_test_file.txt"
# binary_data = covert_message_to_binary("Hi")
# write_covert_data(file_path, binary_data)
# print(read_covert_data(file_path, len(binary_data)))


def send_timing_channel_message(message, interval=0.5):
    """Send a message using timing intervals. 0.5 seconds for '0', 1 second for '1'."""
    for char in message:
        if char == '1':
            time.sleep(interval * 2)  # Wait longer for '1'
        else:
            time.sleep(interval)  # Shorter wait for '0'
        print(".", end="", flush=True)  # Representing a packet being sent

def covert_message_to_binary(message):
    """Convert a message to binary."""
    return ''.join(format(ord(c), '08b') for c in message)

# Example Usage:
binary_message = covert_message_to_binary("Hi")
send_timing_channel_message(binary_message)
