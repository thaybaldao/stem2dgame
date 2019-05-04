import pygame


class Cenario:
    def __init__(self, x, y, largura, altura, imagem, tipo, num, vel):
        self.largura = largura
        self.altura = altura
        self.x = x
        self.y = y
        self.imagem = imagem
        self.tipo = tipo
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.num = num
        self.vel = vel

    def identificacao(self):
        return self.tipo

    def atualizacaoBasica(self):
        pass

    def desenhoBasico(self):
        win.blit(self.imagem, (self.x, self.y))