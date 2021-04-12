import pygame 
import random
import time

pygame.init()

#screen
W  = 400
H = 600
DISPLAYSURF = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game")
BACKGROUND = pygame.image.load("AnimatedStreet.png")


#color
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

#FPS
FPS = 60
timer = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((self.image.pygame.get_size()))
        self.rect = self.surf.get_rect(center = (W //2 , H))
        self.speed = 300
        pixels_per_frame = self.speed // FPS
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        pixels_per_frame = self.speed // FPS
        if self.rect.top > 0:
         if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -pixels_per_frame)
        if self.rect.bottom < H:
         if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,pixels_per_frame)
         
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-pixels_per_frame, 0)
        if self.rect.right < W:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(pixels_per_frame, 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect) 

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.width, self.height = self.image.get_size()
        self.surf = pygame.Surface(self.image.get_size())
        
        center = (random.randint(self.width // 2, W - self.width // 2), -self.height // 2)
        self.rect = self.surf.get_rect(center = center)  

        self.speed = 600
        self.pixels_per_frame = self.speed // FPS  
 
    def move(self):
        self.rect.move_ip(0, self.pixels_per_frame)
        if self.rect.top > H:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 

player_1 = Player()
enemy_1 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(enemy_1)
all_sprites = pygame.sprite.Group()
all_sprites.add(player_1)
all_sprites.add(enemy_1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

Score = 0 
done = False
while not done:
    timer.tick(FPS)
    #pygame.mixer.Sound('background.wav').play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == INC_SPEED:
            for sprite in all_sprites:
              sprite.speed += 100
            
    player_1.move()
    enemy_1.move()
    
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(player_1, enemies):
      pygame.mixer.Sound('crash.wav').play()
      time.sleep(0.5)
      DISPLAYSURF.fill(RED)
      txt_rect = game_over.get_rect(center = (W // 2, H//2))
      DISPLAYSURF.blit(game_over, txt_rect)
      pygame.display.update()
      for entity in all_sprites:
            entity.kill() 
      time.sleep(2)
      done = True

    for sprite in all_sprites:
          sprite.move()
          sprite.draw(DISPLAYSURF)

    DISPLAYSURF.blit(BACKGROUND, (0, 0))
    


    
      
      
    
    player_1.draw(DISPLAYSURF)
    enemy_1.draw(DISPLAYSURF)
    pygame.display.update()
    
   
    pygame.display.flip()

pygame.quit()
