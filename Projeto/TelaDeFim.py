
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
       self.scoreFinal = self.fonte2.render('SCORE FINAL:', True, AZULBB)
       self.melhorScore = self.fonte2.render('MELHOR SCORE:', True, AZULBB)
       self.jogarNovamente = self.fonte2.render('Jogar novamente?', True, AZULBB)

       self.scoreNum = game.score
       if game.score > game.bestScore:
           game.bestScore = game.score

       game.obstaculos.clear()
       game.inimigos.clear()
       game.vidas.clear()
       game.impulsionadores.clear()
       game.tiros.clear()
       game.tirosInimigo.clear()

       game.administradorDeAudio.tocarMusicaDeFundo(os.path.join('Musica', 'menuLoop.wav'), game)



   # metodo para lidar com interacoes com o botao de replay: 610, 280
   def comportamentoBotaoDeReplay(self, game, evento, pos):
       if pos[0] > 610 and pos[0] < 675 and pos[1] > 285 and pos[1] < 350:
           if evento.type != pygame.MOUSEBUTTONDOWN:
               self.botaoPlay = pygame.image.load(os.path.join('Imagens', 'replay_brilho_2.png'))
           else:
               game.novoJogo()
               game.ultimaTela = 'Tela de Fim'
               game.telaAtual = 'Tela de Jogo'

       else:
           self.botaoPlay = pygame.image.load(os.path.join('Imagens', 'replay_2.png'))


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
       self.scoreFinalNum = self.fonte1.render(str(self.scoreNum), True, AMARELO)
       game.janela.blit(self.scoreFinalNum, (790, 445))

   # desenhar o maior score na tela
   def imprimirMaiorScore(self, game):
       self.melhorScoreNum = self.fonte1.render(str(game.bestScore), True, AMARELO)
       game.janela.blit(self.melhorScoreNum, (815, 565))


   # esse metodo deve desenhar tudo que tem na tela, exceto background e botao de audio
   def desenharTela(self, game):
       self.imprimirScore(game)
       self.imprimirMaiorScore(game)
       game.janela.blit(self.botaoPlay, (LARGURA_DA_TELA/2 - 20, 285))
       game.janela.blit(self.fimJogo, (LARGURA_DA_TELA/2 - 250, 120))
       game.janela.blit(self.scoreFinal, (LARGURA_DA_TELA/2 - 207, 460))
       game.janela.blit(self.melhorScore, (LARGURA_DA_TELA/2 - 242, 580))

   def desenhar(self, game):
       self.desenharTelaBasica(game)
       self.desenharTela(game)
       pygame.display.flip()


   def run(self, game):
       while game.telaAtual == self.name and not game.usuarioSaiu:
           self.interpretarEventos(game)
           self.desenhar(game)





