def calculate_checksum(data):
    checksum = 0
    for i in range(0, len(data), 2):
        chunk = data[i:i+2]
        checksum += int.from_bytes(chunk, byteorder='big', signed=False)
        checksum = (checksum & 0xFFFF) + (checksum >> 16)
    return ~checksum & 0xFFFF

def sender():
    data = input("Enter data to send: ").encode('utf-8')
    checksum = calculate_checksum(data)
    data_with_checksum = data + checksum.to_bytes(2, 'big')
    print("Sending data with checksum: {}".format(data_with_checksum.hex()))

def receiver():
    received_data_hex = input("Enter received data (hex): ")
    received_data = bytes.fromhex(received_data_hex)
    received_checksum = received_data[-2:]
    received_data = received_data[:-2]
    calculated_checksum = calculate_checksum(received_data)
    if received_checksum == calculated_checksum.to_bytes(2, 'big'):
        print("Receiver Checksum is equal to 0.")
        print("Received Data: {}".format(received_data.decode('utf-8')))
    else:
        print("Receiver Checksum is not equal to 0. Therefore,")
        print("ERROR DETECTED")

if __name__ == "__main__":
    print("\nSender Side:")
    sender()

    print("\nReceiver Side:")
    receiver()
