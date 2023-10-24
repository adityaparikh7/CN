import ipaddress
import random

def generate_random_ip():
    ip = []
    for i in range(4):
        ip.append(str(random.randint(0, 255)))
    return ".".join(ip)
    

def subnet_calculator(ip, subnet_mask):
    network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)

    print(f"Network Address: {network.network_address}")
    print(f"Netmask: {network.netmask}")
    print(f"Broadcast Address: {network.broadcast_address}")
    print(f"Number of Hosts: {network.num_addresses - 2}")

    subnets = list(network.subnets())
    for i, subnet in enumerate(subnets):
        print(f"\nSubnet {i + 1}:")
        print(f"Subnet Address: {subnet.network_address}")
        print(f"Subnet Mask: {subnet.netmask}")
        print(f"Broadcast Address: {subnet.broadcast_address}")
        print(f"Usable IP Range: {subnet.network_address + 1} - {subnet.broadcast_address - 1}")
        print(f"Number of Hosts: {subnet.num_addresses - 2}")

if __name__ == "__main__":
    ip = generate_random_ip()
    subnet_mask = input("Enter subnet mask in CIDR notation (e.g., 24): ")
    #only till 32

    subnet_calculator(ip, subnet_mask)
