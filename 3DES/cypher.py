# Import necessário para o funcionamento do código (instalado via "pip install pydes")
from pyDes import *


class Cypher:
    # Função construtora da classe
    def __init__(self, key):
        # Cria uma classe que pode criptografar ou decriptograr usando a chave, o outro argumento é só pra não se preocupar com padding
        self.cypher = triple_des(key, padmode=PAD_PKCS5)

    # Função que retorna mensagem criptografada
    def encrypt(self, message):
        return self.cypher.encrypt(message.encode())

    # Função que retorna mensagem decriptografada
    def decrypt(self, message):
        return self.cypher.decrypt(message).decode('utf-8')
