import pygame

# quaisquer itens que aparecem na tela do jogo, exceto background, botoes e jogador sao classes derivadas da classe Cenario
class Cenario:
    def __init__(self, x, y, imagem, tipo, vel):
        self.x = x
        self.y = y
        self.imagem = imagem
        self.largura = imagem.get_width()
        self.altura = imagem.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura) # retangulo de colisoes
        self.tipo = tipo
        self.vel = vel  # velocidade de atualizacao horizontal na tela


    # identifica o tipo do item do cenario
    def identificacao(self):
        return self.tipo


    # descreve como o item do cenario tem sua posicao horizontal atualiza na tela
    def atualizacaoBasica(self):
        # lembrar de apagar o objeto se ele ja estiver fora da tela
        """"TODO"""
        pass


    # desenha o item do cenario na tela
    def desenhar(self, game):
        game.janela.blit(self.imagem, (self.x, self.y))