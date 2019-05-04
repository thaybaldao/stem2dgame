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
    def __init__(self, nomeImagemDeFundo, game):
        super().__init__(nomeImagemDeFundo)

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
        pass

    def run(self, game):
        self.interpretarEventos(game)
        self.atualizar(game)
        self.computarScore(game)
        self.desenhar(game)

    def desenhar(self, game):
        self.desenharTelaBasica()
        self.jogador.desenhar(game)
        pygame.display.flip()



