import pygame
import keyboard

root_size = [800, 800]
root = pygame.display.set_mode(root_size)
clock = pygame.time.Clock()
fpm = 60
platforms = []


class Player:
    def __init__(self, image, speed, jump_height, start_pos):
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
        dy = 0
        if keyboard.is_pressed("left"):
            dx = -self.speed
        elif keyboard.is_pressed("right"):
            dx = self.speed
        if keyboard.is_pressed("up"):
            for platform in platforms:
                if self.player_rect.colliderect(platform.platform_rect):
                    dy = -self.jump_height

        self.player_rect.x += dx
        self.player_rect.y += dy

    def gravity(self):
        for platform in platforms:
            print(player.player_rect.x)
            print(platform.platform_rect.centerx)
            if not platform.platform_rect.colliderect(player.player_rect):
                player.player_rect.y += 10

        #print(self.player_rect.y)
        #if self.player_rect.y > 200:
        #    self.player_rect.y += -6
        #elif self.player_rect.y < 200:
        #    self.player_rect.y += 10
#
    def walls(self):
        dx =0
        dy=0
        player_rect = self.player_rect
        if player_rect.left <= 0:
            player_rect.x = root_size[0]
        elif player_rect.right >= root_size[0]:
            dx = -6 * self.speed
        if player_rect.top <= 0 or player_rect.bottom >= root_size[1]:
            dy = -6 * self.speed

        self.player_rect.x += dx
        self.player_rect.y += dy


class Platform:
    def __init__(self, image, pos):
        self.image = image
        self.platform = pygame.image.load(self.image).convert_alpha()
        self.platform_rect = self.platform.get_rect()
        self.platform_rect.centerx = pos[0]
        self.platform_rect.centery = pos[1]

    def show(self):
        root.blit(self.platform, self.platform_rect)


run = True

player = Player("player.png", 50, 100, [200, 200])
platforms.append(Platform("platform.png", [200, 400]))
while run:
    root.fill("black")
    player.show()
    player.gravity()
    player.move()
    player.walls()
    for platform in platforms:
        platform.show()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(fpm)
    pygame.display.update()
