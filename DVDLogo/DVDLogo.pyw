import pygame, sys
import time
import tkinter
pygame.init()

root = tkinter.Tk()
size = width, height = int(root.winfo_screenwidth() - root.winfo_screenwidth()*0.2), int(root.winfo_screenheight() - root.winfo_screenheight()*0.2)
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255
cornerHit = 0

screen = pygame.display.set_mode(size)

dvd = pygame.image.load("unnamed(1).png")
dvdrect = dvd.get_rect()
pygame.display.set_caption("DVD Corner")

font = pygame.font.Font(None, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    dvdrect = dvdrect.move(speed)
    if dvdrect.right > width or dvdrect.left < 0:
        speed[0] = -speed[0]
    if dvdrect.bottom > height or dvdrect.top < 0:
        speed[1] = -speed[1]

    if (dvdrect.right == width and dvdrect.top == 0) or (dvdrect.left == 0 and dvdrect.bottom == height):
        cornerHit += 1
    
    text = font.render("The DVD logo has hit the corner {} times".format(cornerHit), True, white)
    textRect = text.get_rect()
    textRect.center = (width/2, height/2)

    screen.fill(black)
    screen.blit(text, textRect)
    screen.blit(dvd, dvdrect)
    pygame.display.flip()
    time.sleep(0.01) #60fps