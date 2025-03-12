import pygame
import random
import time

# Pygame inicializálása
pygame.init()

# Ablak beállítások
WIDTH, HEIGHT = 1000, 600  # Kibővített ablak
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Álomváros - Városszimuláció')

# Színek
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (100, 100, 255)
GREY = (169, 169, 169)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
LIGHT_BLUE = (173, 216, 230)
ORANGE = (255, 165, 0)
DARK_GREEN = (34, 139, 34)
BLACK = (0, 0, 0)

# Alap adatok
city_data = {
    'population': 5000,
    'money': 100000,
    'materials': 5000,
    'happiness': 70,
    'pollution': 10,
    'tax_rate': 5,
    'events': []
}

# Épület típusok és hatásaik
building_types = {
    'Park': {'color': GREEN, 'happiness': 5, 'pollution': -2},
    'School': {'color': LIGHT_BLUE, 'happiness': 10, 'money': 100},
    'Hospital': {'color': BLUE, 'happiness': 8, 'pollution': -3},
    'Industrial': {'color': BROWN, 'money': 200, 'pollution': 5},
    'Residential': {'color': GREY, 'population': 50, 'happiness': 3},
    'Fire Station': {'color': RED, 'safety': 5},
    'Police Station': {'color': DARK_GREEN, 'safety': 5},
    'Mall': {'color': ORANGE, 'happiness': 7, 'money': 150}
}

# Térkép (8x10-es rács)
map_grid = [[None for _ in range(12)] for _ in range(8)]
show_building_info = False

def draw_city():
    screen.fill(WHITE)
    for i in range(8):
        for j in range(12):
            x, y = j * 80, i * 75
            building = map_grid[i][j]
            color = building_types.get(building, {}).get('color', WHITE)
            pygame.draw.rect(screen, color, (x, y, 80, 75))
    
    font = pygame.font.SysFont('Arial', 18)
    stats_text = f'Lakosság: {city_data["population"]}  Pénz: ${city_data["money"]}  Boldogság: {city_data["happiness"]}%'
    text = font.render(stats_text, True, BLUE)
    screen.blit(text, (10, HEIGHT - 40))
    
    instruction_text = [
        "Irányítás:",
        "1-8: Épület kiválasztása",
        "Bal klikk: Épület lerakása",
        "I: Épület adatok ki/be",
        "Q: Kilépés"
    ]
    for i, line in enumerate(instruction_text):
        text = font.render(line, True, BLACK)
        screen.blit(text, (10, 50 + i * 25))
    
    if show_building_info:
        info_y = 200
        for building, stats in building_types.items():
            info_text = f"{building}: {', '.join(f'{k}: {v}' for k, v in stats.items() if k != 'color')}"
            text = font.render(info_text, True, BLACK)
            screen.blit(text, (10, info_y))
            info_y += 20
    
    pygame.display.flip()


def handle_click(x, y, building_type):
    grid_x, grid_y = x // 80, y // 75
    if grid_x < 12 and map_grid[grid_y][grid_x] is None:
        if city_data['materials'] >= 100:
            map_grid[grid_y][grid_x] = building_type
            city_data['materials'] -= 100
            for key, value in building_types[building_type].items():
                if isinstance(value, (int, float)):
                    city_data[key] = city_data.get(key, 0) + value

def update_city():
    city_data['money'] += city_data['population'] * (city_data['tax_rate'] / 100)
    if random.randint(1, 20) == 1:
        event = random.choice(['Járvány!', 'Tűzvész!', 'Gazdasági fellendülés!'])
        city_data['events'].append(event)
        if event == 'Járvány!':
            city_data['population'] -= 500
        elif event == 'Tűzvész!':
            city_data['money'] -= 5000
        elif event == 'Gazdasági fellendülés!':
            city_data['money'] += 10000

running = True
selected_building = 'Park'
last_update = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                handle_click(*pygame.mouse.get_pos(), selected_building)
        elif event.type == pygame.KEYDOWN:
            keys = ['Park', 'School', 'Hospital', 'Industrial', 'Residential', 'Fire Station', 'Police Station', 'Mall']
            if pygame.K_1 <= event.key <= pygame.K_8:
                selected_building = keys[event.key - pygame.K_1]
            elif event.key == pygame.K_i:
                show_building_info = not show_building_info
    
    if time.time() - last_update > 5:
        update_city()
        last_update = time.time()
    
    draw_city()

pygame.quit()
