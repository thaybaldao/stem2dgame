from Cenario import *
import pygame

class Obstaculo(Cenario):
    def __init__(self, x, y, imagem, tipo, vel):
        super().__init__(x, y, imagem, tipo, vel)


    def atualizar(self, game):
        self.atualizacaoBasica()


    # verifica as colisoes do personagem principal com obstaculos do cenario
    def checarColisoes(self, telaDeJogo, game):
        # lembrar que se o personagem tiver vidas e se chocar contra os obstaculos, ele nao deve morrer mas sim perder uma vida
        # lembrar que se a booleana telaDeJogo.jogador.ehInvencivel for verdadeira as colisoes com obstaculos devem ser ignoradas
        # lembrar que se a booleana telaDeJogo.jogador.cresceu for verdadeira as colisoes com obstaculos devem apenas levar esta
        # booleana a se tornar falsa, de modo que o jogador voltara a ser pequeno
        if self.rect.colliderect(telaDeJogo.jogador):
            if telaDeJogo.jogador.ehInvencivel == True:
                telaDeJogo.obstaculos.pop()
            else:
                if telaDeJogo.jogador.cresceu == True:
                    telaDeJogo.obstaculos.pop()
                    telaDeJogo.jogador.cresceu = False
                else:
                    telaDeJogo.obstaculos.pop()
                    telaDeJogo.jogador.vidasExtra -= 1