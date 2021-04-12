import pygame 
import random


pygame.init()

#screen
W  = 400
H = 600
DISPLAYSURF = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game")
BACKGROUND = pygame.image.load("AnimatedStreet1.png")


#color
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GOLD = (255,215,0)


font = pygame.font.SysFont("VERDANA", 60)
font_small = pygame.font.SysFont("VERDANA", 20)
game_over = font.render("Game Over", True, WHITE)

#FPS
FPS = 60
timer = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("player1.png")
        self.surf = pygame.Surface(self.image.get_size())
        
        center = (W // 2, H - self.image.get_height() // 2)
        self.rect = self.surf.get_rect(center=center)
        
        self.speed = 450
        
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        pixels_per_frame = self.speed // FPS
        
        '''
        if self.rect.top > 0:
         if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -pixels_per_frame)
        if self.rect.bottom < H:
         if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,pixels_per_frame)
        ''' 
        
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
        self.image = pygame.image.load("enemy1.png")
        self.width, self.height = self.image.get_size()
        self.surf = pygame.Surface(self.image.get_size())
        
        center = (random.randint(self.width // 2, W - self.width // 2), -self.height // 2)
        self.rect = self.surf.get_rect(center = center)  

        self.speed = 600
        
 
    def move(self):
        global score
        pixels_per_frame = self.speed // FPS  
        self.rect.move_ip(0, pixels_per_frame)
        if self.rect.top > H:
            score += 1
            self.speed = random.randint(200,700)
            center = (random.randint(self.width // 2, W - self.width // 2), 
                    -self.height // 2)
            self.rect.center = center
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.width, self.height = self.image.get_size()
        self.surf = pygame.Surface(self.image.get_size())
        
        center = (random.randint(self.width // 2, W - self.width // 2), -self.height // 2)
        self.rect = self.surf.get_rect(center = center)  

        self.speed = 600
        
 
    def move(self):
        global score2
        pixels_per_frame = self.speed // FPS  
        self.rect.move_ip(0, pixels_per_frame)
        if self.rect.top > H:
            self.rect.top = 0
            
            center = (random.randint(self.width // 2, W - self.width // 2), 
                    -self.height // 2)
            self.rect.center = center
        if pygame.sprite.spritecollideany(player1,coins):
            score2 += 1 
            
            self.speed = random.randint(100,800)
            self.rect.top = 0 
            center = (random.randint(self.width // 2, W - self.width // 2), 
                    -self.height // 2)
            self.rect.center = center
            pygame.display.flip()
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 


'''
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

'''
game_done = False
while not game_done:

    enemy1 = Enemy()
    player1 = Player()
    coins1 = Coins()

    #Creating Sprites Groups
    enemies = pygame.sprite.Group()
    enemies.add(enemy1)
    coins = pygame.sprite.Group()
    coins.add(coins1)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1)
    all_sprites.add(enemy1)
    all_sprites.add(coins1)
    


    score = 0
    score2 = 0
    done = False
    while not done:
        timer.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                game_done = True
            # if event.type == INC_SPEED:
            #     for sprite in all_sprites:
            #         sprite.speed += 100
        
       
            
            
        

        if pygame.sprite.spritecollideany(player1, enemies):
            pygame.mixer.Sound('crash.wav').play()
            DISPLAYSURF.fill(BLACK)
            txt_rect = game_over.get_rect(center=(W // 2, H // 2))
            DISPLAYSURF.blit(game_over, txt_rect)
            pygame.display.flip()
            for sprite in all_sprites:
                sprite.kill()
            choosen = False
            while not choosen:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_done = True
                        choosen = True
                    if event.type == pygame.KEYDOWN:
                        choosen = True
                        if event.key == pygame.K_SPACE:
                            game_done = True
            done = True

        DISPLAYSURF.blit(BACKGROUND, (0, 0))

        scores = font_small.render(str(score), True, WHITE)
        DISPLAYSURF.blit(scores, (10, 10))
        
        scores2 = font_small.render(str(score2), True, GOLD)
        DISPLAYSURF.blit(scores2, (370, 10))

        for sprite in all_sprites:
            sprite.move()
            sprite.draw(DISPLAYSURF)

        pygame.display.flip()



pygame.quit()
