from Cenario import *
import pygame

class Crescimento(Cenario):
    def __init__(self, x, y, imagem, tipo, vel):
        super().__init__(x, y, imagem, tipo, vel)


    def atualizar(self, game):
        self.atualizacaoBasica()


    # verifica as colisoes do personagem com o icone de crescimento
    def checarColisoes(self, telaDeJogo):
        # fazer a variavel telaDeJogo.jogador.cresceu ser verdadeira caso ocorra a colisao
        # fazer o icone de crescimento desaparecer depois da colisao
        """TODO"""
        pass