#test
import pygame

pygame.init()

print("init")

pygame.mixer.music.load("/home/pi/Steps_code_and_files/Audio/393320__truword__night-on-long-island.mp3")
pygame.mixer.music.play(-1,0)
