from Cenario import *
import pygame

class Obstaculo(Cenario):
    def __init__(self, x, y, imagem, vel):
        super().__init__(x, y, imagem, vel)


    def atualizar(self, game):
        self.atualizacaoBasica()


    # verifica as colisoes do personagem principal com obstaculos do cenario
    def checarColisoes(self, telaDeJogo, game):
        # lembrar que se o personagem tiver vidas e se chocar contra os obstaculos, ele nao deve morrer mas sim perder uma vida
        # lembrar que se a booleana telaDeJogo.jogador.ehInvencivel for verdadeira as colisoes com obstaculos devem ser ignoradas
        if self.rect.colliderect(telaDeJogo.jogador):
            if telaDeJogo.jogador.ehInvencivel == True:
                telaDeJogo.inimigos.pop()
            else:
                if telaDeJogo.jogador.vidasExtra > 0:
                    telaDeJogo.inimigos.pop()
                    telaDeJogo.jogador.vidasExtra -= 1
                else:
                    game.telaAtual = 'Tela de Fim'