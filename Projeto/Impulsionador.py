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
            collisions = pygame.sprite.spritecollide(game.jogador, game.impulsionadores, False)
            callback = pygame.sprite.collide_mask
            collide = pygame.sprite.spritecollideany(game.jogador, collisions, callback)
            if collide:
                game.impulsionadores.pop(game.impulsionadores.index(self))
                game.administradorDeAudio.tocarEfeitoSonoro(os.path.join('Musica', 'boost.wav'), game)
                pygame.time.wait(1500)
                game.ehInvencivel = True
