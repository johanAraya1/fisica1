import pygame
import pygame_gui
import math

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Constantes físicas
g = 9.81  # gravedad en m/s^2
e = 0.8   # coeficiente de restitución (rebote)
FPS = 60

def main():
    """Función principal para manejar la interfaz y simulación."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulación de Movimiento")
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))

    # Crear barra de controles en la parte superior
    speed_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 10), (150, 30)),
        text="Velocidad Inicial (m/s):",
        manager=manager
    )
    speed_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((170, 10), (100, 30)),
        manager=manager
    )
    speed_input.set_text("30")  # Valor predeterminado

    angle_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((280, 10), (150, 30)),
        text="Ángulo de lanzamiento (°):",
        manager=manager
    )
    angle_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((440, 10), (100, 30)),
        manager=manager
    )
    angle_input.set_text("45")  # Valor predeterminado

    launch_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((550, 10), (100, 30)),
        text="Lanzar",
        manager=manager
    )

    reset_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((660, 10), (100, 30)),
        text="Juego nuevo",
        manager=manager
    )

    clock = pygame.time.Clock()
    running = True
    simulating = False
    x, y = 40, 50 + 10  # Posición inicial de la pelota (esquina superior de la barra roja vertical)
    vx, vy = 0, 0  # Velocidades iniciales
    radius = 10  # Radio de la pelota

    while running:
        time_delta = clock.tick(FPS) / 1000.0
        screen.fill(WHITE)

        # Dibujar el área de simulación debajo de la barra de controles
        pygame.draw.rect(screen, RED, (0, HEIGHT - 20, WIDTH, 20))  # Suelo
        pygame.draw.rect(screen, RED, (20, 50, 20, HEIGHT - 50))  # Pared izquierda

        if simulating:
            # Mover la pelota con ecuaciones del movimiento
            x += vx * time_delta
            vy += g * time_delta
            y += vy * time_delta

            # Detectar colisión con el suelo
            if y + radius >= HEIGHT - 20:
                y = HEIGHT - 20 - radius
                vy = -e * vy

            # Detectar colisión con la pared
            if x - radius <= 40:
                x = 40 + radius
                vx = -e * vx

            # Dibujar la pelota
            pygame.draw.circle(screen, BLACK, (int(x), int(y)), radius)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == launch_button:
                    try:
                        angle = float(angle_input.get_text())
                        speed = float(speed_input.get_text())
                        angle = math.radians(angle)
                        vx = speed * math.cos(angle)
                        vy = -speed * math.sin(angle)
                        x, y = 40, 50 + radius  # Reiniciar posición inicial
                        simulating = True
                    except ValueError:
                        print("Por favor, ingrese valores válidos.")
                elif event.ui_element == reset_button:
                    # Reiniciar la simulación
                    x, y = 40, 50 + radius
                    vx, vy = 0, 0
                    simulating = False

            manager.process_events(event)

        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()