#test
import os
import pygame

pygame.init()

print("init")
index = 0
test = ["a", "b", "c", "d", "e", "f", "g", "h"]

print(len(test))

i = 0
for letter in test:
    if(letter == "h"):
        index = i
        break
    else:
        i += 1
        continue

for letter in test[index:]:
    print(letter)

