#from Configuracoes import *
from Tela import *
import pygame
import os

class TelaDeInicio(Tela):
   def __init__(self):
       super().__init__()
       self.name = 'Tela de Inicio'
       self.botaoPlay = self.play = pygame.image.load(os.path.join('Imagens', 'play.png'))
       self.fonte1 = self.font = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 105)
       self.fonte2 = self.font = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 80)
       self.title = self.fonte1.render(TITULO, True, ROXO)
       self.inst = self.fonte2.render('INSTRUÇÕES', True, ROXO)


   # metodo para lidar com interacoes com o botao que direciona para a tela de instrucoes
   def comportamentoBotaoDeInstrucoes(self, game, evento, pos):
       if pos[0] > 430 and pos[0] < 840 and pos[1] > 540 and pos[1] < 600:
           self.inst = self.fonte2.render('INSTRUCOES', True, AMARELO)

       else:
           self.inst = self.fonte2.render('INSTRUCOES', True, ROXO)

       if evento.type == pygame.MOUSEBUTTONDOWN:
           # check if user wants to see instructions
           if pos[0] > 430 and pos[0] < 840 and pos[1] > 540 and pos[1] < 600:
               game.telaAtual = 'Tela de Instrucoes'

   # metodo para lidar com interacoes com o botao de jogar
   def comportamentoBotaoDeJogar(self, game, evento, pos):
       if pos[0] > 570 and pos[0] < 700 and pos[1] > 330 and pos[1] < 450:
           self.botaoPlay = pygame.image.load(os.path.join('Imagens', 'play1.png'))

       else:
           self.botaoPlay = pygame.image.load(os.path.join('Imagens', 'play.png'))

       if evento.type == pygame.MOUSEBUTTONDOWN:
           # check if user wants to play
           if pos[0] > 570 and pos[0] < 700 and pos[1] > 330 and pos[1] < 450:
               game.telaAtual = 'Tela de Jogo'


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



   # esse metodo deve desenhar tudo que tem na tela, exceto background e botao de audio
   def desenharTela(self, game):
       game.janela.blit(self.title, (LARGURA_DA_TELA/2 - 350, ALTURA_DA_TELA/2 - 200))
       game.janela.blit(self.botaoPlay, (LARGURA_DA_TELA/2 - 60, ALTURA_DA_TELA/2 - 50))
       game.janela.blit(self.inst, (LARGURA_DA_TELA/2 -  200, ALTURA_DA_TELA/2 + 160))

   def desenhar(self, game):
       self.desenharTelaBasica(game)
       self.desenharTela(game)
       pygame.display.flip()


   def run(self, game):
       while game.telaAtual == self.name and not game.usuarioSaiu:
           self.interpretarEventos(game)
           self.desenhar(game)