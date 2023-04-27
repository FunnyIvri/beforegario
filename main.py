import pygame
import keyboard

root_size = [800, 800]
root = pygame.display.set_mode(root_size)
clock = pygame.time.Clock()
fpm = 60
platforms = []
platform_group = pygame.sprite.Group()

class Player:
    def __init__(self, image, speed, jump_height, gravity, start_pos):
        self.gravity = gravity
        self.speed = speed
        self.jump_height = jump_height
        self.start_pos = start_pos
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.start_pos[0]
        self.rect.y = self.start_pos[1]

    def show(self):
        root.blit(self.image, self.rect)

    def move(self):
        dx = 0
        dy = self.gravity
        if keyboard.is_pressed("left"):
            dx = -self.speed
        elif keyboard.is_pressed("right"):
            dx = self.speed
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.rect.bottom <= platform.rect.centery:
                dy = 0
        if keyboard.is_pressed("up"):
            for platform in platforms:
                if self.rect.colliderect(platform.rect):
                    dy = -self.jump_height
        self.rect.x += dx
        self.rect.y += dy


    def walls(self):

        player_rect = self.rect
        if player_rect.left <= 0:
            player_rect.x = root_size[0] - 100

        elif player_rect.right >= root_size[0]:
            player_rect.x = 0
            player_rect.y = player_rect.y - 10

        self.rect = player_rect


class Platform(pygame.sprite.Sprite):
    def __init__(self, image, pos, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

    def show(self):
        root.blit(self.image, self.rect)


run = True

player = Player("player.png", 15, 150, 10, [200, 200])

platforms.append(Platform("platform.png", [400, 200], [150, 38]))
platforms.append(Platform("platform.png", [400, 500], [root_size[0], 38]))
for platform in platforms:
    platform_group.add(platform)

while run:
    root.fill("black")

    player.show()
   # player.gravity()
    player.move()
    player.walls()
    print(platform_group.sprites())
    print(type(root))
    platform_group.draw(root)
    #for platform in platforms:
    #    platform.show()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(fpm)
    pygame.display.update()
