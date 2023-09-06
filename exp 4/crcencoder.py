# CRC encoder
def crc_encode():
    data = input("Enter the dataword to be transmitted: ")
    divisor = input("Enter the divisor: ")

    data = [int(bit) for bit in data]  # Convert input data to a list of integers
    divisor = [int(bit) for bit in divisor]  # Convert divisor to a list of integers

    for i in range(len(divisor) - 1):
        data.append(0)

    for i in range(len(data) - len(divisor) + 1):
        if data[i] == 1:
            for j in range(len(divisor)):
                data[i + j] ^= divisor[j]  # Perform XOR operation

    crc_result = data[-len(divisor) + 1:]
    transmitted_data = data + crc_result

    print("CRC: ", end="")
    print(crc_result)
    print("Transmitted data: ", end="")
    print(transmitted_data)

# CRC decoder
def crc_decode():
    received_data = input("Enter the received codeword: ")
    divisor = input("Enter the divisor: ")

    received_data = [int(bit) for bit in received_data]  # Convert received data to a list of integers
    divisor = [int(bit) for bit in divisor]  # Convert divisor to a list of integers

    for i in range(len(divisor) - 1):
        received_data.append(0)

    for i in range(len(received_data) - len(divisor) + 1):
        if received_data[i] == 1:
            for j in range(len(divisor)):
                received_data[i + j] ^= divisor[j]  # Perform XOR operation

    remainder = received_data[-len(divisor) + 1:]

    has_error = any(bit == 1 for bit in remainder)
    if has_error:
        print("Error in received data")
    else:
        print("No error in received data")

    print("Received CRC: ", end="")
    print(remainder)

crc_encode()
crc_decode()
