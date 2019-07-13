from Configuracoes import *
from Tela import *
from Jogador import *
from Obstaculo import *
from Vida import *
from Impulsionador import *
import pygame
import random
import os
from pygame.locals import *

class TelaDeJogo(Tela):
    def __init__(self, game):
        super().__init__()
        self.name = "Tela de Jogo"

        # inicializando jogador e vetor para armazenar outros elementos do jogo
        self.jogador = Jogador(game)
        self.obstaculos = []
        self.inimigos = []
        self.vidas = []
        self.vidasDisponiveis = []
        self.impulsionadores = []
        self.tiros = []
        self.tirosInimigo = []
        self.comandoDoUsuario = 0
        self.tolerancia = 100

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
        # rand = random.randint(1,100)
        # if rand == 1:
        #     self.inimigos.append(Inimigo(LARGURA_DA_TELA/2, Y_CHAO-300, random.randint(1, 4), 5))

        r = random.randrange(0, 200)
        if len(self.obstaculos) == 0 or self.obstaculos[-1].x + self.obstaculos[-1].largura + self.tolerancia < LARGURA_DA_TELA:
            if r < 4:
                self.obstaculos.append(Obstaculo(1300, 625, pygame.image.load(os.path.join('Imagens', 'obstaculo_1_1.png')), 5))
            if r == 5:
                self.obstaculos.append(Vida(1300, 625, pygame.image.load(os.path.join('Imagens', 'vida.png')), 5))



    def checarComportamentoJogador(self, game, evento):
        # verificar se o usuario pediu para o jogador fazer algum comando (atirar ou pular)
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
        self.jogador.atualizar()

        for obstaculo in self.obstaculos:
            obstaculo.atualizar(game)

        for inimigo in self.inimigos:
            inimigo.atualizar(game)

        for tiro in self.tiros:
            tiro.atualizar(game)

        for tiroInimigo in self.tirosInimigo:
            tiroInimigo.atualizar(game)

        for vida in self.vidas:
            vida.atualizar(game)

        for impulsionador in self.impulsionadores:
            impulsionador.atualizar(game)



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
            # print('pos 0: ', pos[0], ' pos1: ', pos[1] )


    def desenhar(self, game):
        self.desenharTelaBasica(game)

        for obstaculo in self.obstaculos:
            obstaculo.desenhar(game)

        for inimigo in self.inimigos:
            inimigo.desenhar(game)

        for tiro in self.tiros:
            tiro.desenhar(game)

        for tiroInimigo in self.tirosInimigo:
            tiroInimigo.desenhar(game)

        for vida in self.vidas:
            vida.desenhar(self)

        for impulsionador in self.impulsionadores:
            impulsionador.desenhar(self)

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

