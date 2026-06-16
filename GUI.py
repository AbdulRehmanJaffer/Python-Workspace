import pygame

pygame.init()

screen = pygame.display.set_mode((400,500))
pygame.display.set_caption('Background Image')
background = pygame.image.load("images.jpg")

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(background, (0, 0))

    pygame.display.update()
screen.mainloop()

