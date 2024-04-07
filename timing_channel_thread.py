import socket
import time
import threading

# Sender function with threading
def send_timing_channel_message(message, target_ip, target_port, interval=0.5):
    start_time = time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((target_ip, target_port))
        for char in message:
            if char == '1':
                time.sleep(interval * 2)
            else:
                time.sleep(interval)
            s.sendall(b'.')
        end_time = time.time()
    time_taken = end_time - start_time
    # Calculate the speed in bits per second
    speed = len(message) / time_taken
    print(f"Speed of data changing bits per second: {speed:.2f}")


# Receiver function with threading
def listen_for_timing_channel_messages(port, interval=0.5):
    binary_message = ''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            start_time = time.time()
            while True:
                data = conn.recv(1)
                if not data:
                    break
                end_time = time.time()
                # Decode the bit based on the timing interval
                if end_time - start_time >= interval * 1.5:
                    binary_message += '1'
                else:
                    binary_message += '0'
                start_time = time.time()
    # Convert the binary message back to a string
    message = ''.join(chr(int(binary_message[i:i+8], 2)) 
                      for i in range(0, len(binary_message), 8))
    print(f"Decoded message: {message}")

# Convert message to binary
def covert_message_to_binary(message):
    return ''.join(format(ord(c), '08b') for c in message)

# Example usage with threading
def main():
    target_ip = '192.168.1.195'  # Replace with the receiver's IP address
    target_port = 12377  # Replace with the port you want to use
    message = "Hello, World!"
    binary_message = covert_message_to_binary(message)

    # Create threads for sending and receiving messages
    sender_thread = threading.Thread(target=send_timing_channel_message, args=(binary_message, target_ip, target_port))
    receiver_thread = threading.Thread(target=listen_for_timing_channel_messages, args=(target_port,))

    # Start the threads
    sender_thread.start()
    receiver_thread.start()

    # Wait for both threads to complete
    sender_thread.join()
    receiver_thread.join()

if __name__ == "__main__":
    main()
