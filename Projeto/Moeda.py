from Cenario import *
import pygame

class Moeda(Cenario):
    def __init__(self, x, y, imagem, tipo, vel):
        super().__init__(x, y, imagem, tipo, vel)


    def atualizar(self, game):
        self.atualizacaoBasica()


    # verifica as colisoes do personagem com as moedas
    def checarColisoes(self, telaDeJogo):
        # aumentar a pontuacao caso ocorra colisao do personagem com a moeda (trabalhe com o score no metodo telaDeJogo.computarScore e apenas o chame aqui)
        # fazer a moeda desaparecer depois da colisao
        """TODO"""
        pass