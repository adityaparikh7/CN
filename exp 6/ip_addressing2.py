import ipaddress

def classful_ip_address(ip_str):
    try:
        ip = ipaddress.IPv4Address(ip_str)
        if ip.is_private:
            print(f'{ip_str} is a private IP address.')
        else:
            first_octet = int(ip.exploded.split('.')[0])
            if 1 <= first_octet <= 126:
                print(f'{ip_str} belongs to Class A.')
            elif first_octet == 127:
                print(f'{ip_str} is a loopback address.')
            elif 128 <= first_octet <= 191:
                print(f'{ip_str} belongs to Class B.')
            elif 192 <= first_octet <= 223:
                print(f'{ip_str} belongs to Class C.')
            else:
                print(f'{ip_str} belongs to Class D or E.')
    except ipaddress.AddressValueError:
        print(f'Invalid IP address: {ip_str}')

def classless_ip_address(ip_str, subnet_mask_str):
    try:
        ip = ipaddress.IPv4Network(f'{ip_str}/{subnet_mask_str}', strict=False)
        if ip.is_private:
            print(f'{ip_str}/{subnet_mask_str} is a private IP address.')
        else:
            print(f'{ip_str}/{subnet_mask_str} is a classless IP address.')
    except ipaddress.AddressValueError:
        print(f'Invalid IP address or subnet mask: {ip_str}/{subnet_mask_str}')

def assign_subnet_mask(ip_str):
    try:
        ip = ipaddress.IPv4Address(ip_str)
        if ip.is_private:
            print(f'{ip_str} is a private IP address.')
        else:
            first_octet = int(ip.exploded.split('.')[0])
            if 1 <= first_octet <= 127:
                subnet_mask = '255.0.0.0'
            elif 128 <= first_octet <= 191:
                subnet_mask = '255.255.0.0'
            elif 192 <= first_octet <= 223:
                subnet_mask = '255.255.255.0'
            else:
                subnet_mask = 'N/A (Class D or E)'
            
            print(f'Assigned subnet mask for {ip_str} is {subnet_mask}')
    except ipaddress.AddressValueError:
        print(f'Invalid IP address: {ip_str}')

# User input for classful IP address
classful_ip_input = input("Enter a classful IP address (e.g., 192.168.1.1): ")
classful_ip_address(classful_ip_input)
assign_subnet_mask(classful_ip_input)


# User input for classless IP address and subnet mask
classless_ip_input = input("Enter a classless IP address (e.g., 192.168.1.0): ")
subnet_mask_input = input("Enter the subnet mask (e.g., 255.255.255.0): ")
classless_ip_address(classless_ip_input, subnet_mask_input)
assign_subnet_mask(classless_ip_input)

exit()