import pygame 

pygame.init()

window = pygame.display.set_mode((400, 400))
window.fill((255, 255, 255))  # Fill the window with white color   
GREEN = (0, 255, 0)
pygame.draw.circle(window, GREEN, (300, 300), 50)  # Draw a green circle at the center
pygame.draw.circle(window, GREEN, (100, 100), 30)  # Draw a smaller green circle at the top left corner
pygame.display.update()
running = true 
while running:
         
        for event  in pygame.event.get():
            if event.type == pygame.QUIT:
             running = False
pygame.quit()