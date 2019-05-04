from Cenario import *
import pygame

class Poder(Cenario):
    def __init__(self, x, y, imagem, tipo, vel):
        super().__init__(x, y, imagem, tipo, vel)


    def atualizar(self, game):
        self.atualizacaoBasica()


    # verifica as colisoes do personagem com os poderes
    def checarColisoes(self, telaDeJogo):
        # incrementar a variavel inteira telaDeJogo.jogador.poderes  caso ocorra a colisao do personagem com o poder
        # fazer o poder desaparecer depois da colisao
        """TODO"""
        pass