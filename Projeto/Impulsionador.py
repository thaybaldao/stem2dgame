from Cenario import *
import pygame

class Impulsionador(Cenario):
    def __init__(self, x, y, imagem, vel):
        super().__init__(x, y, imagem, vel)


    def atualizar(self, game):
        self.atualizacaoBasica()


    # verifica as colisoes do personagem com o impulsionador
    def checarColisoes(self, game):
        # fazer a variavel game.ehInvencivel ser verdadeira caso ocorra a colisao
        # fazer o impulsionador desaparecer depois da colisao
        if self.rect.colliderect(game.jogador):
            game.administradorDeAudio.tocarEfeitoSonoro(os.path.join('Musica', 'boost.wav'), game)
            pygame.time.wait(1500)
            game.ehInvencivel = True
            game.impulsionadores.pop()