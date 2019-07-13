from Cenario import *
import pygame

class Vida(Cenario):
    def __init__(self, x, y, imagem, vel):
        super().__init__(x, y, imagem, vel)

    def atualizar(self, game):
        self.atualizacaoBasica()

    # verifica as colisoes do personagem com as vidas
    def checarColisoes(self, telaDeJogo, game):
        # incrementar a variavel inteira telaDeJogo.jogador.vidasExtra caso ocorra a colisao do personagem com a vida
        # fazer a vida desaparecer depois da colisao
        if self.rect.colliderect(telaDeJogo.jogador):
            if telaDeJogo.jogador.vidasExtra < 3:
                telaDeJogo.jogador.vidasExtra +=1
            telaDeJogo.vidas.pop()