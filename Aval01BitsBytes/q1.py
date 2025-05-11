


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

