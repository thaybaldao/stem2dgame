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

        game.administradorDeAudio.tocarMusicaDeFundo(os.path.join('Musica', 'music1.wav'), game)


    def computarPontuacao(self, game):
        game.pontuacao += 1

    def imprimirPontuacao(self, game):
        self.pontuacao = self.fonte1.render("SCORE: ", True, ROXO)
        self.pontuacaoNum = self.fonte1.render(str(game.pontuacao), True, ROXO)
        game.janela.blit(self.pontuacao, (35, ALTURA_DA_TELA - 50))
        game.janela.blit(self.pontuacaoNum, (140, ALTURA_DA_TELA - 50))

    # imprime barra de vidas
    def imprimirBarraDeVidas(self, game):
        if game.vidasExtras > 0:
            for i in range(game.vidasExtras):
                game.janela.blit(pygame.image.load(os.path.join('Imagens', 'vida.png')), (70*i + 20, 20))

    def computarTempoDeInvencibilidade(self, game):
        if game.ehInvencivel:
            if game.tempoDeInvencibilidade > 0:
                game.tempoDeInvencibilidade -=1
            else:
                game.ehInvencivel = False
                game.tempoDeInvencibilidade = 15


    # imprime tempo de invencibilidade na Tela a partir do momento em que a varivel game.ehInvencivel se tornar verdadeira, por x segundos
    def imprimirTempoDeInvencibilidade(self, game):
        if game.ehInvencivel:
            self.invencibilidade = self.fonte1.render("INVENCIBILIDADE: ", True, AZULBB)
            self.invencibilidadeNum = self.fonte1.render(str(game.tempoDeInvencibilidade), True, AZULBB)
            game.janela.blit(self.invencibilidade, (LARGURA_DA_TELA - 335, ALTURA_DA_TELA - 50))
            game.janela.blit(self.invencibilidadeNum, (LARGURA_DA_TELA - 80, ALTURA_DA_TELA - 50))


    # cria itens do cenario na tela
    def criarCenario(self, game):
        if not self.batalha:
            r = random.randrange(0, game.aparecimentoElementos)
            if r < 8:
                 if len(game.obstaculos) == 0:
                     game.obstaculos.append(Obstaculo(LARGURA_DA_TELA, 562 + 8*(r%4), pygame.image.load(os.path.join('Imagens', 'obstaculo_1_1.png')), 10 + game.dvel))

                 elif game.obstaculos[-1].x + game.obstaculos[-1].largura + self.tolerancia < LARGURA_DA_TELA:
                     game.obstaculos.append(Obstaculo(LARGURA_DA_TELA, 562 + 8*(r%4), pygame.image.load(os.path.join('Imagens', 'obstaculo_1_1.png')), 5 + game.dvel))
                     if r == 7 and game.vidasExtras < 3 and game.pontuacao > 30 and len(game.vidas) == 0 and len(game.impulsionadores) == 0:
                         game.vidas.append(Vida(LARGURA_DA_TELA + game.obstaculos[-1].largura + 50, 620, pygame.image.load(os.path.join('Imagens', 'vida.png')), 5 + game.dvel))
            elif r < 16:
                 if len(game.obstaculos) == 0:
                     game.obstaculos.append(Obstaculo(LARGURA_DA_TELA, 585 - 5*(r%4), pygame.image.load(os.path.join('Imagens', 'obstaculo_1_2.png')), 10 + game.dvel))

                 elif game.obstaculos[-1].x + game.obstaculos[-1].largura + self.tolerancia < LARGURA_DA_TELA:
                     game.obstaculos.append(Obstaculo(LARGURA_DA_TELA, 585 - 5*(r%4), pygame.image.load(os.path.join('Imagens', 'obstaculo_1_2.png')), 5 + game.dvel))
                     if r == 15 and not game.ehInvencivel and game.pontuacao > 30 and len(game.impulsionadores) == 0 and len(game.vidas) == 0:
                         game.impulsionadores.append(Impulsionador(LARGURA_DA_TELA + game.obstaculos[-1].largura + 50, 580, pygame.image.load(os.path.join('Imagens', 'impulsionador_1.png')), 5 + game.dvel))

            elif r < 18 and game.vidasExtras < 3 and game.pontuacao > 30 and game.pontuacao%5 == 0 and len(game.vidas) == 0 and len(game.impulsionadores) == 0:
                game.vidas.append(Vida(LARGURA_DA_TELA, 200 + 5*r, pygame.image.load(os.path.join('Imagens', 'vida.png')), 5 + game.dvel))

            elif r < 22 and not game.ehInvencivel and game.pontuacao > 30 and game.pontuacao % 5 == 0 and len(game.impulsionadores) == 0 and len(game.vidas) == 0:
                 game.impulsionadores.append(Impulsionador(LARGURA_DA_TELA, 150 + 5*r, pygame.image.load(os.path.join('Imagens', 'impulsionador_1.png')), 5 + game.dvel))
        elif len(game.inimigos) == 0 and self.tempoDeBatalha > 0:
                game.inimigos.append(Inimigo(LARGURA_DA_TELA, 563, pygame.image.load(os.path.join('Imagens', 'inimigo_1.png')), 5 + game.dvel, int(game.pontuacao/25), '1'))


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

        # making background move
        self.imagemDeFundoX -= 2
        self.imagemDeFundoX2 -= 2
        if self.imagemDeFundoX < self.imagemDeFundo.get_width() * -1:
            self.imagemDeFundoX = self.imagemDeFundo.get_width()
        if self.imagemDeFundoX2 < self.imagemDeFundo.get_width() * -1:
            self.imagemDeFundoX2 = self.imagemDeFundo.get_width()

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
        # limpar cenario
        game.obstaculos.clear()
        game.inimigos.clear()
        game.vidas.clear()
        game.impulsionadores.clear()
        game.tiros.clear()
        game.tirosInimigo.clear()
        self.desenhar(game)

        # trocar musica
        game.administradorDeAudio.tocarMusicaDeFundo(os.path.join('Musica', 'music2.wav'), game)

        # escrever mensagem para comecar a batalha
        self.batalhaTexto = self.fonte2.render("BATALHA!", True, ROXO)
        game.janela.blit(self.batalhaTexto, (320, 330))
        pygame.display.flip()
        pygame.time.wait(600)
        self.batalhaTexto = self.fonte2.render("BATALHA!", True, AMARELO)
        game.janela.blit(self.batalhaTexto, (320, 330))
        pygame.display.flip()
        pygame.time.wait(600)
        self.batalhaTexto = self.fonte2.render("BATALHA!", True, ROXO)
        game.janela.blit(self.batalhaTexto, (320, 330))
        pygame.display.flip()
        pygame.time.wait(600)

        # inicializar constantes da batalha
        self.batalha = True
        self.tempoDeBatalha = 10 + random.randrange(0, 5)

    def telaBomTrabalho(self, game):
        # limpar cenario
        game.inimigos.clear()
        game.tiros.clear()
        game.tirosInimigo.clear()
        self.desenhar(game)

        # trocar musica
        game.administradorDeAudio.tocarMusicaDeFundo(os.path.join('Musica', 'music1.wav'), game)

        # escrever mensagem de bom trabalho
        self.batalhaTexto = self.fonte2.render("BOM TRABALHO!", True, ROXO)
        game.janela.blit(self.batalhaTexto, (120, 330))
        pygame.display.flip()
        pygame.time.wait(600)
        self.batalhaTexto = self.fonte2.render("BOM TRABALHO!", True, AMARELO)
        game.janela.blit(self.batalhaTexto, (120, 330))
        pygame.display.flip()
        pygame.time.wait(600)
        self.batalhaTexto = self.fonte2.render("BOM TRABALHO!", True, ROXO)
        game.janela.blit(self.batalhaTexto, (120, 330))
        pygame.display.flip()
        pygame.time.wait(600)

    def computarTempoDeBatalha(self, game):
        if self.batalha:
            if self.tempoDeBatalha > 0:
                self.tempoDeBatalha -=1
            elif len(game.inimigos) == 0:
                self.batalha = False
                self.telaBomTrabalho(game)

    def run(self, game):

        if game.ultimaTela == 'Tela Resultado da Pergunta':
            game.retirarPergunta()
            game.administradorDeAudio.tocarEfeitoSonoro(os.path.join('Musica', 'life.wav'), game)
            pygame.time.wait(1500)
        elif game.ultimaTela == 'Tela de Perguntas':
            game.retirarPergunta()

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



