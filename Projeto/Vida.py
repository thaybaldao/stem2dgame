from Cenario import *
import pygame

class Vida(Cenario):
    def __init__(self, x, y, imagem, vel):
        super().__init__(x, y, imagem, vel)

    def atualizar(self, game):
        self.atualizacaoBasica()

    # verifica as colisoes do personagem com as vidas
    def checarColisoes(self, game):
        # incrementar a variavel inteira game.vidasExtras caso ocorra a colisao do personagem com a vida
        # fazer a vida desaparecer depois da colisao
        if self.rect.colliderect(game.jogador):
            game.vidas.pop()
            game.ultimaTela = 'Tela de Jogo'
            game.telaAtual = 'Tela de Perguntas'