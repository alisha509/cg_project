import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FLAPPY BIRD")
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

obstacle_width = 70
obstacle_color = (255, 0, 0)
obstacle_speed = 150

obstacles = []

def create_obstacle():
    height = random.randint(100, 300)
    top_rect = pygame.Rect(WIDTH, 0, obstacle_width, height)
    bottom_rect = pygame.Rect(WIDTH, height + 200, obstacle_width, HEIGHT - height - 200)
    return [top_rect, bottom_rect]

def move_obstacles(obstacles, dt):
    for rects in obstacles:
        rects[0].x -= obstacle_speed * dt
        rects[1].x -= obstacle_speed * dt

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
    
    for rects in obstacles:
        if player['rect'].colliderect(rects[0]) or player['rect'].colliderect(rects[1]):
            player['game_over'] = True

def draw_player(screen, player):
    screen.blit(player['image'], player['rect'])

def display_game_over(screen):
    screen.blit(game_over_image, (0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Press space to Restart", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - 175, HEIGHT // 2 + 200))
    pygame.display.flip()

def reset_game(player):
    player['rect'].center = (WIDTH // 2, HEIGHT // 2)
    player['velocity'] = pygame.math.Vector2(0, 0)
    player['game_over'] = False
    obstacles.clear()

def draw_obstacles(screen, obstacles):
    for rects in obstacles:
        pygame.draw.rect(screen, obstacle_color, rects[0])
        pygame.draw.rect(screen, obstacle_color, rects[1])

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
            if event.type == pygame.KEYDOWN and player['game_over']:
                if event.key == pygame.K_SPACE:
                    reset_game(player)

        if player['game_over']:
            display_game_over(screen)
            continue

        # Add new obstacles at intervals
        if len(obstacles) == 0 or obstacles[-1][0].x < WIDTH - 300:
            obstacles.append(create_obstacle())

        # Remove obstacles that are off the screen
        if obstacles and obstacles[0][0].x < -obstacle_width:
            obstacles.pop(0)

        move_obstacles(obstacles, dt)
        update_player(player, dt)
        screen.fill((0, 0, 0))  
        draw_player(screen, player)
        draw_obstacles(screen, obstacles)
        pygame.display.flip() 

        clock.tick(60)  

if __name__ == "__main__":
    main()
