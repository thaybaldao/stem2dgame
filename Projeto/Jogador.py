import pygame
from Configuracoes import *
from Obstaculo import *
from Inimigo import *
from Vida import *
from Impulsionador import *
import os
vec = pygame.math.Vector2

class Jogador():
    def __init__(self, game):
        self.x = 150
        self.y = 200
        self.largura = 49
        self.altura = 47
        if game.tipoJogador == 'A' or game.tipoJogador == 'N':
            self.imagem = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_A.png'))
            self.imagemInvencivel = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_Invencivel_A.png'))
            # self.imagemCresceu = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_Cresceu_A.png'))
            # self.imagemInvencivelCresceu = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_Invencivel_Cresceu_A.png'))
        # elif game.tipoJogador == 'B':
        #     self.imagem = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_B.png'))
        #     self.imagemInvencivel  = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_Invencivel_B.png'))
        #     self.imagemCresceu = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_Cresceu_B.png'))
        #     self.imagemInvencivelCresceu = pygame.image.load(
        #         os.path.join('Imagens', 'Personagem_Principal_Invencivel_Cresceu_B.png'))
        # elif game.tipoJogador == 'C':
        #     self.imagem = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_C.png'))
        #     self.imagemInvencivel  = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_Invencivel_C.png'))
        #     self.imagemCresceu = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_Cresceu_C.png'))
        #     self.imagemInvencivelCresceu = pygame.image.load(
        #         os.path.join('Imagens', 'Personagem_Principal_Invencivel_Cresceu_C.png'))
        # else:
        #     self.imagem = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_D.png'))
        #     self.imagemInvencivel  = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_Invencivel_D.png'))
        #     self.imagemCresceu = pygame.image.load(os.path.join('Imagens', 'Personagem_Principal_Cresceu_D.png'))
        #     self.imagemInvencivelCresceu = pygame.image.load(
        #         os.path.join('Imagens', 'Personagem_Principal_Invencivel_Cresceu_D.png'))
        self.rect = self.imagem.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        self.vel = vec(0, 0)
        self.acc = vec(0, ACE_GRAV)
        self.poder = 0
        self.ehInvencivel = False
        self.vidasExtra = 0
        self.poderes = 0
        self.cresceu = False

    # esse metodo atualiza as posicoes do jogador para que ele pule
    def pular(self):
        pass

    # esse metodo atualiza as posicoes do jogador para que ele se mova para a direita
    def moverDireita(self):
        pass

    # esse metodo atualiza as posicoes do jogador para que ele se mova para a esquerda
    def moverEsquerda(self):
        pass

    # esse metodo faz com que o jogador dispare seu poder
    def atirar(self, game):
        # nao esquecer de checar se o personagem tem poderes para atirar
        pass

    # verifica o comando dado pelo usuario e em que estado o jogador esta (pulando, parado, se movendo lateralmente ou atirando)
    # e chama o metodo correspondente para atualizar as posicoes do jogador
    def atualizar(self, game, comandoUsuario):
        # administrar o tempo de invencibilidade do jogador
        pass

    def desenhar(self, game):
        if self.ehInvencivel == False and self.cresceu == False:
            game.janela.blit(self.imagem, (self.rect.left, self.rect.top))
        elif self.ehInvencivel == True and self.cresceu == True:
            game.janela.blit(self.imagemInvencivelCresceu, (self.rect.left, self.rect.top))
        elif janela.ehInvencivel == True:
            game.janela.blit(self.imagemInvencivel, (self.rect.left, self.rect.top))
        else:
            game.janela.blit(self.imagemCresceu, (self.rect.left, self.rect.top))
