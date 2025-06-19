# Lancement du jeu en mode PyGame (graphique)
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Nexus Keepers - PyGame")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((30, 30, 30))
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
