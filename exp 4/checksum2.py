def calculate_checksum(data):
    checksum = 0
    for i in range(0, len(data), 2):
        chunk = data[i:i+2]
        chunk_value = int.from_bytes(chunk, byteorder='big', signed=False)
        checksum += chunk_value
        checksum = (checksum & 0xFFFF) + (checksum >> 16)
    return ~checksum & 0xFFFF

def sender():
    data = input("Enter data to send: ")
    
    # Ensure the length of data is even (add padding if needed)
    if len(data) % 2 != 0:
        data += '\x00'  # Add a null byte as padding
    
    checksum = calculate_checksum(data.encode('utf-8'))

    # Combine the data and checksum into a single 16-bit value
    data_with_checksum = (checksum << 16) | int.from_bytes(data.encode('utf-8'), byteorder='big')
    
    print("Sending data with checksum: {:X}".format(data_with_checksum))

def receiver():
    received_data_hex = input("Enter received data with checksum (hex): ")
    received_data = int(received_data_hex, 16)
    
    # Extract the checksum and data
    received_checksum = received_data >> 16
    received_data = received_data & 0xFFFF

    # Calculate the checksum for the received data
    calculated_checksum = calculate_checksum(received_data.to_bytes(2, byteorder='big'))
    
    if received_checksum == calculated_checksum:
        print("Data integrity verified.")
        print("Received Data: {}".format(received_data.to_bytes(2, byteorder='big').decode('utf-8')))
    else:
        print("Data integrity check failed. Data may be corrupted.")

if __name__ == "__main__":
    print("Sender Side:")
    sender()

    print("\nReceiver Side:")
    receiver()
