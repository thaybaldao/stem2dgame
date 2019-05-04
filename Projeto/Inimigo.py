from Cenario import *
import pygame

class Inimigo(Cenario):
    def __init__(self, x, y, imagem, tipo, num, vel):
        super().__init__(x, y, imagem, tipo, num, vel)
        self.vida = 3

    def atualizar(self, game):
        # fazer o inimigo ter algum tipo de movimento, a fim de diferencia-lo dos obstaculos
        pass

    # verifica as colisoes do personagem com o inimigo
    def checarColisoes(self, telaDeJogo):
        # lembrar que se o personagem tiver vidas e se chocar contra inimigos, ele nao deve morrer mas sim perder uma vida
        # lembrar que se a booleana self.ehInvencivel for verdadeira as colisoes com inimigos devem ser ignoradas
        # lembrar que se a booleana self.cresceu for verdadeira as colisoes com inimigos devem levar apenas a booleana
        # self.cresceu a se tornar falsa, de modo que o jogador voltara a ser pequeno
        pass
