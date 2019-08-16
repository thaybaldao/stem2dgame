#from Configuracoes import *
from Tela import *
import pygame
import os

class TelaDeInicio(Tela):
   def __init__(self, game):
       super().__init__()
       self.name = 'Tela de Inicio'
       self.botaoPlay = self.play = pygame.image.load(os.path.join('Imagens', 'play_1.png'))
       self.fonte1 = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 95)
       self.fonte2 = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 70)
       self.title = self.fonte1.render(TITULO, True, AZULBB)
       self.inst = self.fonte2.render('INSTRUÇÕES', True, AZULBB)
       self.jogador = pygame.image.load(os.path.join('Imagens', 'personagem_principal_FEC_1.png'))

       game.administradorDeAudio.tocarMusicaDeFundo(os.path.join('Musica', 'menuLoop.wav'), game)

   # metodo para lidar com interacoes com o botao que direciona para a tela de instrucoes
   def comportamentoBotaoDeInstrucoes(self, game, evento, pos):
       pass

   # metodo para lidar com interacoes com o botao de jogar
   def comportamentoBotaoDeJogar(self, game, evento, pos):
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

           # checa se o usuario quer jogar
           self.comportamentoBotaoDeJogar(game, evento, pos)

           # print("pos0: ", pos[0], " pos1: ", pos[1])

   # esse metodo deve desenhar tudo que tem na tela, exceto tela de fundo e botao de audio
   def desenharTela(self, game):
       game.janela.blit(self.title, (315, 200))
       game.janela.blit(self.botaoPlay, (600, 365))
       game.janela.blit(self.inst, (445, 540))
       game.janela.blit(self.jogador, (X_CHAO, 350))

   def desenhar(self, game):
       self.desenharTelaBasica(game)
       self.desenharTela(game)
       pygame.display.flip()

   def run(self, game):
       while game.telaAtual == self.name and not game.usuarioSaiu:
           self.interpretarEventos(game)
           self.desenhar(game)