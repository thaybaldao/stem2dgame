from Cenario import *
from Tiro import *
import pygame
import os
import math
import random

class Inimigo(Cenario):
    def __init__(self, x, y, imagem, vel, vida, tipo):
        super().__init__(x, y, imagem, vel)
        self.vida = vida
        self.tempo = pygame.time.get_ticks()
        self.velY = -2.5 *vel
        self.tipo = tipo

    # metodo responsavel pela movimentacao do inimigo na tela
    def atualizar(self, game):
        pass

    # verifica as colisoes do personagem com o inimigo
    def checarColisoes(self, game):
        # lembrar que se o personagem tiver vidas e se chocar contra inimigos, ele nao deve morrer mas sim perder uma vida
        # lembrar que se a booleana game.ehInvencivel for verdadeira as colisoes com inimigos devem ser ignoradas
        pass