import pygame
from obj import Obj, Abelha
from menu import  Menu,GamerOver
from game import Game


class Main:
    def __init__(self, syzex, sizey, title):

        pygame.font.init()

        pygame.mixer.init()

        pygame.init()

        pygame.mixer.music.load("assets/sounds/bg.ogg")
        pygame.mixer.music.play(-1)

        self.window = pygame.display.set_mode([syzex,sizey])

        self.title = pygame.display.set_caption(title)

        self.tela_inicial = Obj("assets/start.png", 0, 0)

        self.loop = True

        self.fps = pygame.time.Clock()

        self.menu = Menu("assets/start.png")

        self.gamerover = GamerOver("assets/gameover.png")

        self.game = Game()


    def draw (self):
        if not self.menu.cenas:
            self.menu.draw(self.window)

        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
        elif not self.gamerover.cenas:
            self.gamerover.draw(self.window)
        else:
            self.menu.cenas = False
            self.game.change_scene = False
            self.gamerover.cenas = False
            self.game.abelha.vidas = 3
            self.game.abelha.pontos = 0
    def events (self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            if not self.menu.cenas:
                self.menu.events(events)
            elif not self.game.change_scene:
                self.game.abelha.movimento_abelha(events)
            else:
                self.gamerover.events(events)

    def update (self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()

            pygame.display.update()

game = Main(360, 640, "ABELHA")
game.update()