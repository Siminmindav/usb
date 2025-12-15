import pygame
from math import sin, cos, radians

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

class cube:
    def __init__(self, points, edges, camera_pos=(400, 300, 700), color=(255, 255, 255)):
        self.color = color
        self.camera_pos = camera_pos
        self.points = points
        self.edges = edges
        self.angle_x = 0
        self.angle_y = 0
    
    def rotate(self, anglex, angley):
        self.angle_x += anglex
        self.angle_y += angley
        rotated_points = []
        for x, y, z in self.points:
            # Rotate around X axis
            y_rot = y * cos(self.angle_x) - z * sin(self.angle_x)
            z_rot = y * sin(self.angle_x) + z * cos(self.angle_x)
            # Rotate around Y axis
            x_rot = x * cos(self.angle_y) + z_rot * sin(self.angle_y)
            z_final = -x * sin(self.angle_y) + z_rot * cos(self.angle_y)
            rotated_points.append((x_rot, y_rot, z_final))
        self.rotated_points = rotated_points

    def draw(self, surface):
        for edge in self.edges:
            points = []
            for vertex in edge:
                x, y, z = self.rotated_points[vertex]
                # Simple perspective projection
                f = 200 / (z + self.camera_pos[2] + 0.1)
                x_proj = int(x * f) + self.camera_pos[0] 
                y_proj = int(y * f) + self.camera_pos[1] 
                points.append((x_proj, y_proj))
            if z + self.camera_pos[2] > 0:
                pygame.draw.line(surface, self.color, points[0], points[1], 1)

cube_points = [
    (-100, -100, -100), (100, -100, -100),
    (100, 100, -100), (-100, 100, -100),
    (-100, -100, 100), (100, -100, 100),
    (100, 100, 100), (-100, 100, 100)
]
cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
]
plane_points = [
    (-500, 100, -200), (200, 100, -200),
    (200, 100, 200), (-500, 100, 200)
]
plane_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (0, 2), (1, 3)
]
skybox_points = [
    (-800, -600, -800), (800, -600, -800),
    (800, 600, -800), (-800, 600, -800),
    (-800, -600, 800), (800, -600, 800),
    (800, 600, 800), (-800, 600, 800)
]
skybox_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
]
lines = [
    (-1100, 300, 0), (500, 300, 0),
    (-300, -500, 0), (-300, 1100, 0),
    (-300, 300, -800), (-300, 300, 800)
]
line_edges = [
    (0, 1), (2, 3), (4, 5)
]


teapot_points = [
    # Body bottom
    (-60, 40, -60), (60, 40, -60),
    (60, 40, 60), (-60, 40, 60),

    # Body top
    (-50, -40, -50), (50, -40, -50),
    (50, -40, 50), (-50, -40, 50),

    # Lid
    (-30, -55, -30), (30, -55, -30),
    (30, -55, 30), (-30, -55, 30),
    (0, -75, 0),   # lid knob

    # Spout
    (60, -10, -15), (85, 0, 0), (60, 10, 15),

    # Handle
    (-60, -15, -15), (-85, -25, 0), (-60, 5, 15)
]
teapot_edges = [
    # Body bottom
    (0, 1), (1, 2), (2, 3), (3, 0),

    # Body top
    (4, 5), (5, 6), (6, 7), (7, 4),

    # Body sides
    (0, 4), (1, 5), (2, 6), (3, 7),

    # Lid
    (8, 9), (9, 10), (10, 11), (11, 8),
    (8, 12), (9, 12), (10, 12), (11, 12),

    # Lid to body
    (4, 8), (5, 9), (6, 10), (7, 11),

    # Spout
    (1, 13), (13, 14), (14, 15), (15, 2),

    # Handle
    (0, 16), (16, 17), (17, 18), (18, 3)
]

#offset teapot position
teapot_points = [(x - 400, y + 50 , z) for x, y, z in teapot_points]

plane_obj = cube(plane_points, plane_edges)
plane_obj.color = (0, 255, 0)
cube_obj = cube(cube_points, cube_edges)
cube_obj.color = (255, 0, 0)
tea_obj = cube(teapot_points, teapot_edges)
tea_obj.color = (255, 255, 0)
skyblox_obj = cube(skybox_points, skybox_edges)
skyblox_obj.color = (0, 0, 255)
lines_obj = cube(lines, line_edges)
lines_obj.color = (255, 255, 255)

objects = [plane_obj, cube_obj, tea_obj, skyblox_obj, lines_obj]
for obj in objects:
    obj.rotate(0, 0)  # Initialize rotated points

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                for obj in objects:
                    if object == skyblox_obj or object == lines_obj:
                        continue
                    obj.rotate(0.1,0)
            if event.key == pygame.K_DOWN:
                for obj in objects:
                    if object == skyblox_obj or object == lines_obj:
                        continue
                    obj.rotate(-0.1,0)
            if event.key == pygame.K_RIGHT:
                for obj in objects:
                    if object == skyblox_obj or object == lines_obj:
                        continue
                    obj.rotate(0,0.1)
            if event.key == pygame.K_LEFT:
                for obj in objects:
                    if object == skyblox_obj or object == lines_obj:
                        continue
                    obj.rotate(0,-0.1)

            if event.key == pygame.K_w:
                for obj in objects:
                    obj.camera_pos = (obj.camera_pos[0], obj.camera_pos[1], obj.camera_pos[2] - 20)
            if event.key == pygame.K_s:
                for obj in objects:
                    obj.camera_pos = (obj.camera_pos[0], obj.camera_pos[1], obj.camera_pos[2] + 20)
            if event.key == pygame.K_a:
                for obj in objects:
                    obj.camera_pos = (obj.camera_pos[0] - 20, obj.camera_pos[1], obj.camera_pos[2])
            if event.key == pygame.K_d:
                for obj in objects:
                    obj.camera_pos = (obj.camera_pos[0] + 20, obj.camera_pos[1], obj.camera_pos[2])
            if event.key == pygame.K_q:
                for obj in objects:
                    obj.camera_pos = (obj.camera_pos[0], obj.camera_pos[1] - 20, obj.camera_pos[2])
            if event.key == pygame.K_e:
                for obj in objects:
                    obj.camera_pos = (obj.camera_pos[0], obj.camera_pos[1] + 20, obj.camera_pos[2])

            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))
    for obj in objects:
        obj.draw(screen)
    pygame.display.flip()
    clock.tick(60)