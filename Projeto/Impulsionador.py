from Cenario import *
import pygame

class Impulsionador(Cenario):
    def __init__(self, x, y, imagem, vel):
        super().__init__(x, y, imagem, vel)


    def atualizar(self, game):
        self.atualizacaoBasica()


    # verifica as colisoes do personagem com o impulsionador
    def checarColisoes(self, telaDeJogo, game):
        # fazer a variavel telaDeJogo.jogador.ehInvencivel ser verdadeira caso ocorra a colisao
        # fazer o impulsionador desaparecer depois da colisao
        if self.rect.colliderect(telaDeJogo.jogador):
            telaDeJogo.jogador.ehInvencivel = True
            telaDeJogo.impulsionadores.pop()