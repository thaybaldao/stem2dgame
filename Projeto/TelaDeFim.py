from Configuracoes import *
from TelaDeJogo import *
from Tela import *
import pygame
import os

class TelaDeFim(Tela):
   def __init__(self, game):
       super().__init__()
       self.name = 'Tela de Fim'
       self.fonte1 = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 95)
       self.fonte2 = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 65)
       self.botaoPlay = pygame.image.load(os.path.join('Imagens', 'replay_2.png'))
       self.fimJogo = self.fonte1.render('FIM DE JOGO!', True, AMARELO)
       self.pontuacaoFinal = self.fonte2.render('SCORE FINAL:', True, AZULBB)
       self.melhorPontuacao = self.fonte2.render('MELHOR SCORE:', True, AZULBB)
       self.jogarNovamente = self.fonte2.render('Jogar novamente?', True, AZULBB)

       self.pontuacaoNum = game.pontuacao

       # atualiza a melhor pontuacao do jogo cada vez que o usuario ultrapassa a melhor pontuacao ate entao
       if game.pontuacao > game.melhorPontuacao:
           game.melhorPontuacao = game.pontuacao

   # metodo para lidar com interacoes com o botao de replay
   def comportamentoBotaoDeReplay(self, game, evento, pos):
       pass


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


   def imprimirPontuacao(self, game):
       pass

   def imprimirMaiorPontuacao(self, game):
       pass

   # esse metodo deve desenhar tudo que tem na tela, exceto tela de fundo e botao de audio
   def desenharTela(self, game):
       self.imprimirPontuacao(game)
       self.imprimirMaiorPontuacao(game)
       game.janela.blit(self.botaoPlay, (LARGURA_DA_TELA/2 - 20, 285))
       game.janela.blit(self.fimJogo, (LARGURA_DA_TELA/2 - 250, 120))
       game.janela.blit(self.pontuacaoFinal, (LARGURA_DA_TELA/2 - 207, 460))
       game.janela.blit(self.melhorPontuacao, (LARGURA_DA_TELA/2 - 242, 580))

   def desenhar(self, game):
       self.desenharTelaBasica(game)
       self.desenharTela(game)
       pygame.display.flip()


   def run(self, game):
       while game.telaAtual == self.name and not game.usuarioSaiu:
           self.interpretarEventos(game)
           self.desenhar(game)





