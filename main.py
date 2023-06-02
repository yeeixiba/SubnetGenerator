import json
from generate_config import create_configuration_file
from subnet_utils import generate_subnet_details

if __name__ == '__main__':
    try:
        # Get user input separated by tabs or commas
        input_data = input("Enter the subnet details separated by tabs or commas (Subnet Name, Zone Name, VLAN ID, "
                           "Subnet CIDR): ")
        if "\t" in input_data:
            subnet_name, zone_name, vlan_id, subnet_cidr = input_data.split("\t")
        elif "," in input_data:
            subnet_name, zone_name, vlan_id, subnet_cidr = input_data.split(",")
        else:
            raise ValueError("Invalid input format. Please separate the values by tabs or commas.")

        # Generate subnet details for wro
        subnet_details_wro = generate_subnet_details(subnet_name, zone_name, vlan_id, subnet_cidr)

        # Generate subnet details for war
        modified_subnet_cidr = '.'.join([subnet_cidr.split('.')[0], str(int(subnet_cidr.split('.')[1]) + 4)]
                                        + subnet_cidr.split('.')[2:])
        subnet_details_war = generate_subnet_details(subnet_name, zone_name, vlan_id, modified_subnet_cidr)

        # Save subnet details to JSON file
        filename = f"{subnet_name}_subnet_details.json"
        with open(filename, "w") as file:
            json.dump({
                "wro_subnet_details": subnet_details_wro,
                "war_subnet_details": subnet_details_war
            }, file, indent=4)

        print(f"Subnet details saved to {filename} successfully!")

        # Create configuration files using generate_config.py
        config_filename_wro = f"{subnet_name}_wro_config.txt"
        create_configuration_file(subnet_details_wro, config_filename_wro)
        print(f"Configuration file '{config_filename_wro}' created successfully!")

        config_filename_war = f"{subnet_name}_war_config.txt"
        create_configuration_file(subnet_details_war, config_filename_war, war_template=True)
        print(f"Configuration file '{config_filename_war}' created successfully!")

    except ValueError as e:
        print(f"Error: {e}")
