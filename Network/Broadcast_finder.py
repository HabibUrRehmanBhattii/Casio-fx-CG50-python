def get_broadcast_ip(ip_address_cidr):
    ip_address, cidr = ip_address_cidr.split("/")
    ip_address_binary = (bin(int(ip_address.split(".")[0]))[2:] + "0"*(8-len(bin(int(ip_address.split(".")[0]))[2:])) + 
                         bin(int(ip_address.split(".")[1]))[2:] + "0"*(8-len(bin(int(ip_address.split(".")[1]))[2:])) + 
                         bin(int(ip_address.split(".")[2]))[2:] + "0"*(8-len(bin(int(ip_address.split(".")[2]))[2:])) + 
                         bin(int(ip_address.split(".")[3]))[2:] + "0"*(8-len(bin(int(ip_address.split(".")[3]))[2:])))
    host_bits = 32 - int(cidr)
    broadcast_ip_binary = ip_address_binary[:32-host_bits] + '1'*host_bits
    broadcast_ip = str(int(broadcast_ip_binary[:8], 2)) + '.' + str(int(broadcast_ip_binary[8:16], 2)) + '.' + str(int(broadcast_ip_binary[16:24], 2)) + '.' + str(int(broadcast_ip_binary[24:], 2))
    return broadcast_ip

print(get_broadcast_ip("120.178.32.99/24")) #120.178.32.255
