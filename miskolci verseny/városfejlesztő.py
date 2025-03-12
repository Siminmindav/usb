import pygame
import random


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Álomváros')


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
BLUE = (100, 100, 255)
GREY = (169, 169, 169)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
LIGHT_BLUE = (173, 216, 230)


city_data = {
    'neighborhoods': {
        'center': {'population': 5000, 'buildings': 100, 'pollution': 10},
        'suburb': {'population': 2000, 'buildings': 50, 'pollution': 5},
    },
    'resources': {'money': 100000, 'materials': 5000},
    'happiness': 70,
    'pollution': 10,  
}


map_grid = [[0 for _ in range(10)] for _ in range(8)]  # 8x10-es térkép
building_types = ['Park', 'School', 'Hospital', 'Industrial', 'Residential']  # Épület típusok

# Ablak frissítése és rajzolás
def draw_city():
    screen.fill(WHITE)

    # Városépületek rajzolása
    for i in range(8):
        for j in range(10):
            x = j * 80
            y = i * 75
            building_type = map_grid[i][j]
            if building_type == 'Park':
                pygame.draw.rect(screen, GREEN, (x, y, 80, 75))  # Park
            elif building_type == 'School':
                pygame.draw.rect(screen, LIGHT_BLUE, (x, y, 80, 75))  # Iskola
            elif building_type == 'Hospital':
                pygame.draw.rect(screen, BLUE, (x, y, 80, 75))  # Kórház
            elif building_type == 'Industrial':
                pygame.draw.rect(screen, BROWN, (x, y, 80, 75))  # Ipari zóna
            elif building_type == 'Residential':
                pygame.draw.rect(screen, GREY, (x, y, 80, 75))  # Lakóépület
            else:
                pygame.draw.rect(screen, DARKGREEN, (x, y, 80, 75))  # Szabad terület

    # Információs sáv
    font = pygame.font.SysFont('Arial', 18)
    text = font.render(f'Money: ${city_data["resources"]["money"]}   Materials: {city_data["resources"]["materials"]}   Happiness: {city_data["happiness"]}   Pollution: {city_data["pollution"]}', True, BLUE)
    screen.blit(text, (10, HEIGHT - 40))
    
    # Kattintás jelzés
    text = font.render(f'Click to build a building! (1=Park, 2=School, 3=Hospital, 4=Industrial, 5=Residential)', True, RED)
    screen.blit(text, (10, HEIGHT - 80))
    
    pygame.display.flip()

# Épületépítés kezelése (kattintás)
def handle_click(x, y, building_type):
    grid_x = x // 80
    grid_y = y // 75
    if map_grid[grid_y][grid_x] == 0:  # Ha üres hely
        if city_data['resources']['materials'] >= 100:  # Ha van elég anyag
            map_grid[grid_y][grid_x] = building_type  # Épület építése
            city_data['resources']['materials'] -= 100  # Csökkentjük az anyagokat
            
            # Különböző épületek hatásai
            if building_type == 'Park':
                city_data['happiness'] += 5  # Park növeli az elégedettséget
            elif building_type == 'School':
                city_data['happiness'] += 10  # Iskola növeli az elégedettséget
                city_data['resources']['money'] += 100  # Iskola bevételt hoz
            elif building_type == 'Hospital':
                city_data['happiness'] += 8  # Kórház növeli az elégedettséget
                city_data['pollution'] -= 2  # Kórház csökkenti a szennyezést
            elif building_type == 'Industrial':
                city_data['resources']['money'] += 200  # Ipari zóna pénzt hoz
                city_data['pollution'] += 5  # Ipari zóna szennyezést generál
            elif building_type == 'Residential':
                city_data['happiness'] += 3  # Lakóépületek növelik az elégedettséget
                city_data['neighborhoods']['center']['population'] += 50  # Lakóépület növeli a lakosságot

# Fő program ciklus
running = True
selected_building = 'Park'  # Alapértelmezett épület

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Ha bal egérgombbal kattintunk
                mouse_x, mouse_y = pygame.mouse.get_pos()
                handle_click(mouse_x, mouse_y, selected_building)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selected_building = 'Park'
            elif event.key == pygame.K_2:
                selected_building = 'School'
            elif event.key == pygame.K_3:
                selected_building = 'Hospital'
            elif event.key == pygame.K_4:
                selected_building = 'Industrial'
            elif event.key == pygame.K_5:
                selected_building = 'Residential'

    # Város rajzolása
    draw_city()

pygame.quit()
