# import ipaddress
# import random

# def generate_random_ip():
#     ip = []
#     for i in range(4):
#         ip.append(str(random.randint(0, 255)))
#     return ".".join(ip)
    

# def subnet_calculator(ip, subnet_mask):
#     network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)

#     print(f"Network Address: {network.network_address}")
#     print(f"Netmask: {network.netmask}")
#     print(f"Broadcast Address: {network.broadcast_address}")
#     print(f"Number of Hosts: {network.num_addresses - 2}")

#     subnets = list(network.subnets())
#     for i, subnet in enumerate(subnets):
#         print(f"\nSubnet {i + 1}:")
#         print(f"Subnet Address: {subnet.network_address}")
#         print(f"Subnet Mask: {subnet.netmask}")
#         print(f"Broadcast Address: {subnet.broadcast_address}")
#         print(f"Usable IP Range: {subnet.network_address + 1} - {subnet.broadcast_address - 1}")
#         print(f"Number of Hosts: {subnet.num_addresses - 2}")

# if __name__ == "__main__":
#     ip = generate_random_ip()
#     subnet_mask = input("Enter subnet mask in CIDR notation (e.g., 24): ")
#     #only till 32

#     subnet_calculator(ip, subnet_mask)


# import ipaddress

# def subnet_calculator(ip, num_subnets):
#     ip = ipaddress.IPv4Address(ip)

#     # Calculate the subnet mask length based on the number of subnets
#     subnet_mask_length = 32 - num_subnets.bit_length()

#     if subnet_mask_length < 0 or subnet_mask_length > 32:
#         print("Invalid number of subnets.")
#         return

#     # Calculate the subnet mask as an IPv4Address object
#     subnet_mask = ipaddress.IPv4Address('255.255.255.255') - (2 ** (32 - subnet_mask_length) - 1)

#     # Calculate the network
#     network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)

#     print(f"IP Address: {ip}")
#     print(f"Subnet Mask: {subnet_mask}")
#     print(f"Network Address: {network.network_address}")
#     print(f"Broadcast Address: {network.broadcast_address}")
#     print(f"Number of Hosts per Subnet: {network.num_addresses - 2}")

#     # Calculate and display subnets
#     subnets = list(network.subnets(new_prefix=subnet_mask_length))
#     for i, subnet in enumerate(subnets):
#         print(f"\nSubnet {i + 1}:")
#         print(f"Subnet Address: {subnet.network_address}")
#         print(f"Broadcast Address: {subnet.broadcast_address}")
#         print(f"Usable IP Range: {subnet.network_address + 1} - {subnet.broadcast_address - 1}")
#         print(f"Number of Hosts: {subnet.num_addresses - 2}")

# if __name__ == "__main__":
#     ip = input("Enter an IP address (e.g., 192.168.1.1): ")
#     num_subnets = int(input("Enter the number of subnets: "))

#     subnet_calculator(ip, num_subnets)


import ipaddress

def calculate_subnet(ip, num_subnets):
    ip = ipaddress.IPv4Address(ip)

    # Calculate the subnet mask length based on the number of subnets
    subnet_mask_length = 32 - num_subnets.bit_length()

    if subnet_mask_length < 0 or subnet_mask_length > 30:
        print("Invalid number of subnets. Must be between 1 and 30.")
        return

    # Calculate the subnet mask as an IPv4Address object
    subnet_mask = ipaddress.IPv4Address('255.255.255.255') - (2 ** (32 - subnet_mask_length) - 1)

    # Calculate the network
    network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)

    print(f"IP Address: {ip}")
    print(f"Subnet Mask: {subnet_mask}")
    print(f"Network Address (Subnet Address): {network.network_address}")
    print(f"Broadcast Address: {network.broadcast_address}")
    print(f"Number of Hosts per Subnet: {network.num_addresses - 2}")

    # Calculate and display subnets
    subnets = list(network.subnets(new_prefix=subnet_mask_length))
    for i, subnet in enumerate(subnets):
        print(f"\nSubnet {i + 1}:")
        print(f"Subnet Address: {subnet.network_address}")
        print(f"Broadcast Address: {subnet.broadcast_address}")
        print(f"IP Range: {subnet.network_address + 1} - {subnet.broadcast_address - 1}")
        print(f"Usable IP Range: {subnet.network_address} - {subnet.broadcast_address}")
        print(f"Number of Hosts: {subnet.num_addresses - 2}")

if __name__ == "__main__":
    ip = input("Enter an IP address (e.g., 192.168.1.1): ")
    num_subnets = int(input("Enter the number of subnets (till 32): "))

    calculate_subnet(ip, num_subnets)

