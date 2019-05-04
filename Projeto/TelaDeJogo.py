from Configuracoes import *
from Tela import *
from Jogador import *
from Obstaculo import *
from Inimigo import*
from Vida import *
from Impulsionador import *
import pygame
import os
from pygame.locals import *

class TelaDeJogo(Tela):
    def __init__(self, game, nomeImagemDeFundo):
        super().__init__(game, nomeImagemDeFundo)

        # inicializando jogador e vetor para armazenar outros elementos do jogo
        self.jogador = Jogador(game)
        self.obstaculos = []
        self.inimigos = []
        self.vidas = []
        self.vidasDisponiveis = []
        self.impulsionadores = []
        self.poderes = []
        self.tiros = []
        self.moedas = []
        self.name = "Tela de Jogo"

        # inicializando a pontuacao
        self.score = 0

    def computarScore(self, game):
        pass

    def imprimirScore(self, game):
        pass

    def imprimirTempoDeInvencibilidade(self):
        # imprimir tempo de invencibilidade a partir do momento em que a varivel jogador.ehInvencivel se tornar verdadeira, por 15 segundos
        pass


    def criarCenario(self, game):
        pass

    # verifica as colisoes do jogo
    def checarColisoes(self):
        for obstaculo in self.obstaculos:
            obstaculo.checarColisoes(self.jogador)

        for inimigo in self.inimigos:
            inimigo.checarColisoes(self.jogador)

        for poder in self.poderes:
            poder.checarColisoes(self.jogador)

        for tiro in self.tiros:
            tiro.checarColisoes(self)

        for vida in self.vidas:
            vida.checarColisoes(self)

        for impulsionador in self.impulsionadores:
            impulsionador.checarColisoes(self)

        for moeda in self.moedas:
            moeda.checarColisoes()



    def atualizar(self, game):
        pass

    def interpretarEventos(self, game):
        game.clock.tick(game.fps)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            # checa se o usuario quer sair do jogo
            self.comportamentoBotaoDeSair(game, event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # checa se o usuario quer tirar o som
                self.comportamentoBotaoDeAudio(game, event, pos)

    def run(self, game):
        while game.telaAtual == self.name and not game.usuarioSaiu:
            self.interpretarEventos(game)
            self.atualizar(game)
            self.computarScore(game)
            self.desenhar(game)

    def desenhar(self, game):
        self.desenharTelaBasica(game)
        self.jogador.desenhar(game)
        pygame.display.flip()



