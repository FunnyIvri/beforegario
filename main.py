import random
import pygame
import keyboard
def loop():
    root_size = [800, 900]
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
            for platform in platform_group:
                if self.rect.colliderect(platform.rect) and self.rect.bottom <= platform.rect.centery:
                    dy = 0
            if self.rect.bottom >= 250:
                scroll = 50
            if keyboard.is_pressed("up"):
                for platform in platform_group:
                    if self.rect.colliderect(platform.rect):
                        dy = -self.jump_height

            self.rect.x += dx
            self.rect.y += dy
            if not keyboard.is_pressed("up"): return scroll

        def walls(self):

            player_rect = self.rect
            if player_rect.left <= -90:
                player_rect.x = root_size[0] - 100

            elif player_rect.right >= root_size[0]+90:
                player_rect.x = 0
                player_rect.y = player_rect.y - 10


            if player_rect.bottom >= root_size[1]+90:
                self.rect.x = self.start_pos[0]
                self.rect.y = self.start_pos[1]
                loop()


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


    for i in range(5):
        x = random.randint(0,root_size[0])
        y = random.randint(0,root_size[1])
        print(x)
        platform_group.add(Platform("platform.png", [x, y], [150, 38]))


    while run:
        root.fill("black")

        player.show()
       # player.gravity()
        player.move()
        player.walls()
        platform_group.draw(root)
        #for platform in platforms:
        #    platform.show()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        clock.tick(fpm)
        pygame.display.update()

loop()