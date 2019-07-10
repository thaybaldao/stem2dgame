from Cenario import *
from Tiro import *
import pygame
import os
import math

class Inimigo(Cenario):
    def __init__(self, x, y, tipo, vel):
        self.carregarImagemInimigo(tipo)
        super().__init__(x, y, self.imagem, tipo, vel)
        self.vida = 3
        self.tempo = pygame.time.get_ticks()

    #carregar a imagem do inimigo
    def carregarImagemInimigo(self,tipo):
        nomeInimigo = 'inimigo_1.png'
        nomeInimigo = nomeInimigo.replace("1", str(tipo))
        self.imagem = pygame.image.load(os.path.join('Imagens', nomeInimigo))
        self.imagem = pygame.transform.scale(self.imagem,
                                              (math.floor(1269 / 3), math.floor(773 / 3)))  # redimensionar a imagem

    def atualizar(self, tela):
        dt = 1
        self.x -= self.vel*dt
        if self.x == 0-self.largura/2:
            tela.inimigos.pop()
        if self.tipo == 2 or self.tipo == 3:
            if ((pygame.time.get_ticks()-self.tempo)%5000 < 150):
                tela.tirosInimigo.append(Tiro(self.x, self.y, 'I', -10))

    # verifica as colisoes do personagem com o inimigo
    def checarColisoes(self, telaDeJogo, game):
        # lembrar que se o personagem tiver vidas e se chocar contra inimigos, ele nao deve morrer mas sim perder uma vida
        # lembrar que se a booleana telaDeJogo.jogador.ehInvencivel for verdadeira as colisoes com inimigos devem ser ignoradas
        # lembrar que se a booleana telaDeJogo.jogador.cresceu for verdadeira as colisoes com inimigos devem apenas levar esta booleana
        # a se tornar falsa, de modo que o jogador voltara a ser pequeno
        if self.rect.colliderect(telaDeJogo.jogador):
            if telaDeJogo.jogador.ehInvencivel == True:
                telaDeJogo.inimigos.pop()
            else:
                if telaDeJogo.jogador.cresceu == True:
                    telaDeJogo.inimigos.pop()
                    telaDeJogo.jogador.cresceu = False

                else:
                    telaDeJogo.inimigos.pop()
                    telaDeJogo.jogador.vidasExtra -= 1