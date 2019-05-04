from Cenario import *
import pygame

class Crescimento(Cenario):
    def __init__(self, x, y, imagem, tipo, num, vel):
        super().__init__(x, y, imagem, tipo, num, vel)

    def atualizar(self, game):
        self.atualizacaoBasica()

    # verifica as colisoes do personagem com as moedas
    def checarColisoes(self, telaDeJogo):
        # setar a variavel jogador.cresceu para True
        # fazer o crescimento desaparecer depois da colisao
        pass