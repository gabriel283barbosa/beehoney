import pygame
from obj import  Obj,Abelha,Texto
import random

class Game:
    def __init__(self):

        self.bg = Obj("assets/bg.png", 0 , 0)
        self.bg2 = Obj("assets/bg.png", 0, -640)

        self.cenas = False

        self.aranha = Obj("assets/spider1.png", random.randrange(0 ,300) , -50)
        self.flor = Obj("assets/florwer1.png", random.randrange(0, 300), -50)
        self.abelha = Abelha("assets/bee1.png", 150 , 600)
        self.change_scene = False
        self.score = Texto(120 , "0")
        self.vida = Texto(60 , "3")

    def draw(self, window):

        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.abelha.drawing(window)
        self.aranha.drawing(window)
        self.flor.drawing((window))
        self.score.draw(window, 150 , 50)
        self.vida.draw(window, 50 , 50)

    def update(self):

        self.score.update_texto(str(self.abelha.pontos))
        self.vida.update_texto(str(self.abelha.vidas))

        self.move_bg()

        self.aranha.animacao("spider", 8 , 5)

        self.movimento_aranha()

        self.abelha.animacao("bee", 2 , 5)

        self.abelha.colision(self.aranha.group , "aranha")

        self.abelha.colision(self.flor.group, "flor")

        self.movimento_flor()

        self.flor.animacao("florwer" , 8 , 3)

        self.gameover()

    def move_bg(self):
#movimenta o background
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4

        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640

    def movimento_aranha(self):
        self.aranha.sprite.rect[1] += 10

        #aliminar a aranha caso ela passe da tela
        if self.aranha.sprite.rect[1] >= 700:
            self.aranha.sprite.kill()
            #adicionando a aranha dnv
            self.aranha = Obj("assets/spider1.png", random.randrange(0 ,300) , -50)

    def movimento_flor(self):
        self.flor.sprite.rect[1] += 5

        # aliminar a flor caso ela passe da tela
        if self.flor.sprite.rect[1] >= 700:
            self.flor.sprite.kill()
            # adicionando a flor dnv
            self.flor = Obj("assets/florwer1.png", random.randrange(0, 300), -50)

    def gameover(self):
        if self.abelha.vidas <= 0:
            self.change_scene = True
