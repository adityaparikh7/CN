import socket
import time

# Function to simulate Go-Back-N ARQ at the sender
def sender(window_size, frame_count, lost_frame_number, host, port):
    frames = [f"Frame {i}" for i in range(frame_count)]
    sender_window = frames[:window_size]

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect((host, port))

        for i in range(frame_count):
            if i < lost_frame_number:
                print(f"Transmitting {frames[i]}")
                s.send(frames[i].encode())
            else:
                print(f"{frames[i]} is lost.")
            
            if i >= window_size:
                sender_window.pop(0)
                sender_window.append(frames[i])
            
            if i >= lost_frame_number:
                print(f"Retransmitting {frames[i]}")
                s.send(frames[i].encode())

            time.sleep(1)

# Input from user
window_size = int(input("Enter the window size: "))
frame_count = int(input("Enter the total number of frames: "))
lost_frame_number = int(input("Enter the frame number to be lost: "))
host = '127.0.0.1'  # Receiver's IP address
port = 12345  # Receiver's port number

# Run sender
sender(window_size, frame_count, lost_frame_number, host, port)
