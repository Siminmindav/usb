"""
music:
_________________________________________________
Music: TheFatRat - Time Lapse
Watch the official music video: https://tinyurl.com/tfrtimelapse
Listen to Time Lapse: https://thefatrat.ffm.to/timelapse
Follow TheFatRat: https://ffm.bio/thefatrat
_________________________________________________

Music: TheFatRat - Unity
Watch the official music video: https://tinyurl.com/unitytfr
Listen to Unity: https://thefatrat.ffm.to/unity
Follow TheFatRat: https://ffm.bio/thefatrat
_________________________________________________
and some other music...

"""
import pygame
import os
import sys
import random
pygame.init()

score = 0
debug = 0
playmusic = 1
musicnumber = 0
fullscreen = -1
music = ["sounds/001","sounds/002","sounds/003"]
frames = 0
images = {}
sounds = {}
bullets = []
screensize = (800, 900)
smolarea = (0,211,470,582) #x y w h
showparts = [0,0,0]
moveparts = [0,0,0]
pushingrect = [710,100,860,360]
borders = [
    [0,160,500,210],
    [475,200,500,570],
    [475,670,500,800],
    [0,800,800,900],
    [500,500,575,550],
    [700,500,800,550],
    [770,50,800,500],
    [0,0,800,50],
    [570,150,620,250]
]
secretcover = [
    [0,0,475,210],
    [470,0,800,100],
    [470,100,800,200],
    [470,200,800,300],
    [470,300,800,400],
    [470,400,800,500],
    [470,500,800,550],
    [470,550,800,797],
]
captions = [
    "now for free!",
    "now for free!",
    "for the whole family to enjoy!",
    "for the whole family to enjoy!",
    "you can add your own music, or not.",
    "you can add your own music, or not.",
    "have a beautiful day!",
    "have a good day!",
    "have a wonderful day!",
    "  :D  ",
    "do 10 push-ups!",
    "carpe diem!",
    "en medias virtus.",
    "I don't like this music, I prefer chopin...",
    "   pygame doesen't suck, you do. -Jujustu Kaisen the art of war",
    "what do I write here? 😭🥀🥀",
    "please kill me"
]
textnumber = 0
texts =[
    "Press enter to go on.",
    "",
    "Press backspace to go back.",
    "",
    "Use arrows to move and space to shoot.",
    "Use f11 to enlarge window. Use end because you can.",
    "Also you can press m to stop the",
    "annoying roblox tycoon music.",
    "I should've made some music, but it's 1 am.",
    "I should've asked someone to make music... hmmm... Im tired...",
    "Text goes here.     ;)      :D         \-|°_°|-/",
    "Second line goes here.    :o    :0",
    "",
    "-------------End--------------",
    "",
    "-------------End?--------------",
    "",
    "",
    "If you are stuck, try going along the walls,",
    "to find something, interesting...",

]

font = pygame.font.SysFont("Arial", 24)
screen = pygame.display.set_mode(screensize, pygame.RESIZABLE)
pygame.display.set_caption(f"regular shooter game - {captions[random.randint(0,len(captions)-2)]}")
clock = pygame.time.Clock()
screen.blit(font.render(f"{'Loading':-^97}",True,(255,255,255)),(0,0))
pygame.display.flip()


for f in os.listdir("images"):
    images[f.split(".")[0]] = pygame.image.load(os.path.join("images", f))

    if f.split(".")[0] in ("broken","thumbnail"):
        images[f.split(".")[0]] = pygame.transform.scale(images[f.split(".")[0]], (100, 100))
    if f.split(".")[0] in ("legs","hatch","greenman", "alien"):
        images[f.split(".")[0]] = pygame.transform.scale(images[f.split(".")[0]], (50, 50))
    images[f.split(".")[0]].set_colorkey((255, 255, 255))

for f in os.listdir("sounds"):
    sounds[f.split(".")[0]] = pygame.mixer.Sound(os.path.join("sounds", f))
    if f.split(".")[0] in "shoot":
        sounds[f.split(".")[0]].set_volume(0.04)
    if f.split(".")[0] in "explosion":
        sounds[f.split(".")[0]].set_volume(0.2)
    if f.split(".")[0] in "impact1":
        sounds[f.split(".")[0]].set_volume(0.05)
    if f.split(".")[0] in "impact2":
        sounds[f.split(".")[0]].set_volume(0.05)



def drawtext(x=0,y=0,text="missing text",font=font):
        screen.blit(font.render(str(text), True, (255, 255, 255)), (x,y))

def onrect(x,y,w,h, rect):
    if rect[0] > x and rect[0] + rect[2] < x + w and rect[1] > y and rect[1] + rect[3] < y + h:
        return True
    return False

def onpoint(x,y,w,h, px, py):
    if px > x and px < x + w and py > y and py < y + h:
        return True
    return False

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

        if self.x + self.sx < 0:
            self.sx = 0
        if self.x + self.sx > screensize[0] - self.rect.width:
            self.sx = 0
        if self.y + self.sy < 0:
            self.sy = 0
        if self.y + self.sy > screensize[1] - self.rect.height:
            self.sy = 0
        for b in borders:
            if self.x + self.rect.width + self.sx > b[0] and self.x + self.sx < b[2] and self.y + self.rect.height > b[1] and self.y < b[3]:
                self.sx = 0
            if self.x + self.rect.width + self.sx > b[0] and self.x + self.sx < b[2] and self.y + self.rect.height + self.sy > b[1] and self.y + self.sy < b[3]:
                self.sy = 0
        if onrect(pushingrect[0],pushingrect[1],pushingrect[2]-pushingrect[0],pushingrect[3]-pushingrect[1], (self.rect)):
            self.sx -= 1


        self.x += self.sx
        self.y += self.sy

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
            if self.counter == 0:
                sounds["explosion"].play()
            surface.blit(images["explosion"], (self.x - self.rect.width // 2, self.y - self.rect.height // 2 ))
            self.counter += 1
            if self.counter > 20:
                aliens.remove(self)
        else:
            surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.x += self.speed
        if self.x > smolarea[2] - self.rect.width:
            self.speed = abs(self.speed) * -1
            self.y += 5
        if self.x < 0:
            self.speed = abs(self.speed)
            self.y += 5
        if self.y > screensize[1]+500:
            pass
        if self.y < -self.rect.height:
            self.y = -self.rect.height+1
        self.rect.topleft = (self.x, self.y) 
        if self.y < 200:
            self.y += 1
        if self.health <= 0:
            self.shot = True

class bullet:
    def __init__(self, x, y):
        self.image = pygame.Surface((3, 15))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = 7

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
    
    def update(self):
        self.y -= self.speed
        self.rect.topleft = (self.x, self.y)
        
class star:
    def __init__(self):
        self.area = smolarea 
        self.x = random.randint(self.area[0], self.area[2] + self.area[0])
        self.y = random.randint(self.area[1], self.area[3] + self.area[1])
        self.size = random.choice([1,1,1,1,1,2,2,2,3])
        self.r = (3-self.size)*40 + 130
        self.b = self.size*25 + 100
        self.speed = self.size / 4

    def draw(self, surface):
        pygame.draw.circle(surface, (self.r, 160, self.b), (self.x, self.y), self.size)
    
    def update(self):
        self.y += self.speed
        if self.y > self.area[1] + self.area[3]:
            self.y = self.area[1]
            self.x = random.randint(self.area[0], self.area[2] + self.area[0])

class alienpart:
    def __init__(self, x, y, tipus):
        self.tipus = tipus
        match tipus:
            case 0:
                self.image = images["legs"]
            case 1:
                self.image = images["greenman"]
            case 2:
                self.image = images["hatch"]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
    
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self, moveparts):
        if self.x > 650:
            self.x -=1
        if moveparts[0] and self.tipus == 0:
            moveparts[0] = 0
            self.x = 750
        if moveparts[1] and self.tipus == 1:
            moveparts[1] = 0
            self.x = 750
        if moveparts[2] and self.tipus == 2:
            moveparts[2] = 0
            self.x = 750


class hands:
    def __init__(self):
        self.x = 580
        self.y = 185
        self.offset = 40
        self.x2= 100
        self.y2 = 100
        self.one = 0
        self.two = 0
    
    def draw(self, surface):
        pygame.draw.line(surface, (0,0,0), (self.x, self.y), (self.x2,self.y2), width=3)
        pygame.draw.line(surface, (0,0,0), (self.x+self.offset, self.y), (self.x2+self.offset,self.y2), width=3)

    def update(self, frame):
        global showparts
        match frame:
            case 1:
                self.x2 = 650
                self.y2 = 115
                self.one = 1
            case 2:
                if self.one:
                    self.one = 0
                    self.x2 = 520
                    self.y2 = 300
                    showparts = [1,0,0]
                    moveparts[0] = 1
            case 3:
                self.x2 = 650
                self.y2 = 215
                self.one = 1
            case 4:
                if self.one:
                    self.one = 0
                    self.x2 = 520
                    self.y2 = 300
                    showparts = [1,1,0]
                    moveparts[1] = 1
            case 5:
                self.x2 = 650
                self.y2 = 315
                self.one = 1
            case 6:
                if self.one:
                    self.one = 0
                    self.x2 = 520
                    self.y2 = 300
                    showparts = [1,1,1]
                    moveparts[2] = 1
                    self.two = 1
            case 7:
                if self.two: 
                    self.two = 0
                    self.x2 = random.randint(0,420)
                    self.y2 = 150
                    aliens.append(alien(self.x2, self.y2+20, random.randint(15,20)/10, 1))
                    showparts = [0,0,0]



ship = Ship()
stars = [star() for _ in range(500)]
aliens = []
parts = [alienpart(750,115,0),alienpart(750,215,1),alienpart(750,315,2)]
handz = hands()

for i in range(2):
    for j in range(2):
        aliens.append(alien(i * 100 + 50, j * 100 + 300, 1, 1))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

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
                bullets.append(bullet(ship.x,ship.y))
                bullets.append(bullet(ship.x + ship.rect.width-10 ,ship.y))
                sounds["shoot"].play()

            if event.key == pygame.K_F11:
                if fullscreen == -1:
                    pygame.display.toggle_fullscreen()
                    pygame.display.set_mode(screensize, pygame.SCALED)
                else:
                    screen = pygame.display.set_mode(screensize, pygame.RESIZABLE)
                fullscreen *= -1
            if event.key == pygame.K_END:
                pygame.display.set_caption(f"regular shooter game - {captions[random.randint(0,len(captions)-2)]}")
            if event.key == pygame.K_m:
                playmusic *= -1
            if event.key == pygame.K_RETURN:
                if textnumber + 2 < len(texts):
                    textnumber += 2
            if event.key == pygame.K_BACKSPACE:
                if 1 < textnumber:
                    textnumber -= 2
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()
            if event.key == 246: #ö
                debug = 1 if debug == 0 else 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ship.xon = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ship.yon = 0

        if debug:
            print(event)

    if playmusic == -1 or debug:
        pygame.mixer.music.stop()
    else:
        if not pygame.mixer.music.get_busy():
            if musicnumber > len(music)-1:
                musicnumber = 0
            pygame.mixer.music.load(music[musicnumber])
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.04)
            musicnumber += 1


    try:
        ship.update()
    

        frames += 1
        screen.blit(images[f"background{frames//6%5+1}"],(0,0))
        handz.update(frames//abs(60-score//3)%7+1)
        
        for s in stars:
            s.update()
            s.draw(screen)
        for a in aliens:
            a.update()
            a.draw(screen)
            if a.y > screensize[1]+500:
                aliens.remove(a)
        for b in bullets:
            b.update()
            b.draw(screen)
            for a in aliens:
                if onpoint(a.x,a.y,a.rect.width,a.rect.height,b.x,b.y):
                    a.health -= 1
                    score += 1
                    bullets.remove(b)
                    break
            for o in borders:
                if onpoint(o[0],o[1],o[2]-o[0],o[3]-o[1],b.x,b.y):
                    bullets.remove(b)
                    sounds["impact2"].play() if random.randint(0,1) else sounds["impact1"].play()
        for p in parts:
            p.draw(screen)
            p.update(moveparts)

        if showparts[1]:
            screen.blit(images["greenman"], (520,300))
        if showparts[0]:
            screen.blit(images["legs"], (520,300))
        if showparts[2]:
            screen.blit(images["hatch"], (520,300))

        screen.blit(images["worker"],(550,150))
        handz.draw(screen)
        ship.draw(screen)

        if secretcover and not debug:
            for s in secretcover:
                pygame.draw.rect(screen,(0,0,0),(s[0],s[1],s[2]-s[0],s[3]-s[1]))
                if onpoint(s[0],s[1],s[2]-s[0],s[3]-s[1],ship.x,ship.y):
                    secretcover.remove(s)
        
        drawtext(120, 820, texts[textnumber])
        drawtext(120, 850, texts[textnumber+1])
        drawtext(0, 820, f"Scr: {score}")


        #debug
        pygame.draw.rect(screen,(10,10,10),(800,0,800,800))
        x,y = 0,0
        for i in images:
            x += 1
            if x > 5:
                y += 1
                x = 0
            if "background" in i:
                continue
            screen.blit(images[i], (800+100*x,240+100*y))
        if debug:
            for b in borders:
                pygame.draw.rect(screen,(255,0,0),(b[0],b[1],b[2]-b[0],b[3]-b[1]),2)
        drawtext(1000, 20, f"{int(clock.get_fps())} fps")
        drawtext(800, 60, "I was planning to make a boss fight, I didn't do it, but I can tell how ")
        drawtext(800, 80, "would it look like. So you would be the worker that builds rockets,")
        drawtext(800, 100, "and enemies would come you would get points and upgrade stuff,")
        drawtext(800, 120,"like faster parts(hatch.png legs.png greenman.png) delivery. ")
        drawtext(800, 140, "And then the Sweat the main boss would come, after you win, the Sweat  ")
        drawtext(800, 160, "throws his keyboard at the screen (keyboard.png) breaking (broken.png) it.")
        drawtext(800, 180, "Also there would be head pictures in the left corner like in undertale.")
        drawtext(800, 200, "And an intern that you need to kill, funny named pilot and much more...")
        drawtext(800, 220, "This won't game is not finished, it doesen't need to be.")
        drawtext(800, 240, "It's good enough...")
        drawtext(800, 20, f"{frames//6%5+1} {frames//abs(60-score//3)%7+1} {frames}")
        pygame.display.flip() 

    except:
        print("well, that sucks.\n some error happened,")

    
    clock.tick(60)  
