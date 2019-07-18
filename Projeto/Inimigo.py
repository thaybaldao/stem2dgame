from Cenario import *
from Tiro import *
import pygame
import os
import math

class Inimigo(Cenario):
    def __init__(self, x, y, imagem, vel, vida):
        super().__init__(x, y, imagem, vel)
        self.vida = vida
        self.tempo = pygame.time.get_ticks()


    def atualizar(self, tela):
        dt = 1
        self.x -= self.vel*dt
        if self.x == 0-self.largura/2:
            tela.inimigos.pop()

    # verifica as colisoes do personagem com o inimigo
    def checarColisoes(self, game):
        # lembrar que se o personagem tiver vidas e se chocar contra inimigos, ele nao deve morrer mas sim perder uma vida
        # lembrar que se a booleana game.ehInvencivel for verdadeira as colisoes com inimigos devem ser ignoradas
        if self.rect.colliderect(game.jogador):
            if not game.ehInvencivel:
                if game.vidasExtras > 0:
                    game.inimigos.pop()
                    game.vidasExtras -= 1
                else:
                    game.administradorDeAudio.tocarEfeitoSonoro(os.path.join('Musica', 'death.wav'), game)
                    pygame.time.wait(3100)
                    game.ultimaTela = 'Tela de Jogo'
                    game.telaAtual = 'Tela de Fim'
