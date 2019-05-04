from Configuracoes import *
from Tela import *
from Jogador import *
from Obstaculo import *
from Inimigo import*
from Vida import *
from Impulsionador import *
from Moeda import *
from Crescimento import *
from Poder import *
from Tiro import *
import pygame
import os
from pygame.locals import *

class TelaDeJogo(Tela):
    def __init__(self, game, nomeImagemDeFundo):
        super().__init__(game, nomeImagemDeFundo)
        self.name = "Tela de Jogo"

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
        self.comandoDoUsuario = 0

        # inicializando a pontuacao do jogo
        self.score = 0


    def computarScore(self):
        # chamar estemetodo nas colisoes do jogador com as moedas
        """TODO"""
        pass


    def imprimirScore(self, game):
        """TODO"""
        pass

    # imprime tempo de invencibilidade na Tela a partir do momento em que a varivel jogador.ehInvencivel se tornar verdadeira, por x segundos
    def imprimirTempoDeInvencibilidade(self):
        """TODO"""
        pass


    # cria itens do cenario na tela
    def criarCenario(self, game):
        """TODO"""
        pass

    def checarComportamentoJogador(self, game, evento):
        # verificar se o usuario pediu para o jogador fazer algum comando (andar para esquerda, andar para a direita, ou ainda, pular)
        """TODO"""
        pass


    def checarColisoes(self):
        for obstaculo in self.obstaculos:
            obstaculo.checarColisoes(self)

        for inimigo in self.inimigos:
            inimigo.checarColisoes(self)

        for poder in self.poderes:
            poder.checarColisoes(self)

        for tiro in self.tiros:
            tiro.checarColisoes(self)

        for vida in self.vidas:
            vida.checarColisoes(self)

        for impulsionador in self.impulsionadores:
            impulsionador.checarColisoes(self)

        for moeda in self.moedas:
            moeda.checarColisoes(self)


    def atualizar(self, game):
        self.jogador.atualizar(game, self.comandoDoUsuario)

        for obstaculo in self.obstaculos:
            obstaculo.atualizar(game)

        for inimigo in self.inimigos:
            inimigo.atualizar(game)

        for poder in self.poderes:
            poder.atualizar(game)

        for tiro in self.tiros:
            tiro.atualizar(game)

        for vida in self.vidas:
            vida.atualizar(game)

        for impulsionador in self.impulsionadores:
            impulsionador.atualizar(game)

        for moeda in self.moedas:
            moeda.atualizar(game)


    def interpretarEventos(self, game):
        game.clock.tick(game.fps)

        for evento in pygame.event.get():
            pos = pygame.mouse.get_pos()

            # checa se o usuario quer sair do jogo
            self.comportamentoBotaoDeSair(game, evento)

            # checa se o usuario quer mover o jogador
            self.checarComportamentoJogador(game, evento)

            # checa se o usuario quer tirar o som
            self.comportamentoBotaoDeAudio(game, evento, pos)


    def desenhar(self, game):
        self.desenharTelaBasica(game)

        for obstaculo in self.obstaculos:
            obstaculo.desenhar(self)

        for inimigo in self.inimigos:
            inimigo.desenhar(self)

        for poder in self.poderes:
            poder.desenhar(self)

        for tiro in self.tiros:
            tiro.desenhar(self)

        for vida in self.vidas:
            vida.desenhar(self)

        for impulsionador in self.impulsionadores:
            impulsionador.desenhar(self)

        for moeda in self.moedas:
            moeda.desenhar(self)

        self.jogador.desenhar(game)

        self.imprimirScore(game)

        if self.jogador.ehInvencivel:
            self.imprimirTempoDeInvencibilidade()

        # desenhar a barra de vidas
        """TODO"""

        pygame.display.flip()


    def run(self, game):
        while game.telaAtual == self.name and not game.usuarioSaiu:
            self.criarCenario(game)
            self.interpretarEventos(game)
            self.atualizar(game)
            self.computarScore()
            self.desenhar(game)

