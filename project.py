import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("within the boundaries")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('bird.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.velocity = pygame.math.Vector2(0, 0)
        self.game_over = False

    def update(self, dt):
        if self.game_over:
            return

        self.velocity.x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -200 * dt 
        if keys[pygame.K_RIGHT]:
            self.velocity.x = 200 * dt  
        if keys[pygame.K_UP]:
            self.velocity.y = -500 * dt  

        self.velocity.y += 20 * dt  
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        if self.rect.bottom > HEIGHT:
            self.game_over = True
        if self.rect.top < 0:
            self.game_over = True
        if self.rect.right > WIDTH:
            self.game_over = True
        if self.rect.left < 0:
            self.game_over = True

def display_game_over(screen):
    gm = pygame.image.load('gm.jpg').convert_alpha()
    gm = pygame.transform.scale(gm, (WIDTH, HEIGHT))
    screen.blit(gm, (0, 0))
    pygame.display.flip()

player = Player()
sprites = pygame.sprite.Group()
sprites.add(player)
running = True
last_time = pygame.time.get_ticks()

while running:
    current_time = pygame.time.get_ticks()
    dt = (current_time - last_time) / 1000.0  
    last_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if player.game_over:
        display_game_over(screen)
        continue

    sprites.update(dt)
    screen.fill((0, 0, 0))
    sprites.draw(screen)
    pygame.display.flip()

    clock.tick(120)

pygame.quit()

