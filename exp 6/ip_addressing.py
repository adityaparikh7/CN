import random

def generate_random_ip():
    ip = []
    for i in range(4):
        ip.append(str(random.randint(0, 255)))
    return ".".join(ip)

def get_ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return 'Class A'
    elif first_octet == 127:
        return 'Loopback Address'
    elif 128 <= first_octet <= 191:
        return 'Class B'
    elif 192 <= first_octet <= 223:
        return 'Class C'
    elif 224 <= first_octet <= 239:
        return 'Class D (Multicast)'
    elif 240 <= first_octet <= 255:
        return 'Class E (Reserved)'
    else:
        return 'Unknown'

def generate_subnet_mask(ip_class):
    if ip_class == 'Class A':
        subnet_mask = '255.0.0.0'
    elif ip_class == 'Class B':
        subnet_mask = '255.255.0.0'
    elif ip_class == 'Class C':
        subnet_mask = '255.255.255.0'
    else:
        subnet_mask = 'N/A (Class D or E)'
    return subnet_mask


random_ip = generate_random_ip()
ip_class = get_ip_class(random_ip)
subnet_mask = generate_subnet_mask(ip_class)

print(f'Random IP Address: {random_ip}')
print(f'Subnet Mask: {subnet_mask}')
print(f'IP Address Class: {ip_class}')
    