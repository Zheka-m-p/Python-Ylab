def int32_to_ip(int32):
    ip_1 = int32 // 256**3
    ip_2 = int32 % 256**3 // 256**2
    ip_3 = int32 % 256**3 % 256**2 // 256
    ip_4 = int32 % 256**3 % 256**2 % 256
    ipv4 = map(str, [ip_1, ip_2, ip_3, ip_4])
    return '.'.join(ipv4)
