import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer")
clock = pygame.time.Clock()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('bird.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):
        self.velocity.x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -5
        if keys[pygame.K_RIGHT]:
            self.velocity.x = 5
        if keys[pygame.K_UP]:
            self.velocity.y = -10

        self.velocity.y += 0.5  # gravity
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        if self.rect.bottom > HEIGHT:
        
            self.rect.bottom = HEIGHT
            self.velocity.y = 0
            



player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()




