from Configuracoes import *
from Tela import *
from Jogador import *
from Obstaculo import *
from Vida import *
from Impulsionador import *
from Inimigo import *
from Tiro import *
import pygame
import random
import os
from pygame.locals import *

class TelaDeJogo(Tela):
    def __init__(self, game):

        super().__init__()
        self.name = "Tela de Jogo"
        self.fonte1 = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 35)
        self.fonte2 = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 160)
        self.batalha = False
        self.time = 0

        # inicializando jogador e vetor para armazenar outros elementos do jogo
        self.tolerancia = game.jogador.largura*2.1


    def computarPontuacao(self, game):
        pass

    def imprimirPontuacao(self, game):
        pass

    # imprime barra de vidas
    def imprimirBarraDeVidas(self, game):
        pass
    def computarTempoDeInvencibilidade(self, game):
        pass

    # imprime tempo de invencibilidade na Tela a partir do momento em que a varivel game.ehInvencivel se tornar verdadeira, por x segundos
    def imprimirTempoDeInvencibilidade(self, game):
        pass


    # cria itens do cenario na tela
    def criarCenario(self, game):
        pass


    def checarComportamentoJogador(self, game, evento):
        # verificar se o usuario pediu para o jogador fazer algum comando (atirar ou pular)
        if evento != [] and evento.type == pygame.KEYDOWN: #verificar se há algo na fila de eventos e se há teclas precionadas
            if evento.key == pygame.K_UP:
                game.jogador.pular(game)
            elif evento.key == pygame.K_SPACE:
                game.jogador.atirar(game)


    def checarColisoes(self, game):
        for obstaculo in game.obstaculos:
            obstaculo.checarColisoes(game)

        for vida in game.vidas:
            vida.checarColisoes(game)

        for impulsionador in game.impulsionadores:
            impulsionador.checarColisoes(game)

        for inimigo in game.inimigos:
            inimigo.checarColisoes(game)

        for tiro in game.tiros:
            tiro.checarColisoes(game, tiro)

        for tiroInimigo in game.tirosInimigo:
            tiroInimigo.checarColisoes(game, tiroInimigo)

    def atualizar(self, game):
        game.jogador.atualizar(game)

        for obstaculo in game.obstaculos:
            obstaculo.atualizar(game)
            if obstaculo.x < - obstaculo.largura - 20:
                game.obstaculos.pop(game.obstaculos.index(obstaculo))

        for vida in game.vidas:
            vida.atualizar(game)
            if vida.x < - vida.largura - 20:
                game.vidas.pop(game.vidas.index(vida))

        for impulsionador in game.impulsionadores:
            impulsionador.atualizar(game)
            if impulsionador.x < - impulsionador.largura - 20:
                game.impulsionadores.pop(game.impulsionadores.index(impulsionador))

        for inimigo in game.inimigos:
            inimigo.atualizar(game)
            if inimigo.x < - inimigo.largura - 20:
                game.inimigos.pop(game.inimigos.index(inimigo))

        for tiro in game.tiros:
            tiro.atualizar(game)
            if tiro.x < - tiro.largura - 20:
                game.tiros.pop(game.tiros.index(tiro))
        for tiroInimigo in game.tirosInimigo:
            tiroInimigo.atualizar(game)
            if tiroInimigo.x < - tiroInimigo.largura - 20:
                game.tirosInimigo.pop(game.tirosInimigo.index(tiroInimigo))

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
            # print('pos 0: ', pos[0], ' pos1: ', pos[1] )

    def desenhar(self, game):
        self.desenharTelaBasica(game)

        for obstaculo in game.obstaculos:
            obstaculo.desenhar(game)

        for vida in game.vidas:
            vida.desenhar(game)

        for impulsionador in game.impulsionadores:
            impulsionador.desenhar(game)

        for inimigo in game.inimigos:
            inimigo.desenhar(game)

        for tiro in game.tiros:
            tiro.desenhar(game)

        for tiroInimigo in game.tirosInimigo:
            tiroInimigo.desenhar(game)

        game.jogador.desenhar(game, self)

        self.imprimirPontuacao(game)

        self.imprimirTempoDeInvencibilidade(game)

        self.imprimirBarraDeVidas(game)

        pygame.display.flip()

    def telaBatalha(self, game):
        pass

    def telaBomTrabalho(self, game):
        pass

    def computarTempoDeBatalha(self, game):
        pass

    def run(self, game):

        self.time = 1

        while game.telaAtual == self.name and not game.usuarioSaiu:

            # aumentar a velocidade do jogo
            if game.aparecimentoElementos > 25 and self.time % 300 == 0:
                game.aparecimentoElementos -= 1
            if self.time % 1200 == 0:
                game.dvel += 1

            # iniciar batalhas
            if not self.batalha and self.time % 1800 == 0:
                self.telaBatalha(game)


            if self.time % 30 == 0:
                self.computarPontuacao(game)
                self.criarCenario(game)

            if self.time % 60 == 0:
                self.computarTempoDeInvencibilidade(game)
                self.computarTempoDeBatalha(game)

            self.interpretarEventos(game)
            self.checarColisoes(game)
            self.atualizar(game)
            self.desenhar(game)

            self.time += 1



