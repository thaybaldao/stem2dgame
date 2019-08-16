from Cenario import *
from Configuracoes import *
import pygame
import math
import os

class Tiro(Cenario):
    def __init__(self, x, y, tipo, vel):
        self.carregarImagemTiro(tipo)
        super().__init__(x, y, self.imagem, vel)

    # carregar a imagem do tiro
    def carregarImagemTiro(self, tipo):
        self.imagem = pygame.image.load(os.path.join('Imagens', 'tiro.png'))

        #Inverter a imagem para o tiro do inimigo
        if tipo == 'I':
            self.imagem = pygame.transform.flip(self.imagem, 1, 0)

    # atualiza a posicao do tiro apos disparado
    def atualizar(self, tela):
        self.atualizacaoBasica()

    # verifica as colisoes do tiro com o inimigo
    def checarColisoes(self, game, tiro):
        # lembrar que se o personagem tiver vidas e se chocar contra os obstaculos, ele nao deve morrer mas sim perder uma vida
        # lembrar que se a booleana telaDeJogo.jogador.ehInvencivel for verdadeira as colisoes com obstaculos devem ser ignoradas
        pass