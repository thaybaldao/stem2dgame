from Configuracoes import *
from Tela import *
import pygame
import os


class TelaDePerguntas(Tela):
   def __init__(self):
       super().__init__()
       self.name = 'Tela de Perguntas'
       self.alternativaA = pygame.image.load(os.path.join('Imagens', 'alternativa_A.png'))
       self.alternativaB = pygame.image.load(os.path.join('Imagens', 'alternativa_B.png'))
       self.alternativaC = pygame.image.load(os.path.join('Imagens', 'alternativa_C.png'))
       self.alternativaD = pygame.image.load(os.path.join('Imagens', 'alternativa_D.png'))

   # metodo para lidar com a escolha da alternativa A
   def comportamentoBotaoAlternativaA(self, game, evento, pos):
       if evento.type == pygame.MOUSEBUTTONDOWN:
           # check if user wants to play
           if pos[0] > 200 and pos[0] < 250 and pos[1] > 600 and pos[1] < 640:
               game.telaAtual = 'Tela de Jogo'


   # metodo para lidar com a escolha da alternativa B
   def comportamentoBotaoAlternativaB(self, game, evento, pos):
       if evento.type == pygame.MOUSEBUTTONDOWN:
           # check if user wants to play
           if pos[0] > 300 and pos[0] < 350 and pos[1] > 600 and pos[1] < 640:
               game.telaAtual = 'Tela de Jogo'

   # metodo para lidar com a escolha da alternativa C
   def comportamentoBotaoAlternativaC(self, game, evento, pos):
       if evento.type == pygame.MOUSEBUTTONDOWN:
           # check if user wants to play
           if pos[0] > 400 and pos[0] < 450 and pos[1] > 600 and pos[1] < 640:
               game.telaAtual = 'Tela de Jogo'


   # metodo para lidar com a escolha da alternativa D
   def comportamentoBotaoAlternativaD(self, game, evento, pos):
       if evento.type == pygame.MOUSEBUTTONDOWN:
           # check if user wants to play
           if pos[0] > 500 and pos[0] < 550 and pos[1] > 600 and pos[1] < 640:
               game.telaAtual = 'Tela de Jogo'


   def interpretarEventos(self, game):
       game.clock.tick(game.fps)

       for evento in pygame.event.get():
           pos = pygame.mouse.get_pos()

           # checa se o usuario quer sair do jogo
           self.comportamentoBotaoDeSair(game, evento)

           # checa se o usuario quer tirar o som
           self.comportamentoBotaoDeAudio(game, evento, pos)

           # checa se o usuario escolheu a alternativa A
           self.comportamentoBotaoAlternativaA(game, evento, pos)

           # checa se o usuario escolheu a alternativa B
           self.comportamentoBotaoAlternativaB(game, evento, pos)

           # checa se o usuario escolheu a alternativa C
           self.comportamentoBotaoAlternativaC(game, evento, pos)

           # checa se o usuario escolheu a alternativa D
           self.comportamentoBotaoAlternativaD(game, evento, pos)


   # esse metodo deve desenhar tudo que tem na tela, exceto background e botao de audio
   def desenharTela(self, game):
       game.janela.blit(self.alternativaA, (150, 200))
       game.janela.blit(self.alternativaB, (150, 600))
       game.janela.blit(self.alternativaC, (850, 200))
       game.janela.blit(self.alternativaD, (850, 600))


   def desenhar(self, game):
       self.desenharTelaBasica(game)
       self.desenharTela(game)
       pygame.display.flip()


   def run(self, game):
       while game.telaAtual == self.name and not game.usuarioSaiu:
           self.interpretarEventos(game)
           self.desenhar(game)


