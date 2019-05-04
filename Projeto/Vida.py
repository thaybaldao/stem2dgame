from Cenario import *
import pygame

class Vida(Cenario):
    def __init__(self, x, y, imagem, tipo, num, vel):
        super().__init__(x, y, imagem, tipo, num, vel)

    def atualizar(self, game):
        self.atualizacaoBasica()

    # verifica as colisoes do personagem com as vidas
    def checarColisoes(self, telaDeJogo):
        # incrementar a variavel inteira jogador.vidasExtra  caso ocorra a colisao do personagem com a vida
        # fazer a vida desaparecer depois da colisao
        pass