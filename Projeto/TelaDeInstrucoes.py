from Configuracoes import *
from Tela import *
import pygame
import os


class TelaDeInstrucoes(Tela):
   def __init__(self):
       super().__init__()
       self.name = "Tela de Instrucoes"
       self.fonte1 = self.font = pygame.font.Font(os.path.join('Fontes', '04B_30__.TTF'), 40)
       #self.fonte2 = self.font = pygame.font.Font(os.path.join('Fontes', '04B_30__.TTF'), 20)
       self.title = self.fonte1.render('INSTRUCOES', True, NAVY)
       self.jogar = self.fonte1.render('JOGAR!', True, AZULBB)
       self.voltar = self.fonte1.render('VOLTAR', True, AZULBB)
       #self.botaoPlay = self.play = pygame.image.load(os.path.join('Imagens', 'Play.png'))


   # metodo para lidar com interacoes com o botao de jogar
   def comportamentoBotaoDeJogar(self, game, evento, pos):
       if pos[0] > 200 and pos[0] < 400 and pos[1] > 600 and pos[1] < 640:
           self.jogar = self.fonte1.render('JOGAR!', True, AZULBB)

       else:
           self.jogar = self.fonte1.render('JOGAR!', True, NAVY)

       if evento.type == pygame.MOUSEBUTTONDOWN:
           # check if user wants to play
           if pos[0] > 200 and pos[0] < 400 and pos[1] > 600 and pos[1] < 640:
               game.telaAtual = 'Tela de Perguntas'

   # metodo para lidar com interacoes com o botao que redireciona para a tela de inicio
   def comportamentoBotaoVoltarTelaInicio(self, game, evento, pos):
       if pos[0] > 600 and pos[0] < 800 and pos[1] > 600 and pos[1] < 640:
           self.voltar = self.fonte1.render('VOLTAR', True, AZULBB)

       else:
           self.voltar = self.fonte1.render('VOLTAR', True, NAVY)

       if evento.type == pygame.MOUSEBUTTONDOWN:
           # check if user wants to play
           if pos[0] > 600 and pos[0] < 800 and pos[1] > 600 and pos[1] < 640:
               game.telaAtual = 'Tela de Inicio'


   def interpretarEventos(self, game):
       game.clock.tick(game.fps)

       for evento in pygame.event.get():
           pos = pygame.mouse.get_pos()

           # checa se o usuario quer sair do jogo
           self.comportamentoBotaoDeSair(game, evento)

           # checa se o usuario quer tirar o som
           self.comportamentoBotaoDeAudio(game, evento, pos)

           # checa se o usuario quer jogar
           self.comportamentoBotaoDeJogar(game, evento, pos)

           # checa se o usuario quer voltar para a tela de inicio
           self.comportamentoBotaoVoltarTelaInicio(game, evento, pos)


   # esse metodo deve desenhar tudo que tem na tela, exceto background e botao de audio
   def desenharTela(self, game):
       game.janela.blit(self.jogar, (200, 600))
       game.janela.blit(self.voltar, (600, 600))


   def imprimirInstrucoes(self, game, num, text):
        fonte2 = pygame.font.Font(os.path.join('Fontes', '04B_30__.TTF'), 20)
        ins = fonte2.render(text, True, NAVY)
        game.janela.blit(ins, (70, 40 + 75*num))

   def desenhar(self, game):
       self.desenharTelaBasica(game)
       self.desenharTela(game)
       game.janela.blit(self.title, (200, 20))
       self.imprimirInstrucoes(game, 1, '- Clique na barra de espaco para pular.')
       self.imprimirInstrucoes(game, 2, '- Evite os obstáculos!')
       self.imprimirInstrucoes(game, 3, '- Colete coracoes para ter a possibilidade de ganhar vidas extras.')
       self.imprimirInstrucoes(game, 4, '- Colete boosters para ficar invencivel por 15s.')
       self.imprimirInstrucoes(game, 5, '- Colete estrelas para ficar invencivel por 15s.')
       self.imprimirInstrucoes(game, 6, '- Clique no icone de som para desliga-lo.')

       pygame.display.flip()

   def run(self, game):
       while game.telaAtual == self.name and not game.usuarioSaiu:
           self.interpretarEventos(game)
           self.desenhar(game)


