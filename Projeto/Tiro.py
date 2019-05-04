from Cenario import *
import pygame

class Tiro(Cenario):
    def __init__(self, x, y, imagem, tipo, vel):
        super().__init__(x, y, imagem, tipo, vel)

    # atualiza a posicao do tiro apos disparado
    def atualizar(self, game):
        """TODO"""
        pass


    # verifica as colisoes do tiro com o inimigo
    def checarColisoes(self, telaDeJogo):
        # decrementa a variavel telaDeJogo.inimigo.vida a cada colisao do tiro com o inimigo
        # fazer o tiro desaparecer a cada colisao dele com o inimigo
        # fazer o inimigo desaparecer apos telaDeJogo.inimigo.vida ser zero
        """TODO"""
        pass