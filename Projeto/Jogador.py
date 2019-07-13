import pygame
import math
from Configuracoes import *
from Obstaculo import *
from Vida import *
from Impulsionador import *
import os
vec = pygame.math.Vector2

class Jogador():
    def __init__(self, game):
        self.x = X_CHAO
        self.y = Y_CHAO
        self.carregarImagemPersonagem(game)
        self.largura = self.imagem.get_width()
        self.altura = self.imagem.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)  # retangulo de colisoes
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        self.vel = vec(0, 0)
        self.acc = vec(0, ACE_GRAV)
        self.poder = 1
        self.ehInvencivel = False
        self.vidasExtra = 0
        self.cresceu = False


    # carrega a imagem do personagem de acordo com a escolha do usuario
    def carregarImagemPersonagem(self, game):
        self.imagemF = pygame.image.load(os.path.join('Imagens', 'personagem_principal_FEC_1.png'))
        self.imagemD = pygame.image.load(os.path.join('Imagens', 'personagem_principal_DIR_1.png'))
        self.imagemE = pygame.image.load(os.path.join('Imagens', 'personagem_principal_ESQ_1.png'))
        # carregar imagens para modo invencivel
        self.imagemInvencivelF = pygame.image.load(os.path.join('Imagens', 'personagem_principal_invencivel_FEC_1.png'))
        self.imagemInvencivelD = pygame.image.load(os.path.join('Imagens', 'personagem_principal_invencivel_DIR_1.png'))
        self.imagemInvencivelE = pygame.image.load(os.path.join('Imagens', 'personagem_principal_invencivel_ESQ_1.png'))
        self.imagem = self.imagemF


    # esse metodo atualiza as posicoes do jogador para que ele pule
    def pular(self, evento):
        if self.pos.y == Y_CHAO:
            self.vel.y = VELOC_INICIAL_PULO

    # esse metodo faz com que o jogador dispare seu poder
    def atirar(self, tiros):
        tiros.append(Tiro(self.x-self.largura/2, self.pos.y/2, 'A', 10))


    # verifica o comando dado pelo usuario e em que estado o jogador esta (pulando, parado, se movendo lateralmente ou atirando)
    # e chama o metodo correspondente para atualizar as posicoes do jogador
    def atualizar(self):
        # Equações de Movimento
        dt = 1
        # Atualizar velocidade e posição do jogador
        self.vel += self.acc*dt
        self.pos += self.vel*dt
        self.rect.midbottom = self.pos

        if self.pos.y >= (Y_CHAO):
            self.pos.y = (Y_CHAO)
            self.vel.y = 0


    # desenha o jogador na tela com a imagem correspondente ao seu estado atual
    def desenhar(self, game):
        # vetor com as imagens
        if self.ehInvencivel == False:
            self.images = [self.imagemF, self.imagemD, self.imagemE]
        elif self.ehInvencivel == True:
            self.images = [self.imagemInvencivelF, self.imagemInvencivelD, self.imagemInvencivelE]

        # gerar efeito gradual no pulo
        if self.pos.y == (Y_CHAO):
            self.imagem = self.images[0]
        elif self.pos.y < (Y_CHAO) and self.pos.y > (0.95*Y_CHAO):
            self.imagem = self.images[1]
        else:
            self.imagem = self.images[2]

        game.janela.blit(self.imagem, (self.rect.left, self.rect.top))