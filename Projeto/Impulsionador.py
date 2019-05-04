from Cenario import *
import pygame

class Impulsionador(Cenario):
    def __init__(self, x, y, imagem, tipo, vel):
        super().__init__(x, y, imagem, tipo, vel)


    def atualizar(self, game):
        self.atualizacaoBasica()


    # verifica as colisoes do personagem com o impulsionador
    def checarColisoes(self, telaDeJogo):
        # fazer a variavel telaDeJogo.jogador.ehInvencivel ser verdadeira caso ocorra a colisao
        # fazer o impulsionador desaparecer depois da colisao
        """"TODO"""
        pass