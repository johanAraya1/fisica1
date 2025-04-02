import pygame
import sys
import time

# Inicializar pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 700  # Aumentamos la altura para incluir el área de datos
GAME_HEIGHT = 600  # Altura del área de juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game Mejorado")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Configuración de la paleta
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
paddle_speed = 8

# Configuración de la pelota
BALL_RADIUS = 8
initial_ball_speed_x = 4
initial_ball_speed_y = -4

# Configuración de los bloques
BLOCK_ROWS = 5
BLOCK_COLUMNS = 10
BLOCK_WIDTH = WIDTH // BLOCK_COLUMNS
BLOCK_HEIGHT = 20

# Fuente
font = pygame.font.Font(None, 36)

def reset_game():
    global paddle_x, paddle_y, ball_x, ball_y, ball_speed_x, ball_speed_y, blocks, score, start_time, running, game_over
    paddle_x = (WIDTH - PADDLE_WIDTH) // 2
    paddle_y = GAME_HEIGHT - 30
    ball_x = WIDTH // 2
    ball_y = GAME_HEIGHT // 2
    ball_speed_x = initial_ball_speed_x
    ball_speed_y = initial_ball_speed_y
    blocks = [pygame.Rect(col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
              for row in range(BLOCK_ROWS) for col in range(BLOCK_COLUMNS)]
    score = 0
    start_time = time.time()
    running = True
    game_over = False

reset_game()

# Bucle del juego
while True:
    screen.fill(BLACK)
    
    if not game_over:
        # Dibujar área de datos
        pygame.draw.rect(screen, GRAY, (0, GAME_HEIGHT, WIDTH, HEIGHT - GAME_HEIGHT))
        
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Movimiento de la paleta
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
            paddle_x += paddle_speed
        
        # Movimiento de la pelota
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        
        # Colisión con las paredes
        if ball_x <= 0 or ball_x >= WIDTH - BALL_RADIUS:
            ball_speed_x *= -1
        if ball_y <= 0:
            ball_speed_y *= -1
        
        # Colisión con la paleta
        paddle_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        if paddle_rect.colliderect(pygame.Rect(ball_x, ball_y, BALL_RADIUS, BALL_RADIUS)):
            ball_speed_y *= -1
        
        # Colisión con los bloques
        for block in blocks[:]:
            if pygame.Rect(ball_x, ball_y, BALL_RADIUS, BALL_RADIUS).colliderect(block):
                blocks.remove(block)
                ball_speed_y *= -1
                score += 10
                # Incrementar velocidad cada 50 puntos
                if score % 50 == 0:
                    ball_speed_x += 2 if ball_speed_x > 0 else -2
                    ball_speed_y += 2 if ball_speed_y > 0 else -2
        
        # Game over si la pelota cae
        if ball_y >= GAME_HEIGHT:
            game_over = True
        
        # Dibujar bloques
        for block in blocks:
            pygame.draw.rect(screen, RED, block)
            pygame.draw.rect(screen, GRAY, block, 2)  # Bordes de los bloques
        
        # Dibujar paleta y pelota
        pygame.draw.rect(screen, BLUE, paddle_rect)
        pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
        
        # Calcular velocidad de la pelota
        speed = (ball_speed_x**2 + ball_speed_y**2)**0.5
        
        # Calcular tiempo transcurrido
        elapsed_time = time.time() - start_time
        
        # Mostrar datos en tres columnas
        score_text = font.render(f"Puntaje: {score}", True, BLACK)
        speed_text = font.render(f"Velocidad: {speed:.2f}", True, BLACK)
        time_text = font.render(f"Tiempo: {elapsed_time:.1f} s", True, BLACK)
        screen.blit(score_text, (10, GAME_HEIGHT + 10))
        screen.blit(speed_text, (WIDTH // 3, GAME_HEIGHT + 10))
        screen.blit(time_text, (2 * WIDTH // 3, GAME_HEIGHT + 10))
    else:
        # Pantalla de "Perdiste"
        game_over_text = font.render("¡Perdiste!", True, WHITE)
        play_again_text = font.render("Jugar de nuevo", True, GREEN)
        quit_text = font.render("Salir", True, RED)
        
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
        play_again_rect = screen.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT // 2))
        quit_rect = screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 50))
        
        # Manejo de eventos en la pantalla de "Perdiste"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(event.pos):
                    reset_game()
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
    
    # Actualizar pantalla
    pygame.display.flip()
    pygame.time.delay(16)  # Aproximadamente 60 FPS