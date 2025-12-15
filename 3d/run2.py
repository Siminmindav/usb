import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Geometry Dash 3D")
clock = pygame.time.Clock()
running = True

class shape:
    def __init__(self, bottom_right, points, edges, camera_pos=(400, 300, 0), color=(255,255,255)):
        self.color = color
        self.camera_pos = camera_pos
        self.edges = edges
        self.bottom_right = bottom_right
        self.points = [(x + bottom_right[0], y + bottom_right[1], z + bottom_right[2]) for x, y, z in points]

    def draw(self, surface):
        for edge in self.edges:
            x0, y0, z0 = self.points[edge[0]]
            x1, y1, z1 = self.points[edge[1]]
            # Simple perspective projection
            f0 = 200 / (z0 + self.camera_pos[2] + 0.1)
            x0_proj = int(x0 * f0) + self.camera_pos[0] 
            y0_proj = int(y0 * f0) + self.camera_pos[1] 
            f1 = 200 / (z1 + self.camera_pos[2] + 0.1)
            x1_proj = int(x1 * f1) + self.camera_pos[0] 
            y1_proj = int(y1 * f1) + self.camera_pos[1] 
            if z0 + self.camera_pos[2] > 0 and z1 + self.camera_pos[2] > 0:
                pygame.draw.line(surface, self.color, (x0_proj, y0_proj), (x1_proj, y1_proj), 1)

    def update_position(self, new_bottom_right):
        dx = new_bottom_right[0] - self.bottom_right[0]
        dy = new_bottom_right[1] - self.bottom_right[1]
        dz = new_bottom_right[2] - self.bottom_right[2]
        self.points = [(x + dx, y + dy, z + dz) for x, y, z in self.points]
        self.bottom_right = new_bottom_right

planes = []
planespeed = 5
highscore = 0
score = 0
speed = 50
vspeed = [0,0,0]
health = 390

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
cube_obj = shape(bottom_right=(0, 0, 0), points=cube_points, edges=cube_edges, color=(255, 255, 255))
cube_obj.update_position((0, 200, 500))

plane_points = [
    (-200, 100, -200), (200, 100, -200),
    (200, 100, 200), (-200, 100, 200)
]
plane_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
]

for i in range(200):
    for j in range(3):
        plane_obj = shape(bottom_right=(0, 0, 0), points=plane_points, edges=plane_edges.copy(), color=(0, 205, 0))
        plane_obj.update_position((-400 + j * 405, 200, 81000 - i * 405))
        planes.append(plane_obj)
    r = randint(0, 3)
    match r:
        case 0:
            planes[-1].color = (255, 0, 0)
            planes[-1].edges.append((0,2))
            planes[-1].edges.append((1,3))
        case 1:
            planes[-2].color = (255, 0, 0)
            planes[-2].edges.append((0,2))
            planes[-2].edges.append((1,3))
        case 2:
            planes[-3].color = (255, 0, 0)
            planes[-3].edges.append((0,2))
            planes[-3].edges.append((1,3))
        case 3:
            planes[-1].color = (255, 0, 0)
            planes[-3].color = (255, 0, 0)
            planes[-1].edges.append((0,2))
            planes[-1].edges.append((1,3))
            planes[-3].edges.append((1,3))
            planes[-3].edges.append((0,2))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if cube_obj.bottom_right[0] - speed > -600:
                    cube_obj.update_position((cube_obj.bottom_right[0] - speed, cube_obj.bottom_right[1], cube_obj.bottom_right[2]))
            if event.key == pygame.K_d:
                if cube_obj.bottom_right[0] + speed < 600:
                    cube_obj.update_position((cube_obj.bottom_right[0] + speed, cube_obj.bottom_right[1], cube_obj.bottom_right[2]))
            if event.key == pygame.K_SPACE:
                if cube_obj.bottom_right[1] > 150:
                    vspeed[1] = -50



    if cube_obj.bottom_right[1] + vspeed[1] < 200:
        vspeed[1] += 2
    else:
        vspeed[1] = 0

    cube_obj.update_position((cube_obj.bottom_right[0] + vspeed[0], cube_obj.bottom_right[1] + vspeed[1], cube_obj.bottom_right[2] + vspeed[2]))

    if health < 0:
        score = 0
        health = 390
        planespeed = 5

    for plane in planes:
        if (cube_obj.bottom_right[0] > plane.bottom_right[0] - 200 and
            cube_obj.bottom_right[0] < plane.bottom_right[0] + 200 and
            cube_obj.bottom_right[1] + 100 > plane.bottom_right[1] - 100 and
            cube_obj.bottom_right[1] - 100 < plane.bottom_right[1] + 100 and
            cube_obj.bottom_right[2] + 100 > plane.bottom_right[2] - 100 and
            cube_obj.bottom_right[2] - 100 < plane.bottom_right[2] + 100):
            if plane.color == (255, 0, 0):
                health -= 5
            else:
                health += 0.05
                if health > 390: 
                    health = 390

    screen.fill((0, 0, 0))
   
    for plane in planes:
        plane.draw(screen)
        plane.update_position((plane.bottom_right[0], plane.bottom_right[1], plane.bottom_right[2] - planespeed))
        if plane.bottom_right[2] < 0:
            plane.update_position((plane.bottom_right[0], plane.bottom_right[1], 81000))
            planespeed += 0.04
            score += 1
            if score > highscore:
                highscore = score

    cube_obj.draw(screen)

    pygame.draw.rect(screen, (255, 0, 0), (10, 10, health * 2, 20))
    screen.blit(pygame.font.SysFont("arial", 20).render(f"Highscore: {int(highscore/3)}", True,(255,255,255)), (10, 40))
    screen.blit(pygame.font.SysFont("arial", 20).render(f"Score: {int(score/3)}", True,(255,255,255)), (10, 70))

    pygame.display.flip()
    clock.tick(60)