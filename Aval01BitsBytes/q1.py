


# AQUISIÇÃO DE DADOS (IP E MÁSCARA)
strIp = input("Informe o numero de IP: ")
intMask = int(input("Informe a máscara de sub-rede (CIDR = 18): "))

# CÁLCULO DO NÚMERO DE HOSTS
hostsBits = 32 - intMask

# CÁLCULO DO NÚMERO DE SUB-REDES

# CÁLCULO DO NÚMERO DE HOSTS
hosts_Net = (2 ** hostsBits)- 2
print("Número de hosts: ", hosts_Net)

ip = 0
for num in strIp.split('.'):
    ip = (ip << 8) | int(num)
    print(ip)
print("IP: ", ip)