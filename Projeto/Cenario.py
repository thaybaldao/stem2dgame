import pygame
from Configuracoes import *

# quaisquer itens que aparecem na tela do jogo, exceto background, botoes e jogador sao classes derivadas da classe Cenario
class Cenario:
    def __init__(self, x, y, imagem, vel):
        self.x = x
        self.y = y
        self.imagem = imagem
        self.largura = imagem.get_width()
        self.altura = imagem.get_height()
        self.rect = pygame.Rect(self.x+self.largura/6, self.y+self.altura/6, 2*self.largura/3, 2*self.altura/3) # retangulo de colisoes
        self.vel = vel  # velocidade de atualizacao horizontal na tela


    # descreve como o item do cenario tem sua posicao horizontal atualiza na tela
    def atualizacaoBasica(self):
        if self.x > -200:
            self.x -= self.vel
        self.rect.x = self.x
        self.rect.y = self.y


    # desenha o item do cenario na tela
    def desenhar(self, game):
        game.janela.blit(self.imagem, (self.x, self.y))
        pygame.draw.rect(game.janela, (255, 0, 0), self.rect, 2)