#################################################
#2025.12.10
#the music is by tobi fox 
#other cool game:
#https://github.com/Siminmindav/spinner
#################################################

import pygame
import os
import sys
import random
import math
pygame.init()

class Ship:
    def __init__(self):
        self.image = images["ship"]
        self.rect = self.image.get_rect()
        self.rect.width -= 47
        self.rect.height -= 20
        self.x = 400
        self.y = 500
        self.sx = 0
        self.sy = 0
        self.speed = 0.3
        self.mu = 0.95
        self.xon = 0
        self.yon = 0
        self.health = 3

    def draw(self, surface):
        surface.blit(self.image, (self.x - 23 , self.y))
        if self.health <= 0:
            surface.blit(images["explosion"], (self.x - 23, self.y))
    
    def update(self):
        self.sx += self.xon * self.speed
        self.sy += self.yon * self.speed
        self.sx *= self.mu
        self.sy *= self.mu

        if self.x + self.sx < -70:
            self.sx = 0
            self.x = screensize[0] - self.rect.width + 69
        if self.x + self.sx > screensize[0] - self.rect.width + 70:
            self.sx = 0
            self.x = -69
        if self.y + self.sy < 0:
            self.sy = 0
            self.y = 0
        if self.y + self.sy > screensize[1] - self.rect.height:
            self.sy = 0
            self.y = screensize[1] - self.rect.height
        self.x += self.sx
        self.y += self.sy

        self.rect.topleft = (self.x, self.y) 

class bullet:
    def __init__(self, x, y):
        self.image = pygame.Surface((3, 15))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = 5

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
    
    def update(self):
        if self.y < -15:
            bullets.remove(self)
        self.y -= self.speed
        self.rect.topleft = (self.x, self.y) 

class alien:
    def __init__(self, x, y, speed, health):
        self.image = images["alien"]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = speed
        self.shot = False
        self.health = health
        self.max_health = health
        self.counter = 0
        
    def draw(self, surface):
        if self.shot:
            surface.blit(images["explosion"], (self.x - self.rect.width // 2, self.y - self.rect.height // 2 ))
            self.counter += 1
            if self.counter > 20:
                aliens.remove(self)
                global score
                score += 1
        else:
            surface.blit(self.image, (self.x, self.y))
    
    def update(self):
        self.x += self.speed + random.randint(-10, 10) * (self.max_health-self.health) / 8 * (self.shot-1)
        self.y += random.randint(-10, 10) * (self.max_health-self.health) / 8 * (self.shot-1)
        if self.x > screensize[0]:
            self.speed = abs(self.speed) * -1
        if self.x < -self.rect.width:
            self.speed = abs(self.speed)
        if self.y > screensize[1]:
            self.y = screensize[1] - self.rect.height
        if self.y < -self.rect.height:
            self.y = -self.rect.height+1
        self.rect.topleft = (self.x, self.y) 
        if self.health <= 0:
            self.shot = True

class alien2(alien):
    def __init__(self, x, y, speed, health, reload):
        super().__init__(x, y, speed, health)
        self.image = images["alien2"]
        self.rect = self.image.get_rect()
        self.reload = reload
        self.reload_counter = 0
    
    def draw(self, surface):
        if self.shot:
            surface.blit(images["explosion"], (self.x, self.y))
            self.counter += 1
            if self.counter > 20:
                aliens.remove(self)
                global score
                score += 2
        else:
            surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.x += self.speed + random.randint(-10, 10) * (self.max_health-self.health) / 100 * (self.shot-1)
        self.y += random.randint(-10, 10) * (self.max_health-self.health) / 100 * (self.shot-1)
        if self.x > screensize[0]:
            self.speed = self.speed * -1
        if self.x < -self.rect.width:
            self.speed = self.speed * -1
        if self.y > screensize[1]:
            self.y = screensize[1] - self.rect.height
        if self.y < -self.rect.height:
            self.y = -self.rect.height+1
        self.rect.topleft = (self.x, self.y) 
        if self.health <= 0:
            self.shot = True
        self.reload_counter += 1
        if self.reload_counter >= self.reload and not self.shot:
            self.reload_counter = 0
            self.shoot()

    def shoot(self):
        alien_bullets.append(bullet2(self.x + 6, self.y + self.rect.height-20))
        alien_bullets.append(bullet2(self.x + 33, self.y + self.rect.height-8))
        alien_bullets.append(bullet2(self.x + 66, self.y + self.rect.height-8))
        alien_bullets.append(bullet2(self.x + 89, self.y + self.rect.height-20))
        sounds["shoot"].play()
        
class bullet2(bullet):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.Surface((6, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
    
    def draw(self, surface):
        super().draw(surface)
    
    def update(self):
        if self.y > screensize[1]:
            alien_bullets.remove(self)
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

class star:
    def __init__(self):
        self.x = random.randint(0, screensize[0])
        self.y = random.randint(0, screensize[1])
        self.size = random.choice([1,1,1,1,1,2,2,2,3])
        self.r = (3-self.size)*40 + 130
        self.b = self.size*25 + 100
        self.speed = self.size / 2

    def draw(self, surface):
        pygame.draw.circle(surface, (self.r, 160, self.b), (self.x, self.y), self.size)
    
    def update(self):
        self.y += self.speed
        if self.y > screensize[1]:
            self.y = 0
            self.x = random.randint(0, screensize[0])
        if self.y > screensize[1]:
            self.y = 0

def onclick(x,y,w,h, mx, my):
    if mx > x and mx < x + w and my > y and my < y + h:
        return True
    return False

screensize = (600, 600)
images = {}
sounds = {}
sound_on = True
bullets = []
alien_bullets = []
aliens = []
stars = [star() for _ in range(100)]
score = 0
level = 1
debug = False
new_highscore = False

for f in os.listdir("images"):
    images[f.split(".")[0]] = pygame.image.load(os.path.join("images", f))
    images[f.split(".")[0]].set_colorkey((255, 255, 255))
    if f.split(".")[0] == "alien":
        images[f.split(".")[0]] = pygame.transform.scale(images[f.split(".")[0]], (50, 50))

for f in os.listdir("sounds"):
    sounds[f.split(".")[0]] = pygame.mixer.Sound(os.path.join("sounds", f))
    if f.split(".")[0] in "shoot":
        sounds[f.split(".")[0]].set_volume(0.1)
    if f.split(".")[0] in "explosion":
        sounds[f.split(".")[0]].set_volume(0.3)

ship = Ship()   

captions = [
    "space invaders but better (probably)",
    "vibecoded by: siminmindav",
    "have fun!",
    "resize the window to make the game easier!",
    "use F or f11 to toggle the broken fullscreen mode",
    "press ő and have linux to enable debug mode (if you can >:D)",
    "press F1 to take a screenshot",
    "press m to silence/un-silence the game",
]

screen = pygame.display.set_mode(screensize, pygame.RESIZABLE)
pygame.display.set_caption(f"shooter - {random.choice(captions)}")
clock = pygame.time.Clock()
running = True

for i in range(5):
    for j in range(2):
        aliens.append(alien(i * 100 + 50, j * 100 + 50, 1, 1))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            screensize = (event.w, event.h)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if ship.health <= 0:
                mx, my = pygame.mouse.get_pos()
                if onclick(screensize[0]//2 - 33, screensize[1]//2 + 97, 100, 30, mx, my):
                    ship = Ship()
                    bullets = []
                    aliens = []
                    score = 0
                    level = 1
                    for i in range(5):
                        for j in range(3):
                            aliens.append(alien(i * 100 + 50, j * 100 + 50, level, level))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.xon -= 1
            if event.key == pygame.K_RIGHT:
                ship.xon += 1
            if event.key == pygame.K_UP:
                ship.yon -= 1
            if event.key == pygame.K_DOWN:
                ship.yon += 1
            if event.key == pygame.K_SPACE:
                bullets.append(bullet(ship.x + ship.rect.width // 2 - 26, ship.y))
                bullets.append(bullet(ship.x + ship.rect.width // 2 + 14, ship.y))
                if sound_on:
                    sounds["shoot"].play()
            if event.key == pygame.K_F11 or event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                    pygame.display.set_mode(screensize, pygame.SCALED)
            if pygame.key.name(event.key) == "ő":
                debug = not debug
            if event.key == pygame.K_F1:
                pygame.image.save(screen, "screenshot.png")
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_m:
                sound_on = not sound_on
                if sound_on:
                    pygame.mixer.unpause()
                else:
                    pygame.mixer.pause()

            if debug and sys.platform == "linux":
                if event.key == pygame.K_HOME:
                    ship.x = 400
                    ship.y = 650
                    ship.sx = 0
                    ship.sy = 0
                if event.key == pygame.K_END:
                    ship.health = 0
                if event.key == pygame.K_DELETE:
                    aliens = []
                if event.key == pygame.K_SCROLLLOCK:
                    ship.health = 1000

                if event.key == pygame.K_PAGEUP:
                    aliens = []
                    aliens.append(alien2(300, 200, 0, 10, 60))
                if event.key == pygame.K_PAGEDOWN:
                    aliens = []
                    for i in range(5):
                        for j in range(3):
                            aliens.append(alien(i * 100 + 50, j * 100 + 50, 3, 1))

                if event.key == pygame.K_F2:
                    for i in range(20):
                        for j in range(5):
                            bullets.append(bullet(i * 40, j * 30 + ship.y))

            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ship.xon = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ship.yon = 0


    if pygame.mixer.music.get_busy() == False and sound_on:
        pygame.mixer.music.load(os.path.join("sounds", "music.ogg"))
        pygame.mixer.music.play()
    else:
        if not sound_on:
            pygame.mixer.music.stop()

    ship.update()
    for b in bullets:
        b.update()
        for a in aliens:
            if b.rect.colliderect(a.rect):
                try: 
                    bullets.remove(b)
                except:
                    pass
                a.health -= 1
                if a.health <= 0:
                    sounds["explosion"].play()

    for b in alien_bullets:
        b.update()
        if b.rect.colliderect(ship.rect):
            try:
                alien_bullets.remove(b)
            except:
                pass
            ship.health -= 1
            if ship.health <= 0:
                sounds["explosion"].play()

    for a in aliens:
        a.update()
        if a.rect.colliderect(ship.rect) and not a.shot:
            a.shot = True
            sounds["explosion"].play()
            if ship.health >= 0:
                ship.health -= 1

    if len(aliens) == 0 and ship.health > 0:
        level += 1
        if level % 3 == 0:
            for i in range(2):
                for j in range(2):
                    aliens.append(alien2(i * 200 + 50, j * 200 + 50, level / 5, level * 2 , max(300 - level * 7, 20)))
        else:
            for i in range(5):
                for j in range(3):
                    aliens.append(alien(i * 100 + 50, j * 100 + 50, level, level))

    screen.fill((50,50,60))
    for s in stars:
        s.update()
        s.draw(screen)
    
    ship.draw(screen)
    for b in bullets:
        b.draw(screen)
    for b in alien_bullets:
        b.draw(screen)
    for a in aliens:
        a.draw(screen)

    screen.blit(pygame.font.SysFont("Arial", 24).render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    screen.blit(pygame.font.SysFont("Arial", 24).render(f"Level: {level}", True, (255, 255, 255)), (10, 40))
    screen.blit(pygame.font.SysFont("Arial", 24).render(f"Health: {ship.health}", True, (255, 255, 255)), (10, 70))
    if debug:
        screen.blit(pygame.font.SysFont("Arial", 24).render(f"Debug mode on", True, (255, 255, 255)), (screensize[0]-200,10))
        screen.blit(pygame.font.SysFont("Arial", 24).render(f"Fps: {math.floor(clock.get_fps()*100)/100}", True, (255, 255, 255)), (screensize[0]-200,40))
        screen.blit(pygame.font.SysFont("Arial", 24).render(f"Sound: {sound_on}", True, (255, 255, 255)), (screensize[0]-200,70))
        screen.blit(pygame.font.SysFont("Arial", 11).render(f"home, insert aliens, delete alien2, end die, scrolllock 1000h, f1 screenshot, f2 bullets, f11 window sizer, ő debug", True, (255, 255, 255)), (0,screensize[1]-10))
        pygame.draw.rect(screen,(255, 0, 0),(ship.rect.x, ship.rect.y, ship.rect.width, ship.rect.height), 1)
        for a in aliens:
            pygame.draw.rect(screen,(0, 255, 0),(a.rect.x, a.rect.y, a.rect.width, a.rect.height), 1)
            screen.blit(pygame.font.SysFont("Arial", 12).render(f"H: {a.health}", True, (255, 255, 255)), (a.rect.x, a.rect.y - 15))
        for b in bullets:
            pygame.draw.rect(screen,(0, 0, 255),(b.rect.x, b.rect.y, b.rect.width, b.rect.height), 1)
        for b in alien_bullets:
            pygame.draw.rect(screen,(255, 255, 0),(b.rect.x, b.rect.y, b.rect.width, b.rect.height), 1)

    if ship.health <= 0:
        with open("highscore", "r") as f:
            highscore = int(f.read())
        if score > highscore and not debug:
            with open("highscore", "w") as f:
                f.write(str(score))
                new_highscore = True
            highscore = score
        screen.blit(pygame.font.SysFont("Arial", 72).render(f"GAME OVER", True, (255, 0, 0)), (screensize[0]//2 - 200, screensize[1]//2 - 100))
        if new_highscore:
            screen.blit(pygame.font.SysFont("Arial", 36).render(f"NEW HIGHSCORE: {highscore}", True, (255, 255, 0)), (screensize[0]//2 - 150, screensize[1]//2 - 25))
        else:
            screen.blit(pygame.font.SysFont("Arial", 36).render(f"Highscore: {highscore}", True, (255, 255, 255)), (screensize[0]//2 - 90, screensize[1]//2 - 25))
        screen.blit(pygame.font.SysFont("Arial", 36).render(f"Final Score: {score}", True, (255, 255, 255)), (screensize[0]//2 - 100, screensize[1]//2 + 20))
        screen.blit(pygame.font.SysFont("Arial", 24).render(f"Press ESC to exit or", True, (255, 255, 255)), (screensize[0]//2 - 95, screensize[1]//2 + 65))
        pygame.draw.rect(screen,(255, 255, 255),(screensize[0]//2 - 33, screensize[1]//2 + 97, 100, 30), 2)
        screen.blit(pygame.font.SysFont("Arial", 24).render(f"REPLAY", True, (255, 255, 255)), (screensize[0]//2 - 30, screensize[1]//2 + 100))
        aliens = []
        bullets = []
        ship.speed = 0

    pygame.display.flip() 
    clock.tick(60)         