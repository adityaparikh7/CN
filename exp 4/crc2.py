import random

def generator(length):
    generator = [1]
    for _ in range(length - 2):
        generator.append(random.randint(0,1))
    generator.append(1)
    return generator

def crc_encode(data, generator_polynomial):
    data = list(data)  
    generator = list(generator_polynomial)
    data.extend([0] * (len(generator) - 1)) 
    for i in range(len(data) - len(generator) + 1):
        if data[i] == 1:
            for j in range(len(generator)):
                data[i + j] ^= generator[j]

    crc_code = data[-(len(generator) - 1):]
    return crc_code

data_input = input("Enter the data bits (0s and 1s): ")
data_bits = [int(bit) for bit in data_input]

generator_length = len(data_bits)  
random_generator = generator(generator_length)

encoded_crc = crc_encode(data_bits, random_generator)
print("Generated Random Generator Polynomial:", random_generator)
print("Encoded CRC:", encoded_crc)