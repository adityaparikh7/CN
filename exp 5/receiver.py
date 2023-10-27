import socket

# Function to simulate Go-Back-N ARQ at the receiver
def receiver(window_size, port):
    frames_received = 0

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('0.0.0.0', port))

        while True:
            data, addr = s.recvfrom(1024)
            frame = data.decode()
            frames_received += 1

            if frames_received <= window_size:
                print(f"Received {frame}")
            else:
                print(f"Discarded {frame}")

# Input from user
window_size = int(input("Enter the window size: "))
port = 12345  # Port number for the receiver

# Run receiver
receiver(window_size, port)
