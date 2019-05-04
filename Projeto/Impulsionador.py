from Cenario import *
import pygame

class Impulsionador(Cenario):
    def __init__(self, x, y, largura, altura, imagem, tipo, num, vel):
        super().__init__(x, y, largura, altura, imagem, tipo, num, vel)

    def atualizar(self, game):
        self.atualizacaoBasica()

    # verifica as colisoes do personagem com o impulsionador
    def checarColisoes(self, telaDeJogo):
        # fazer a variavel jogador.ehInvencivel ser verdadeira
        # fazer o impulsionador desaparecer depois da colisao
        pass