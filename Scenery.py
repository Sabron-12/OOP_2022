def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))
screen.fill((254, 213, 162))    # Фон
polygon(screen, (254, 213, 196), [[0, 200], [600, 200], [600, 100], [0, 100]])
circle(screen, (252, 238, 33), (300, 100), 50)



pi = 3.14
polygon(screen, (252, 152, 49), [[2, 205], [13, 190], [13, 205], [2, 205]])
polygon(screen, (252, 152, 49), [[13, 205], [13, 190], [125, 100], [125, 205]])
draw_ellipse_angle(screen, (254, 213, 196), [0, 125, 142, 42], 40)

polygon(screen, (252, 152, 49), [[125, 113], [125, 205], [300, 205], [275, 185],
                                 [230, 185], [145, 135], [135, 120]]) # 1 часть горы (до половины солнца)

polygon(screen, (252, 152, 49), [[300, 205], [600, 205], [560, 170], [545, 177],
                                 [515, 155], [505, 157], [485, 135], [380, 170], [365, 185], [330, 175]])
draw_ellipse_angle(screen, (252, 152, 49), [507, 162, 50, 25], 140)

draw_ellipse_angle(screen, (252, 152, 49), [415, 145, 88, 37], 60)
draw_ellipse_angle(screen, (254, 213, 196), [375, 137, 75, 27], 20) # 2 часть горы (от половины солнца)

polygon(screen, (172, 67, 52), [[0, 250], [2, 250], [10, 255], [10, 300], [0, 300]])
ellipse(screen, (172, 67, 52), [5, 225, 57, 200])
polygon(screen, (172, 67, 52), [[55, 285], [80, 250], [110, 265], [130, 220],
                                [200, 230], [260, 270], [340, 255], [340, 300], [55, 300]])
draw_ellipse_angle(screen, (172, 67, 52), [300, 245, 130, 60], 60)
polygon(screen, (172, 67, 52), [[380, 220], [460, 250], [480, 235], [490, 245],
                                [500, 235], [530, 240], [600, 200], [600, 300], [380, 300]])
draw_ellipse_angle(screen, (254, 213, 162), [393, 215, 75, 30], 150)

polygon(screen, (179, 134, 148), [[0, 400], [600, 400], [600, 275], [0, 300]])  # Тёмно-сиреневая полоса


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
