import pygame
import math
pygame.init()

W = 800
H = 600

screen = pygame.display.set_mode((W,H))

def draw_star(n, radius, color, center):
    n *= 2
    points = []
    for i in range(n):
        phi = 2 * math.pi / n * i
       
        r = radius if i % 2 == 0 else radius / 2 
        
        x = r * math.sin(phi) + center[0]
        y = -r * math.cos(phi) + center[1]
        points.append((x, y))
    
    pygame.draw.polygon(screen, color, points)



        
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    
    screen.fill((255,255,255))
    
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 10, 100, 100))
    pygame.draw.circle(screen, (255, 0, 0), (300, 60), 50, 50)
    draw_star(5, 50, (255 ,255, 0), (300, 300))
 
    pygame.display.flip()
