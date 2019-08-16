import pygame
import math
from Configuracoes import *
from Obstaculo import *
from Vida import *
from Impulsionador import *
from Tiro import *
import os
vec = pygame.math.Vector2

class Jogador():
    def __init__(self, game):
        self.x = X_CHAO
        self.y = Y_CHAO
        self.carregarImagemPersonagem(game)
        self.largura = self.image.get_width()
        self.altura = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)  # retangulo de colisoes
        self.rect.center = (self.x + self.largura/2, self.y + self.altura/2)
        self.pos = vec(self.x + self.largura/2, self.y + self.altura/2)
        self.vel = vec(0.0, 0.0)
        self.acc = vec(0.0, 0.0)

    # carrega a imagem do personagem de acordo com a escolha do usuario
    def carregarImagemPersonagem(self, game):
        self.imagemF = pygame.image.load(os.path.join('Imagens', 'personagem_principal_FEC_1.png'))
        self.imagemD = pygame.image.load(os.path.join('Imagens', 'personagem_principal_DIR_1.png'))
        self.imagemE = pygame.image.load(os.path.join('Imagens', 'personagem_principal_ESQ_1.png'))
        # carregar imagens para modo invencivel
        self.imagemInvencivelF = pygame.image.load(os.path.join('Imagens', 'personagem_principal_invencivel_FEC_1.png'))
        self.imagemInvencivelD = pygame.image.load(os.path.join('Imagens', 'personagem_principal_invencivel_DIR_1.png'))
        self.imagemInvencivelE = pygame.image.load(os.path.join('Imagens', 'personagem_principal_invencivel_ESQ_1.png'))
        self.image = self.imagemD

        # vetor com as imagens
        if game.ehInvencivel == False:
            self.imagens = [self.imagemF, self.imagemD, self.imagemE]
            if self.pular:
                self.image = self.imagemD
            else:
                self.image = self.imagemE
        if game.ehInvencivel == True:
            self.imagens = [self.imagemInvencivelF, self.imagemInvencivelD, self.imagemInvencivelE]
            if self.pular:
                self.image = self.imagemInvencivelD
            else:
                self.image = self.imagemInvencivelE

    # esse metodo atualiza as posicoes do jogador para que ele pule
    def pular(self, game):
        pass

    # esse metodo faz carregar o tiro do jogador na tela
    def atirar(self, game):
        pass

    # esse metodo atualiza as posicoes do jogador
    def atualizar(self, game):
        pass

    # desenha o jogador na tela com a imagem correspondente ao seu estado atual
    def desenhar(self, game, tela):
        pass

        game.janela.blit(self.imagem, (self.rect.left, self.rect.top))
        # pygame.draw.rect(game.janela, (255, 0, 0), self.rect, 2)