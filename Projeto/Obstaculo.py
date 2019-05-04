from Cenario import *
import pygame

class Obstaculo(Cenario):
    def __init__(self, x, y, imagem, tipo, num, vel):
        super().__init__(x, y, imagem, tipo, num, vel)

    def atualizar(self, game):
        self.atualizacaoBasica()

    # verifica as colisoes do personagem principal com obstaculos do cenario
    def checarColisoes(self, telaDeJogo):
        # lembrar que se o personagem tiver vidas e se chocar contra obstaculos, ele nao deve morrer mas sim perder uma vida
        # lembrar que se a booleana self.ehInvencivel for verdadeira as colisoes com obstaculos devem ser ignoradas
        # lembrar que se a booleana self.cresceu for verdadeira as colisoes com obstaculos devem levar apenas a booleana
        # self.cresceu a se tornar falsa, de modo que o jogador voltara a ser pequeno
        pass