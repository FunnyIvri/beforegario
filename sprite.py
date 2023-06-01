import pygame
import keyboard

root_size = [800, 800]
root = pygame.display.set_mode(root_size)
clock = pygame.time.Clock()
fpm = 60
platform_group = pygame.sprite.Group()
run = True


class Player:
    def __init__(self, image, speed, jump_height, start_pos, gravity):
        self.gravity = gravity
        self.image = image
        self.speed = speed
        self.jump_height = jump_height
        self.start_pos = start_pos
        self.player = pygame.image.load(self.image).convert_alpha()
        self.player_rect = self.player.get_rect()
        self.player_rect.x = self.start_pos[0]
        self.player_rect.y = self.start_pos[1]

    def show(self):
        root.blit(self.player, self.player_rect)

    def move(self):
        dx = 0
        dy = self.gravity
        if keyboard.is_pressed("left"):
            dx = -self.speed
        elif keyboard.is_pressed("right"):
            dx = self.speed

        self.player_rect.x += dx
        self.player_rect.y += dy

    def walls(self):

        player_rect = self.player_rect
        if player_rect.left <= 0:
            player_rect.x = root_size[0] - 100

        elif player_rect.right >= root_size[0]:
            player_rect.x = 0
            player_rect.y = player_rect.y - 10

        self.player_rect = player_rect


class Platform(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


player = Player("player.png", 15, 150, [200, 200])
pl = Platform("platform.png", 400, 400)
platform_group.add(pl)
while run:
    root.fill("black")
    player.show()
    player.move()
    player.walls()
    platform_group.draw(root)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(fpm)
    pygame.display.update()
