# Description: This program will calculate the number of subnetworks and the maximum number of computers in each subnetwork and the addresses of each subnetwork. It takes input as IP address and subnet mask and number of subnetworks.

import math

# Get the IP address and subnet mask from the user
ip_address = input("Enter the IP address and subnet mask (e.g. 193.16.16.0/24): ")
ip, subnet_mask = ip_address.split("/")
subnet_mask = int(subnet_mask)

# Get the number of subnetworks from the user
num_subnets = int(input("Enter the number of subnetworks: "))

# Calculate the new netmask
bits_needed = int(math.ceil(math.log(num_subnets, 2)))
new_subnet_mask = subnet_mask + bits_needed

# Calculate the maximum number of computers in each subnet
max_computers = 2 ** (32 - new_subnet_mask) - 2

# Split the IP address into its octets
octets = ip.split(".")

# Calculate the address of each subnetwork
subnet_addresses = []
for i in range(num_subnets):
    subnet_octets = octets[:3]
    subnet_octets.append(str(i * 64))
    subnet_addresses.append(".".join(subnet_octets) + "/" + str(new_subnet_mask))

# Print the results
print("New netmask: /" + str(new_subnet_mask))
print("Maximum number of computers in each subnet: " + str(max_computers))
print("Addresses of each subnetwork:")
for subnet in subnet_addresses:
    print(subnet)
