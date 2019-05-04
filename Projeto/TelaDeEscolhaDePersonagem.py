from Configuracoes import *
from Tela import *
import pygame
import os


class TelaDeEscolhaDePersonagem(Tela):
    def __init__(self, game, nomeImagemDeFundo):
        super().__init__(game, nomeImagemDeFundo)
        self.name = 'Tela de Escolha de Personagens'

    def comportamentoBotaoEscolhaPesonagemA(self, game, evento, pos):
        # atualizar a string game.tipoJogador com 'A' caso o usuario selecione este personagem
        # trocar para a tela de jogo caso o usuario selecione o personagem
        pass


    def comportamentoBotaoEscolhaPesonagemB(self, game, evento, pos):
        # atualizar a string game.tipoJogador com 'B' caso o usuario selecione este personagem
        # trocar para a tela de jogo caso o usuario selecione o personagem
        pass


    def comportamentoBotaoEscolhaPesonagemC(self, game, evento, pos):
        # atualizar a string game.tipoJogador com 'C' caso o usuario selecione este personagem
        # trocar para a tela de jogo caso o usuario selecione o personagem
        pass


    def comportamentoBotaoEscolhaPesonagemD(self, game, evento, pos):
        # atualizar a string game.tipoJogador com 'D' caso o usuario selecione este personagem
        # trocar para a tela de jogo caso o usuario selecione o personagem
        pass


    def interpretarEventos(self, game):
        game.clock.tick(game.fps)

        for evento in pygame.event.get():
            pos = pygame.mouse.get_pos()

            # checa se o usuario quer sair do jogo
            self.comportamentoBotaoDeSair(game, evento)

            # checa se o usuario quer tirar o som
            self.comportamentoBotaoDeAudio(game, evento, pos)

            # checa se o usuario escolheu o personagem A
            self.comportamentoBotaoEscolhaPesonagemA(game, evento, pos)

            # checa se o usuario escolheu o personagem B
            self.comportamentoBotaoEscolhaPesonagemB(game, evento, pos)

            # checa se o usuario escolheu o personagem C
            self.comportamentoBotaoEscolhaPesonagemC(game, evento, pos)

            # checa se o usuario escolheu o personagem D
            self.comportamentoBotaoEscolhaPesonagemD(game, evento, pos)


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