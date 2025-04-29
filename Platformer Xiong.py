import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#define game variable
tile_size = 50


#load images
sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')

def draw_grid():
    for line in range(0, 6):
        pygame.draw.line(screen, (255, 255, 255), (0, line * title_size), (screen_width, line * title_size)
        pygame.draw.line(screen, (255, 255, 255), (line * title_size, 0), (line * title_size, screen height)



class World():
    def __init__(self, data):
        self.tile_list = []

        #load images
        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grass.png')

        row_count = 0
        for now in data:
            col_count = 0
            for tile in row:
                if title == 1:
                    img = pygame.tranform.scale(dirt_img, (tile_size, title_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                            row_count = 0
        for now in data:
            col_count = 0
            for tile in row:
                if title == 2:
                    img = pygame.tranform.scale(grass_img, (tile_size, title_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

world_data = [
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 2, 2, 2, 1],
]

world = World(world_data)

run = True
while run:

    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (100, 100))

    world.draw()

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
