from Cenario import *
import pygame

class Poder(Cenario):
    def __init__(self, x, y, largura, altura, imagem, tipo, num, vel):
        super().__init__(x, y, largura, altura, imagem, tipo, num, vel)

    def atualizar(self, game):
        self.atualizacaoBasica()

    # verifica as colisoes do personagem com os poderes
    def checarColisoes(self, telaDeJogo):
        # incrementar a variavel inteira jogador.poderes  caso ocorra a colisao do personagem com o poder
        # fazer o poder desaparecer depois da colisao
        pass