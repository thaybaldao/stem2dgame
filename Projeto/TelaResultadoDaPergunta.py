from Configuracoes import *
from Tela import *
import pygame
import os


class TelaResultadoDaPergunta(Tela):
   def __init__(self):
       super().__init__()
       self.name = 'Tela Resultado da Pergunta'
       self.botaoPlay = self.play = pygame.image.load(os.path.join('Imagens', 'play.png'))

   def comportamentoBotaoDeJogar(self, game, evento, pos):
       if pos[0] > 610 and pos[0] < 738 and pos[1] > 280 and pos[1] < 399:
           self.botaoPlay = pygame.image.load(os.path.join('Imagens', 'play1.png'))

       else:
           self.botaoPlay = pygame.image.load(os.path.join('Imagens', 'play.png'))

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


   # esse metodo deve desenhar tudo que tem na tela, exceto background e botao de audio
   def desenharTela(self, game):
       game.janela.blit(self.botaoPlay, (610, 280))


   def desenhar(self, game):
       self.desenharTelaBasica(game)
       self.desenharTela(game)
       pygame.display.flip()


   def run(self, game):
       while game.telaAtual == self.name and not game.usuarioSaiu:
           self.interpretarEventos(game)
           self.desenhar(game)