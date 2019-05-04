from Cenario import *
import pygame

class Tiro(Cenario):
    def __init__(self, x, y, largura, altura, imagem, tipo, num, vel):
        super().__init__(x, y, largura, altura, imagem, tipo, num, vel)

    def atualizar(self, game):
        pass

    # verifica as colisoes do tiro com o inimigo
    def checarColisoes(self, telaDeJogo):
        # decrementa a variavel inimigo.vida a cada colisao do tiro com o inimigo
        # fazer o tiro desaparecer a cada colisao dele com o inimigo
        # fazer o inimigo desaparecer apos inimigo.vida ser zero
        pass