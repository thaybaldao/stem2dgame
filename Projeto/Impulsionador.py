from Cenario import *
import pygame

class Impulsionador(Cenario):
    def __init__(self, x, y, imagem, vel):
        super().__init__(x, y, imagem, vel)

    def atualizar(self, game):
        self.atualizacaoBasica()

    # verifica as colisoes do personagem principal com o impulsionador
    def checarColisoes(self, game):
        # fazer a variavel game.ehInvencivel ser verdadeira caso ocorra a colisao entre o personagem principal e o impulsionador
        # fazer o impulsionador desaparecer depois da colisao
        pass
