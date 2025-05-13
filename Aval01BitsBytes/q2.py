import hashlib
import time

# Função que busca o nonce válido
def findNonce(data_bytes, bits_zero):
    nonce = 0
    alvo = '0' * bits_zero
    inicio = time.time()

    while True:
        # Concatena os dados com o nonce em bytes
        combinado = data_bytes + nonce.to_bytes(8, 'big')

        # Calcula o hash SHA-256
        hash_hex = hashlib.sha256(combinado).hexdigest()

        # Converte o hash para binário (256 bits)
        hash_bin = bin(int(hash_hex, 16))[2:].zfill(256)

        # Verifica se o início do hash tem os bits zero necessários
        if hash_bin.startswith(alvo):
            tempo = time.time() - inicio
            return nonce, hash_hex, tempo

        nonce += 1

# Casos de teste: (texto, bits_zero)
testes = [
    ("Esse um texto elementar", 8),
    ("Esse um texto elementar", 10),
    ("Esse um texto elementar", 15),
    ("Textinho", 8),
    ("Textinho", 18),
    ("Textinho", 22),
    ("Meu texto médio", 18),
    ("Meu texto médio", 19),
    ("Meu texto médio", 20)
]

# Cabeçalho da tabela
print(f"{'Texto':<25} {'Bits':<5} {'Nonce':<10} {'Hash':<64} {'Tempo (s)':<10}")
print("-" * 120)

# Executa os testes
for texto, bits in testes:
    dados = texto.encode()
    nonce, hash_encontrado, tempo = findNonce(dados, bits)
    print(f"{texto:<25} {bits:<5} {nonce:<10} {hash_encontrado:<64} {tempo:.4f}")