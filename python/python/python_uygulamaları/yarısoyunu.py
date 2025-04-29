import pygame
import random
import sys

# Pygame'i başlat
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basit Yarış Oyunu")

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# FPS
clock = pygame.time.Clock()

# Oyuncu arabası
player_car = pygame.image.load("car.webp")
player_car = pygame.transform.scale(player_car, (50, 100))
player_x = WIDTH // 2
player_y = HEIGHT - 120
player_speed = 5

# Engel arabaları
enemy_car = pygame.image.load("car.webp")
enemy_car = pygame.transform.scale(enemy_car, (50, 100))
enemy_x = random.randint(0, WIDTH - 50)
enemy_y = -100
enemy_speed = 7

# Skor
score = 0

# Yazı tipi
font = pygame.font.SysFont(None, 48)
0,
def display_score(score):
    text = font.render(f"Skor: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Ana oyun döngüsü
running = True
while running:
    screen.fill(BLACK)

    # Olayları kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tuşları kontrol et
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed

    # Engel arabasını hareket ettir
    enemy_y += enemy_speed

    # Engel arabası ekranın dışına çıkarsa
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(0, WIDTH - 50)
        score += 1

    # Çarpışma kontrolü
    player_rect = pygame.Rect(player_x, player_y, 50, 100)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 100)
    if player_rect.colliderect(enemy_rect):
        print("Oyun Bitti!")
        print(f"Toplam Skor: {score}")
        pygame.quit()
        sys.exit()

    # Grafik öğelerini ekrana çiz
    screen.blit(player_car, (player_x, player_y))
    screen.blit(enemy_car, (enemy_x, enemy_y))
    display_score(score)

    # Ekranı güncelle
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
