import pygame

class Obj:

    def __init__(self,image,x,y):

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect =  self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.frame = 1
        self.frame2 = 1

        self.tick = 0


    def drawing(self,window):
        self.group.draw(window)

    def animacao(self,image, tick, frames):

        self.tick +=1
        if self.tick == tick:
            self.tick = 0
            self.frame +=1

        if self.frame  == frames:
            self.frame = 1

        self.sprite.image = pygame.image.load("assets/" + image + str(self.frame) + ".png")


class Abelha(Obj):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        pygame.mixer.init()

        self.sound_pontos = pygame.mixer.Sound("assets/sounds/score.ogg")

        self.sound_vida = pygame.mixer.Sound("assets/sounds/bateu.ogg")

        self.vidas = 3

        self.pontos = 0

    def movimento_abelha(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0]-30
            self.sprite.rect[1] = pygame.mouse.get_pos()[1]

    def colision(self, group , name):
        name = name

        colision = pygame.sprite.spritecollide(self.sprite, group, True)

        if name  == "flor" and colision:
            self.pontos +=  1
            self.sound_pontos.play()


        elif name == "aranha" and colision:
            self.vidas -= 1
            self.sound_vida.play()

class Texto:

    def __init__(self, size , texto):

        self.font = pygame.font.SysFont("Arial bold", size)
        self.render = self.font.render(texto, False, (255, 255 ,255))

    def draw(self, window , x , y):
        window.blit( self.render, (x, y))

    def update_texto(self, update):
        self.render = self.font.render(update, False, (255, 255, 255))