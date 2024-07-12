import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WITHIN THE BOUNDARIES")
clock = pygame.time.Clock()

bird_image = pygame.image.load('bird.png').convert_alpha()
bird_image = pygame.transform.scale(bird_image, (60, 60))
game_over_image = pygame.image.load('gm.jpg').convert_alpha()
game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))

player = {
    'image': bird_image,
    'rect': bird_image.get_rect(center=(WIDTH // 2, HEIGHT // 2)),
    'velocity': pygame.math.Vector2(0, 0),
    'game_over': False
}

def handle_input(player, dt):
    keys = pygame.key.get_pressed()
    player['velocity'].x = 0
    if keys[pygame.K_LEFT]:
        player['velocity'].x = -200 * dt
    if keys[pygame.K_RIGHT]:
        player['velocity'].x = 200 * dt
    if keys[pygame.K_UP]:
        player['velocity'].y = -300 * dt

def update_player(player, dt):
    if player['game_over']:
        return

    handle_input(player, dt)
    player['velocity'].y += 20 * dt  
    player['rect'].x += player['velocity'].x
    player['rect'].y += player['velocity'].y

    if (player['rect'].bottom > HEIGHT or player['rect'].top < 0 or
        player['rect'].right > WIDTH or player['rect'].left < 0):
        player['game_over'] = True

def draw_player(screen, player):
    screen.blit(player['image'], player['rect'])

def display_game_over(screen):
    screen.blit(game_over_image, (0, 0))
    pygame.display.flip()

def main():
    last_time = pygame.time.get_ticks()

    while True:
        current_time = pygame.time.get_ticks()
        dt = (current_time - last_time) / 1000.0  
        last_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if player['game_over']:
            display_game_over(screen)
            continue

        update_player(player, dt)
        screen.fill((0, 0, 0))  
        draw_player(screen, player)
        pygame.display.flip() 

        clock.tick(60)  

if __name__=="__main__":
    main()
