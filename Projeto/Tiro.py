from Cenario import *
from Configuracoes import *
import pygame
import math
import os

class Tiro(Cenario):
    def __init__(self, x, y, tipo, vel):
        self.carregarImagemTiro(tipo)
        super().__init__(x, y, self.imagem, tipo, vel)


    #carregar a imagem do tiro
    def carregarImagemTiro(self, tipo):
        self.imagem = pygame.image.load(os.path.join('Imagens', 'tiro.png'))
        self.imagem = pygame.transform.scale(self.imagem,
                                              (math.floor(1269 / 3), math.floor(773 / 3)))  # redimensionar a imagem
        #Inverter a imagem para o tiro do inimigo
        if tipo == 'I':
            self.imagem = pygame.transform.flip(self.imagem, 1, 0)

    # atualiza a posicao do tiro apos disparado
    def atualizar(self, tela):
        # Atualizar velocidade e posição do tiro
        dt = 1
        self.x += self.vel*dt
        if self.x == LARGURA_DA_TELA-self.largura/2:
            tela.tiros.pop()
        if self.x == 0-self.largura/2:
            tela.tirosInimigo.pop()


    # verifica as colisoes do tiro com o inimigo
    def checarColisoes(self, telaDeJogo):
        # decrementa a variavel telaDeJogo.inimigo.vida a cada colisao do tiro com o inimigo
        # fazer o tiro desaparecer a cada colisao dele com o inimigo
        # fazer o inimigo desaparecer apos telaDeJogo.inimigo.vida ser zero
        """TODO"""
        pass