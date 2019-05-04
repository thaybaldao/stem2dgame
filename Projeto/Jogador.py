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
        self.carregarImagemPersonagem(game)
        self.largura = self.imagem.get_width()
        self.altura = self.imagem.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)  # retangulo de colisoes
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        self.vel = vec(0, 0)
        self.acc = vec(0, ACE_GRAV)
        self.poder = 0
        self.ehInvencivel = False
        self.vidasExtra = 0
        self.cresceu = False


    # carrega a imagem do personagem de acordo com a escolha do usuario
    def carregarImagemPersonagem(self, game):
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


    # esse metodo atualiza as posicoes do jogador para que ele pule
    def pular(self):
        """TODO"""
        pass


    # esse metodo atualiza as posicoes do jogador para que ele se mova para a direita
    def moverDireita(self):
        """TODO"""
        pass


    # esse metodo atualiza as posicoes do jogador para que ele se mova para a esquerda
    def moverEsquerda(self):
        """TODO"""
        pass


    # esse metodo faz com que o jogador dispare seu poder
    def atirar(self, game):
        # nao esquecer de checar se o personagem tem poderes (booleana self.poder contabiliza isso) para atirar
        """TODO"""
        pass


    # verifica o comando dado pelo usuario e em que estado o jogador esta (pulando, parado, se movendo lateralmente ou atirando)
    # e chama o metodo correspondente para atualizar as posicoes do jogador
    def atualizar(self, game, comandoUsuario):
        # nao esquecer de administrar o tempo de invencibilidade do jogador
        """TODO"""
        pass


    # desenha o jogador na tela com a imagem correspondente ao seu estado atual
    def desenhar(self, game):
        if self.ehInvencivel == False and self.cresceu == False:
            game.janela.blit(self.imagem, (self.rect.left, self.rect.top))
        elif self.ehInvencivel == True and self.cresceu == True:
            game.janela.blit(self.imagemInvencivelCresceu, (self.rect.left, self.rect.top))
        elif self.ehInvencivel == True:
            game.janela.blit(self.imagemInvencivel, (self.rect.left, self.rect.top))
        else:
            game.janela.blit(self.imagemCresceu, (self.rect.left, self.rect.top))
