import pygame

WIDTH = 1030
HEIGHT = 700


def init_screen(screen, image):
    pygame.display.set_caption('Warriors Simulation')
    screen.blit(image, [0, 0])

    return screen
