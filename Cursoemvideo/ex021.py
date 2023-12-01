# Tocando uma musquinha

import pygame
pygame.init()
pygame.mixer.music.load('musquinha.mp3')
pygame.mixer.music.play()
pygame.event.wait()