import random

def crc_encode():
    data = input("Enter the data to be transmitted: ")
    data = list(data)
    
    # Generate a random divisor with first and last bits as 1
    divisor = ['1'] + [str(random.randint(0, 1)) for _ in range(len(data) // 2 - 2)] + ['1']
    
    print("Generated random divisor: ", "".join(divisor))
    
    for i in range(len(divisor)-1):
        data.append('0')
    print("Data after appending zeroes: ", end="")
    print(data)
    
    for i in range(len(data)-len(divisor)+1):
        if data[i] == '1':
            for j in range(len(divisor)):
                if data[i+j] == divisor[j]:
                    data[i+j] = '0'
                else:
                    data[i+j] = '1'
    
    crc = data[len(data)-len(divisor)+1:]
    print("CRC: ", "".join(crc))
    
    # Append the CRC to the transmitted data
    transmitted_data = data + crc
    print("Transmitted data: ", "".join(transmitted_data))

crc_encode()