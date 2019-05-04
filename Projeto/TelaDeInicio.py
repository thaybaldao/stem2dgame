from Configuracoes import *
from Tela import *
import pygame
import os

class TelaDeInicio(Tela):
    def __init__(self, game, nomeImagemDeFundo):
        super().__init__(game, nomeImagemDeFundo)
        self.name = 'Tela de Inicio'

    # metodo para lidar com interacoes com o botao que direciona para a tela de instrucoes
    def comportamentoBotaoDeInstrucoes(self, game, evento, pos):
        # caso o usuario clique neste botao ele sera redirecionado para a tela de instrucoes
        # para fazer isto basta fazer a variavel game.telaAtual = 'Tela de Instrucoes'
        """TODO"""
        pass


    # metodo para lidar com interacoes com o botao de jogar
    def comportamentoBotaoDeJogar(self, game, evento, pos):
        # caso o usuario clique neste botao ele sera redirecionado para a tela de jogo
        # para fazer isto basta fazer a variavel game.telaAtual = 'Tela de Jogo'
        """TODO"""
        pass


    # metodo para lidar com interacoes com o botao que direciona para a tela de escolha de personagens
    def comportamentoBotaoDeEscolherPersonagem(self, game, evento, pos):
        # caso o usuario clique neste botao ele sera redirecionado para a tela de escolha de personagens
        # para fazer isto basta fazer a variavel game.telaAtual = 'Tela de Escolha de Personagens'
        """TODO"""
        pass


    def interpretarEventos(self, game):
        game.clock.tick(game.fps)

        for evento in pygame.event.get():
            pos = pygame.mouse.get_pos()

            # checa se o usuario quer sair do jogo
            self.comportamentoBotaoDeSair(game, evento)

            # checa se o usuario quer tirar o som
            self.comportamentoBotaoDeAudio(game, evento, pos)

            # checa se o usuario clicou no botao para abrir a tela de instrucoes
            self.comportamentoBotaoDeInstrucoes(game, evento, pos)

            # checa se o usuario clicou no botao para abrir a tela de escolher personagem
            self.comportamentoBotaoDeEscolherPersonagem(game, evento, pos)

            # checa se o usuario quer jogar
            self.comportamentoBotaoDeJogar(game, evento, pos)


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



