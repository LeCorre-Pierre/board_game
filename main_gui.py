import sys
import json
import pygame
import os

# Palette moderne
TILE_COLORS = {
    "Planches": (222, 184, 135),   # Beige bois
    "Cailloux": (120, 120, 120),  # Gris pierre
    "Lac": (66, 170, 255),        # Bleu vif
    "portal": (255, 215, 0),      # Jaune portail
    "start": (76, 175, 80),       # Vert accent
    "center": (245, 245, 245),    # Blanc cassé
}

TILE_TYPES = ["Planches", "Cailloux", "Lac"]
TILE_ROLES = ["center", "top", "left", "right", "start", "portal"]
TILE_SIZE = 120
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 1000  # Agrandit la fenêtre

class CubeNexusEditor:
    def __init__(self):
        self.keeper_name = ""
        self.selected_tile = None
        self.tile_types = {
            "center": "Cailloux",
            "top": "Terre",
            "left": "Lac",
            "right": "Lac",
            "start": "Planches",
            "portal": "portal"
        }
        self.font = None
        self.title_font = None
        self.button_font = None
        self.bg_color = (245, 248, 255)
        self.shadow_color = (200, 210, 230)
        self.button_color = (66, 133, 244)
        self.button_hover = (36, 103, 214)
        self.button_text = (255, 255, 255)
        self.input_bg = (255, 255, 255)
        self.input_border = (66, 133, 244)
        self.input_active = (36, 103, 214)

    def draw_tiles(self, screen):
        cx, cy = SCREEN_WIDTH // 2, 300
        positions = {
            "center": (cx, cy),
            "top": (cx, cy - TILE_SIZE),
            "left": (cx - TILE_SIZE, cy),
            "right": (cx + TILE_SIZE, cy),
            "start": (cx, cy + TILE_SIZE),
            "portal": (cx, cy + 2 * TILE_SIZE)
        }
        for role, (x, y) in positions.items():
            color = TILE_COLORS.get(self.tile_types.get(role, "Cailloux"), (200, 200, 200))
            rect = pygame.Rect(x - TILE_SIZE//2, y - TILE_SIZE//2, TILE_SIZE, TILE_SIZE)
            # Ombre
            shadow = rect.move(6, 6)
            pygame.draw.rect(screen, self.shadow_color, shadow, border_radius=18)
            # Tuile
            pygame.draw.rect(screen, color, rect, border_radius=18)
            pygame.draw.rect(screen, (0,0,0), rect, 2, border_radius=18)
            # Label
            label = self.font.render(role, True, (40,40,40))
            screen.blit(label, (x - label.get_width()//2, y - label.get_height()//2))
            # Highlight selection
            if self.selected_tile == role:
                pygame.draw.rect(screen, (255,87,34), rect, 5, border_radius=18)

    def get_tile_at_pos(self, pos):
        cx, cy = SCREEN_WIDTH // 2, 300
        positions = {
            "center": (cx, cy),
            "top": (cx, cy - TILE_SIZE),
            "left": (cx - TILE_SIZE, cy),
            "right": (cx + TILE_SIZE, cy),
            "start": (cx, cy + TILE_SIZE),
            "portal": (cx, cy + 2 * TILE_SIZE)
        }
        for role, (x, y) in positions.items():
            rect = pygame.Rect(x - TILE_SIZE//2, y - TILE_SIZE//2, TILE_SIZE, TILE_SIZE)
            if rect.collidepoint(pos):
                return role
        return None

    def draw_button(self, screen, rect, text, hover):
        color = self.button_hover if hover else self.button_color
        pygame.draw.rect(screen, color, rect, border_radius=12)
        label = self.button_font.render(text, True, self.button_text)
        screen.blit(label, (rect.x + (rect.w-label.get_width())//2, rect.y + (rect.h-label.get_height())//2))

    def save(self):
        data_dir = os.path.join(os.path.dirname(__file__), "data")
        os.makedirs(data_dir, exist_ok=True)
        if self.keeper_name:
            file_path = os.path.join(data_dir, f"{self.keeper_name}_cube.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(self.tile_types, f, ensure_ascii=False, indent=2)
            # Affiche une confirmation visuelle
            self.save_message = f"Cube sauvegardé sous data/{self.keeper_name}_cube.json !"
        else:
            self.save_message = "Veuillez saisir un nom de Keeper avant de sauvegarder."

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Cube Nexus Customizer")
        self.font = pygame.font.SysFont("Segoe UI", 28, bold=True)
        self.title_font = pygame.font.SysFont("Segoe UI", 44, bold=True)
        self.button_font = pygame.font.SysFont("Segoe UI", 32, bold=True)
        input_box = pygame.Rect(120, 60, 360, 50)
        color_inactive = self.input_border
        color_active = self.input_active
        color = color_inactive
        active = False
        text = ''
        clock = pygame.time.Clock()
        running = True
        save_rect = pygame.Rect(200, 620, 200, 50)
        save_hover = False
        json_box = pygame.Rect(40, 870, 520, 100)
        self.save_message = ""
        while running:
            mouse_pos = pygame.mouse.get_pos()
            save_hover = save_rect.collidepoint(mouse_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                        role = self.get_tile_at_pos(event.pos)
                        if role and role != "portal":
                            self.selected_tile = role
                    if save_rect.collidepoint(event.pos):
                        self.save()
                elif event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            self.keeper_name = text
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                    elif self.selected_tile and event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                        self.tile_types[self.selected_tile] = TILE_TYPES[event.key - pygame.K_1]
            screen.fill(self.bg_color)
            # Titre
            title = self.title_font.render("Cube Nexus Customizer", True, (36, 103, 214))
            screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 10))
            # Input box
            pygame.draw.rect(screen, self.input_bg, input_box, border_radius=10)
            pygame.draw.rect(screen, color_active if active else color_inactive, input_box, 3, border_radius=10)
            txt_surface = self.font.render(text or self.keeper_name or "Nom du Keeper", True, (40,40,40))
            screen.blit(txt_surface, (input_box.x+10, input_box.y+10))
            # Tuiles
            self.draw_tiles(screen)
            # Légende moderne
            legend_y = 500
            for i, ttype in enumerate(TILE_TYPES):
                color = TILE_COLORS[ttype]
                rect = pygame.Rect(60 + i*170, legend_y, 40, 40)
                pygame.draw.rect(screen, color, rect, border_radius=8)
                pygame.draw.rect(screen, (0,0,0), rect, 2, border_radius=8)
                label = self.font.render(f"{i+1}: {ttype}", True, (40,40,40))
                screen.blit(label, (110 + i*170, legend_y+5))
            # Bouton sauvegarde
            self.draw_button(screen, save_rect, "Sauvegarder", save_hover)
            # Instructions modernes
            instructions = [
                "Cliquez sur une tuile puis appuyez sur 1, 2 ou 3 pour changer le type.",
                "Saisissez le nom du Keeper et appuyez sur Entrée.",
                "Cliquez sur 'Sauvegarder' pour enregistrer la configuration."
            ]
            for i, line in enumerate(instructions):
                label = self.font.render(line, True, (100,100,120))
                screen.blit(label, (40, 800 + i*28))
            # Message de sauvegarde
            if self.save_message:
                msg = self.font.render(self.save_message, True, (36, 103, 214))
                screen.blit(msg, (SCREEN_WIDTH//2 - msg.get_width()//2, 880))
            # Affichage du JSON
            pygame.draw.rect(screen, (255,255,255), json_box, border_radius=10)
            pygame.draw.rect(screen, (66, 133, 244), json_box, 2, border_radius=10)
            json_str = json.dumps(self.tile_types, ensure_ascii=False, indent=2)
            lines = json_str.split('\n')
            for i, line in enumerate(lines):
                label = self.font.render(line, True, (40,40,40))
                screen.blit(label, (json_box.x+10, json_box.y+10 + i*28))
            pygame.display.flip()
            clock.tick(30)
        pygame.quit()

if __name__ == "__main__":
    editor = CubeNexusEditor()
    editor.run()
