import pygame 

pygame.init()

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.display.set_caption("Paint")
font = pygame.font.SysFont("VERDANA", 15)
change = font.render("To change brush press '1'", True, BLACK)
color = font.render("To change color press '2'", True, BLACK)
save = font.render("To save your image press SPACE", True, BLACK)


WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

isPressed = False
prevPoint = (0, 0)
curPoint = (0, 0)

def drawRectangle(surface, color, x, y, w, h):
    pygame.draw.rect(surface, color, [x, y, w, h], 5)

def drawCircle(surface, color, x, y):
    pygame.draw.circle(surface, color, (x, y), 30, 3)

def drawLine(surface, color, startPos, endPos):
    pygame.draw.line(surface, color, startPos, endPos, 2)

def erase(surface, x, y):
    pygame.draw.circle(surface, WHITE, (x, y), 40)


currentTool = 0
toolCount = 4

current_color = 0
colors = (BLUE, GREEN, RED)


done = False
while not done:
    for event in pygame.event.get():
        
        txt_rect = change.get_rect(center=(WIDTH // 10, HEIGHT // 20))
        screen.blit(change, txt_rect)
        
        txt_rect = color.get_rect(center=(WIDTH // 10, HEIGHT // 10))
        screen.blit(color, txt_rect)

        txt_rect = color.get_rect(center=(WIDTH // 10, HEIGHT/6.8))
        screen.blit(save, txt_rect)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                currentTool = (currentTool + 1) % toolCount
            elif event.key == pygame.K_2:
                current_color = (current_color + 1) % len(colors)
            elif event.key == pygame.K_SPACE:
                pygame.image.save(screen, 'screenshot.jpg')
        if event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True
            prevPoint = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
        elif event.type == pygame.MOUSEMOTION and isPressed == True:
            prevPoint = curPoint
            curPoint = pygame.mouse.get_pos()
        elif event.type == pygame.QUIT:
            done = True
      
            
    if currentTool == 0:
        drawLine(screen, colors[current_color], prevPoint, curPoint)
    elif currentTool == 1:
        drawRectangle(screen, colors[current_color], curPoint[0], curPoint[1], 100, 100)
    elif currentTool == 2:
        drawCircle(screen, colors[current_color], *curPoint)
    elif currentTool == 3:
        erase(screen, *curPoint)

    pygame.display.flip()