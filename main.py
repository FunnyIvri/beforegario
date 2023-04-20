import pygame
import keyboard

root_size = [800, 800]
root = pygame.display.set_mode(root_size)
clock = pygame.time.Clock()
fpm = 60


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
            dx = -15
        elif keyboard.is_pressed("right"):
            dx = 15
        if keyboard.is_pressed("up"):
            dy = -self.jump_height
        elif keyboard.is_pressed("down"):
            dy = -self.jump_height
        self.player_rect.x += dx
        self.player_rect.y += dy

    def gravity(self):
        print(self.player_rect.y)
        if self.player_rect.y > 200:

            self.player_rect.y += -6
        elif self.player_rect.y < 200:
            self.player_rect.y += 10
    def walls(self):
        player_rect = self.player_rect
        if player_rect.left <= 0 or player_rect.right >= root[0]:
            dx = -1 * self.speed

        if player_rect.top <= 0 or player_rect.bottom >= root[1]:
            dy = -1 * self.speed


        self.player_rect.x += dx
        self.player_rect.y += dy
run = True

player = Player("player.png", 2, 1, [200, 200])
while run:
    root.fill("black")
    player.show()
    player.gravity()
    player.move()
    player.walls()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(fpm)
    pygame.display.update()
