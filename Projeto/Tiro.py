from Cenario import *
from Configuracoes import *
import pygame
import math
import os

class Tiro(Cenario):
    def __init__(self, x, y, tipo, vel):
        self.carregarImagemTiro(tipo)
        super().__init__(x, y, self.imagem, vel)


    #carregar a imagem do tiro
    def carregarImagemTiro(self, tipo):
        self.imagem = pygame.image.load(os.path.join('Imagens', 'tiro.png'))
        #self.imagem = pygame.transform.scale(self.imagem,
                                              #(math.floor(1269 / 3), math.floor(773 / 3)))  # redimensionar a imagem
        #Inverter a imagem para o tiro do inimigo
        if tipo == 'I':
            self.imagem = pygame.transform.flip(self.imagem, 1, 0)

    # atualiza a posicao do tiro apos disparado
    def atualizar(self, tela):
        # Atualizar velocidade e posição do tiro
        self.atualizacaoBasica()
        #dt = 1
        #self.x += self.vel*dt
        #if self.x == LARGURA_DA_TELA-self.largura/2:
        #    tela.tiros.pop()
        #if self.x == 0-self.largura/2:
        #    tela.tirosInimigo.pop()


    # # verifica as colisoes do tiro com o inimigo
    def checarColisoes(self, game, tiro):
        # lembrar que se o personagem tiver vidas e se chocar contra os obstaculos, ele nao deve morrer mas sim perder uma vida
        # lembrar que se a booleana telaDeJogo.jogador.ehInvencivel for verdadeira as colisoes com obstaculos devem ser ignoradas
        for inimigo in game.inimigos:
            if self.vel <0 and self.rect.colliderect(inimigo):
                # decrementa a variavel telaDeJogo.inimigo.vida a cada colisao do tiro com o inimigo
                inimigo.vida -= 1
                # fazer o tiro desaparecer a cada colisao dele com o inimigo
                game.tiros.pop(game.tiros.index(tiro))
                # fazer o inimigo desaparecer apos telaDeJogo.inimigo.vida ser zero
                if inimigo.vida < 1:
                    game.inimigos.pop(game.inimigos.index(inimigo))
        for tiroInimigo in game.tirosInimigo:
            if self.vel <0 and self.rect.colliderect(tiroInimigo):
                # fazer o tiro do jogador e do inimigo desaparecerem a cada colisao entre eles
                game.tiros.pop(game.tiros.index(tiro))
                game.tirosInimigo.pop(game.tirosInimigo.index(tiroInimigo))

        if self.vel > 0 and self.rect.colliderect(game.jogador):
            if not game.ehInvencivel:
                if game.vidasExtras > 0:
                    game.tirosInimigo.pop()
                    game.vidasExtras -= 1
                else:
                    game.administradorDeAudio.tocarEfeitoSonoro(os.path.join('Musica', 'death.wav'), game)
                    pygame.time.wait(3100)
                    game.ultimaTela = 'Tela de Jogo'
                    game.telaAtual = 'Tela de Fim'