import ipaddress

def generate_subnet_details(subnet_name, zone_name, vlan_id, subnet_cidr):
    subnet_details = {}

    subnet_details["subnet_name"] = subnet_name
    subnet_details["zone_name"] = zone_name

    # Validate VLAN ID
    try:
        vlan_id = int(vlan_id)
        if vlan_id < 1 or vlan_id > 4095:
            raise ValueError("VLAN ID must be between 1 and 4095.")
    except ValueError:
        raise ValueError("Invalid VLAN ID. Please enter a numeric value.")

    subnet_details["vlan_id"] = vlan_id

    # Validate subnet CIDR format
    try:
        subnet = ipaddress.ip_network(subnet_cidr)
        subnet_address = str(subnet.network_address)
        subnet_netmask = str(subnet.netmask)
    except ValueError:
        raise ValueError("Invalid subnet CIDR format. Please enter a valid CIDR notation.")

    subnet_details["subnet_cidr"] = subnet_cidr

    # Split the subnet CIDR into subnet address and netmask
    subnet_parts = subnet_cidr.split('/')
    subnet_address = subnet_parts[0]
    subnet_netmask = subnet_parts[1]

    subnet_details["subnet_address"] = subnet_address
    subnet_details["subnet_netmask"] = subnet_netmask

    # Calculate the default gateway as the first IP address in the subnet
    octets = subnet_address.split(".")
    octets[-1] = str(int(octets[-1]) + 1)  # Increment the last octet by 1
    default_gateway = ".".join(octets)
    subnet_details["default_gateway"] = default_gateway
    subnet_details["default_gateway_cidr"] = f"{default_gateway}/{subnet_netmask}"

    # Set the location based on the subnet name
    if "CPD" in subnet_name:
        subnet_details["location"] = "CPD"
    elif "zCPD" in subnet_name:
        subnet_details["location"] = "zCPD"

    return subnet_details
