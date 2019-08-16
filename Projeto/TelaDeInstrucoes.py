from Configuracoes import *
from Tela import *
import pygame
import os

class TelaDeInstrucoes(Tela):
   def __init__(self):
       super().__init__()
       self.name = "Tela de Instrucoes"
       fonte1 = self.font = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 70)
       self.title = fonte1.render('INSTRUCOES', True, NAVY)
       self.fonte2 = self.font = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 30)
       self.voltar = self.fonte2.render('VOLTAR', True, AZULBB)
       self.botaoPlay = self.play = pygame.image.load(os.path.join('Imagens', 'play_1.png'))
       self.jogador = pygame.image.load(os.path.join('Imagens', 'personagem_principal_FEC_1.png'))

   # metodo para lidar com interacoes com o botao de jogar
   def comportamentoBotaoDeJogar(self, game, evento, pos):
        pass

   # metodo para lidar com interacoes com o botao que redireciona para a tela de inicio
   def comportamentoBotaoVoltarTelaInicio(self, game, evento, pos):
        pass

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

           # print("pos0: ", pos[0], " pos1: ", pos[1])

   def imprimirInstrucoes(self, game, num, text):
        pass

   # esse metodo deve desenhar tudo que tem na tela, exceto tela de fundo e botao de audio
   def desenharTela(self, game):
       pass


   def desenhar(self, game):
       self.desenharTelaBasica(game)
       self.desenharTela(game)
       pygame.display.flip()


   def run(self, game):
       while game.telaAtual == self.name and not game.usuarioSaiu:
           self.interpretarEventos(game)
           self.desenhar(game)


