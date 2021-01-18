from cypher import *

if __name__ == '__main__':
    # Recebe a mensagem
    msg = input("Digite sua mensagem que queira criptografar: ")
    # Recebe a chave
    key = input("Digite sua chave (String de tamanho de 16 ou 24): ")
    # Cria a classe enviando a chave
    c = Cypher(key.encode())
    # Mostra a chave pra enviar pro destinatário
    print(
        f'Chave para descriptografar: {key}')
    # Criptografa a mensagem que foi recebida
    msg = c.encrypt(msg)
    # Mostra a mensagem que é pra enviar pro destinatário
    print(f'Texto criptografado: {msg}')
    # Mostra como ocorre o processo inverso(descriptografar)
    print(f'Mensagem descriptografada: {c.decrypt(msg)}')
