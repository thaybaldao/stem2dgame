from Cenario import *
import pygame

class Moeda(Cenario):
    def __init__(self, x, y, largura, altura, imagem, tipo, num, vel):
        super().__init__(x, y, largura, altura, imagem, tipo, num, vel)

    def atualizar(self, game):
        self.atualizacaoBasica()

    # verifica as colisoes do personagem com as moedas
    def checarColisoes(self, telaDeJogo):
        # aumentar a pontuacao caso ocorra colisao do personagem com a moeda
        # fazer a moeda desaparecer depois da colisao
        pass