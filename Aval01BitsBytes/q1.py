


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

# CÁLCULO DO ENDEREÇO DA REDE, BROADCAST E HOSTS
def calcular_dados_rede(ip_str, intMask):
    ip = ip_str_to_int(ip_str)

    # Máscara
    mascara = ((1 << intMask) - 1) << (32 - intMask) #A primeira parte gera tudo 1 para rede e  a segunda 0 pros hosts
    
    # Endereço da rede
    rede = ip & mascara # O endereço da rede é obtido aplicando a operação AND entre o IP e a máscara
    
    # Broadcast
    broadcast = rede | (~mascara) # O endereço de broadcast é obtido aplicando a operação OR entre o endereço da rede 
                                               #e o complemento da máscara
    
    # Cálculo do Gateway e IPs utilizáveis
    if intMask == 32:
        primeiro = ultimo = rede                # O endereço da rede e o broadcast são iguais
        total_hosts = 1
    elif intMask == 31:
        primeiro = rede                         # O primeiro IP utilizável é o endereço da rede     
        ultimo = broadcast                      # O último IP utilizável é o broadcast
        total_hosts = 2
    else:                                       # O primeiro, último IP utilizável e gateway são obtidos a partir do endereço da rede e do broadcast
        primeiro = rede + 1
        ultimo = broadcast - 2
        gateway = broadcast - 1
        total_hosts = (1 << (32 - intMask)) - 2

    # Resultado formatado
    return {
        "a) Endereço da rede": int_to_ip_str(rede),
        "b) Broadcast": int_to_ip_str(broadcast),
        "c) Gateway": int_to_ip_str(gateway),
        "d) Total de hosts utilizáveis": total_hosts,
        "Primeiro IP utilizável": int_to_ip_str(primeiro),
        "Último IP utilizável": int_to_ip_str(ultimo),
    }
# RETORNO DOS RESULTADOS
resultado = calcular_dados_rede(ip_str, intMask)
for chave, valor in resultado.items():
    print(f"{chave}: {valor}")