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
import random
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
        self.tirosInimigo = []
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
        rand = random.randint(1,100)
        if rand == 1:
            self.inimigos.append(Inimigo(LARGURA_DA_TELA/2, Y_CHAO-300, random.randint(1, 4), 5))

    def checarComportamentoJogador(self, game, evento):
        # verificar se o usuario pediu para o jogador fazer algum comando (atirar ou pular)
        # chamar aqui o metodo que atualiza as coordenadas do jogador e faz ele se mover (jogador.atualizar(comandoDoUsuario))
        if evento != [] and evento.type == pygame.KEYDOWN: #verificar se há algo na fila de eventos e se há teclas precionadas
            if evento.key == pygame.K_UP:
                self.jogador.pular(evento)
            elif evento.key == pygame.K_SPACE:
                self.jogador.atirar(self.tiros)


    def checarColisoes(self):
        for obstaculo in self.obstaculos:
            obstaculo.checarColisoes(self)

        for inimigo in self.inimigos:
            inimigo.checarColisoes(self)

        for poder in self.poderes:
            poder.checarColisoes(self)

        for tiro in self.tiros:
            tiro.checarColisoes(self)

        for tiroInimigo in self.tirosInimigo:
            tiroInimigo.checarColisoes(self)

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
            inimigo.atualizar(self)

        for poder in self.poderes:
            poder.atualizar(game)

        for tiro in self.tiros:
            tiro.atualizar(self)

        for tiroInimigo in self.tirosInimigo:
            tiroInimigo.atualizar(self)

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
            #print(pos)

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
            inimigo.desenhar(game)

        for poder in self.poderes:
            poder.desenhar(self)

        for tiro in self.tiros:
            tiro.desenhar(game)

        for tiroInimigo in self.tirosInimigo:
            tiroInimigo.desenhar(game)

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

