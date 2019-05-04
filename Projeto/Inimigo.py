from Cenario import *
import pygame

class Inimigo(Cenario):
    def __init__(self, x, y, imagem, tipo, vel):
        super().__init__(x, y, imagem, tipo, vel)
        self.vida = 3


    def atualizar(self, game):
        # fazer o inimigo pular para cima e para baixo incessantemente para que ele tenha algum
        # tipo de movimento e, portanto, seja possivel diferencia-lo dos inimigos
        """TODO"""
        pass


    # verifica as colisoes do personagem com o inimigo
    def checarColisoes(self, telaDeJogo):
        # lembrar que se o personagem tiver vidas e se chocar contra inimigos, ele nao deve morrer mas sim perder uma vida
        # lembrar que se a booleana telaDeJogo.jogador.ehInvencivel for verdadeira as colisoes com inimigos devem ser ignoradas
        # lembrar que se a booleana telaDeJogo.jogador.cresceu for verdadeira as colisoes com inimigos devem apenas levar esta booleana
        # a se tornar falsa, de modo que o jogador voltara a ser pequeno
        """TODO"""
        pass
