from Configuracoes import *
from Tela import *
import pygame
import os


class TelaDeFim(Tela):
   def __init__(self):
       super().__init__()
       self.name = 'Tela de Fim'
       self.botaoPlay = self.play = pygame.image.load(os.path.join('Imagens', 'replay.png'))


   # metodo para lidar com interacoes com o botao de replay
   def comportamentoBotaoDeReplay(self, game, evento, pos):
       if pos[0] > 610 and pos[0] < 738 and pos[1] > 280 and pos[1] < 399:
           self.botaoPlay = pygame.image.load(os.path.join('Imagens', 'replay1.png'))

       else:
           self.botaoPlay = pygame.image.load(os.path.join('Imagens', 'replay.png'))

       if evento.type == pygame.MOUSEBUTTONDOWN:
           # check if user wants to play
           if pos[0] > 610 and pos[0] < 738 and pos[1] > 280 and pos[1] < 399:
               game.telaAtual = 'Tela de Jogo'

   def interpretarEventos(self, game):
       game.clock.tick(game.fps)

       for evento in pygame.event.get():
           pos = pygame.mouse.get_pos()

           # checa se o usuario quer sair do jogo
           self.comportamentoBotaoDeSair(game, evento)

           # checa se o usuario quer tirar o som
           self.comportamentoBotaoDeAudio(game, evento, pos)

           # checa se o usuario quer reiniciar o jogo
           self.comportamentoBotaoDeReplay(game, evento, pos)


   # desenhar o score do jogo na tela
   def imprimirScore(self, game):
       """TODO"""
       pass


   # desenhar o maior score na tela
   def imprimirMaiorScore(self, game):
       """TODO"""
       pass


   # esse metodo deve desenhar tudo que tem na tela, exceto background e botao de audio
   def desenharTela(self, game):
       self.imprimirScore(game)
       self.imprimirMaiorScore(game)
       game.janela.blit(self.botaoPlay, (610, 280))

   def desenhar(self, game):
       self.desenharTelaBasica(game)
       self.desenharTela(game)
       pygame.display.flip()


   def run(self, game):
       while game.telaAtual == self.name and not game.usuarioSaiu:
           self.interpretarEventos(game)
           self.desenhar(game)





