import random

# Function to simulate Go-Back-N ARQ
def go_back_n_arq(window_size, frame_count, lost_frame_number):
    frames = [f"{i:04b}" for i in range(frame_count)]
    sender_window = frames[:window_size]
    receiver_window = []
    
    print("Sender Window: ", sender_window)
    print("Receiver Window: ", receiver_window)
    
    for i in range(frame_count):
        if i < lost_frame_number:
            print(f"Transmitting Frame {frames[i]}")
        else:
            print(f"Frame {frames[i]} is lost.")
        
        if i >= window_size:
            sender_window.pop(0)
            sender_window.append(frames[i])
        
        if i >= lost_frame_number:
            print(f"Retransmitting Frame {frames[i]}")
        
        receiver_window.append(frames[i])
        if len(receiver_window) == window_size:
            print("Receiver received frames:", receiver_window)
            receiver_window = []
        print("-" * 30)

# Input from user
window_size = int(input("Enter the window size: "))
frame_count = int(input("Enter the total number of frames: "))
lost_frame_number = int(input("Enter the frame number to be lost: "))

# Run Go-Back-N ARQ simulation
go_back_n_arq(window_size, frame_count, lost_frame_number)
