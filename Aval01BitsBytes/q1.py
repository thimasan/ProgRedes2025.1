


# AQUISIÇÃO DE DADOS (IP E MÁSCARA)
ip_str = input("Informe o numero de IP: ")
intMask = int(input("Informe a máscara de sub-rede (CIDR = 18): "))

# CONVERSÃO DO IP PARA INTEIRO
def ip_str_to_int(ip_str): # Converte o IP em string para inteiro
    octetos = ip_str.split('.') # Divide o IP em octetos
    ip_int = 0
    for octeto in octetos:
        ip_int = (ip_int << 8) | int(octeto) # Converte cada octeto para inteiro e desloca 8 bits para a esquerda
    return ip_int

# CONVERSÃO DO IP_INTEIRO PARA STRING
def int_to_ip_str(ip_int): #Converte o número inteiro de volta para uma string no formato xxxx.xxxx.xxxx.xxxx
    octetos = []            #lista para armazenar os octetos
    for i in range(4):
        octetos.insert(0, str(ip_int & 0xFF)) # Extrai o último octeto
        ip_int = ip_int >> 8 # Desloca 8 bits para a direita
    return '.'.join(octetos)

print(ip_str_to_int(ip_str)) # Converte o IP em string para inteiro
print(int_to_ip_str(ip_str_to_int(ip_str))) # Converte o IP inteiro de volta para string
