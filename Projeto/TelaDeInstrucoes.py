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
        if pos[0] > 1110 and pos[0] < 1180 and pos[1] > 630 and pos[1] < 700:
            if evento.type != pygame.MOUSEBUTTONDOWN:
                self.botaoPlay = self.play = pygame.image.load(os.path.join('Imagens', 'play_brilho_1.png'))
            else:
                game.telaAtual = 'Tela de Jogo'
        else:
            self.botaoPlay = self.play = pygame.image.load(os.path.join('Imagens', 'play_1.png'))


   # metodo para lidar com interacoes com o botao que redireciona para a tela de inicio
   def comportamentoBotaoVoltarTelaInicio(self, game, evento, pos):
        if pos[0] > 50 and pos[0] < 150 and pos[1] > 30 and pos[1] < 55:
            if evento.type != pygame.MOUSEBUTTONDOWN:
                self.voltar = self.fonte2.render('VOLTAR', True, AMARELO)
            else:
                game.telaAtual = 'Tela de Inicio'

        else:
            self.voltar = self.fonte2.render('VOLTAR', True, AZULBB)


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
        ins = self.fonte2.render(text, True, AZULBB)
        game.janela.blit(ins, (70, 170 + 100*num))



   # esse metodo deve desenhar tudo que tem na tela, exceto background e botao de audio
   def desenharTela(self, game):
       game.janela.blit(self.title, (500, 60))
       game.janela.blit(self.voltar, (50, 30))
       game.janela.blit(self.jogador, (X_CHAO, 350))
       self.imprimirInstrucoes(game, 0, '- Evite os obstaculos clicando na seta para cima para pular.')
       self.imprimirInstrucoes(game, 1, '- Pressione a barra de espaco para atirar nos inimigos.')
       self.imprimirInstrucoes(game, 2, '- Colete coracoes para ter a possibilidade de ganhar vidas extras.')
       self.imprimirInstrucoes(game, 3, '- Colete boosters para ficar invencivel por 15s.')
       self.imprimirInstrucoes(game, 4, '- Clique no icone de som para desliga-lo.')
       game.janela.blit(self.botaoPlay, (1110, 630))


   def desenhar(self, game):
       self.desenharTelaBasica(game)
       self.desenharTela(game)
       pygame.display.flip()


   def run(self, game):
       while game.telaAtual == self.name and not game.usuarioSaiu:
           self.interpretarEventos(game)
           self.desenhar(game)


