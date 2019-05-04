from Configuracoes import *
from Tela import *
import pygame
import os


class TelaDeMudancaDeNivel(Tela):
    def __init__(self, game, nomeImagemDeFundo):
        super().__init__(game, nomeImagemDeFundo)
        self.name = 'Tela de Mudanca de Nivel'

    def comportamentoBotaoProximoNivel(self, game, evento, pos):
        pass


    def interpretarEventos(self, game):
        game.clock.tick(game.fps)

        for evento in pygame.event.get():
            pos = pygame.mouse.get_pos()

            # checa se o usuario quer sair do jogo
            self.comportamentoBotaoDeSair(game, evento)

            # checa se o usuario quer tirar o som
            self.comportamentoBotaoDeAudio(game, evento, pos)

            # checa se o usuario quer jogar
            self.comportamentoBotaoProximoNivel(game, evento, pos)


    # esse metodo deve desenhar tudo que tem na tela, exceto background e botao de audio
    def desenharTela(self, game):
        pass


    def desenhar(self, game):
        self.desenharTelaBasica(game)
        self.desenharTela(game)
        pygame.display.flip()


    def run(self, game):
        while game.telaAtual == self.name and not game.usuarioSaiu:
            self.interpretarEventos(game)
            self.desenhar(game)
