import pygame


class Cenario:
    def __init__(self, x, y, imagem, tipo, num, vel):
        self.x = x
        self.y = y
        self.imagem = imagem
        self.largura = imagem.get_width()
        self.altura = imagem.get_height()
        self.tipo = tipo
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.num = num
        self.vel = vel

    def identificacao(self):
        return self.tipo

    def atualizacaoBasica(self):
        pass

    def desenhar(self, game):
        game.janela.blit(self.imagem, (self.x, self.y))