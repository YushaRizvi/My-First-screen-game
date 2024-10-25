import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game screen")
penguin_image = pygame.transform.scale(pygame.image.load("penguins.jpeg"),(200,200))

penguin_position = penguin_image.get_rect(center=(300,300))

screen.fill("grey")

while True:
    for event in pygame.event.get():

        if event.type==pygame.QUIT:

            pygame.quit()

    screen.blit(penguin_image,penguin_position)

    pygame.display.flip()
    
