import pygame, os
from math import floor
pygame.init()

deafaultfont = pygame.font.SysFont("Arial", 20)


def on(x=0,y=0,sz=0,m=0):
    return pygame.mouse.get_pos()[0] > x and pygame.mouse.get_pos()[0] < x+sz and pygame.mouse.get_pos()[1] > y and pygame.mouse.get_pos()[1] < y+m

def onf(x=0,y=0,w=0,h=0, m=[0,0]): #faster because no get_pos function
    return m[0] > x and m[0] < x+w and m[1] > y and m[1] < y+h

def onrect(x1=0,y1=0,w1=0,h1=0, x2=0,y2=0,w2=0,h2=0):
    return x2 + w2/2 > x1 and x2 - w2/2 < x1 + w1 and y2 + h2/2 > y1 and y2 - h2/2 < y1 + h1

images = {}

for i in os.listdir("images"):
    path = os.path.join("images", i)
    key = os.path.splitext(i)[0]
    if i not in ["magyar.png", "english.png","español.svg","русский.png","performance.png"]:
        img = pygame.transform.scale(pygame.image.load(path), (50,50))
    elif i == "performance.png":
        img = pygame.transform.scale(pygame.image.load(path), (10,10))
    else:
        img = pygame.transform.scale(pygame.image.load(path),(150, 75))
    images[key] = img

for i in images:
    images[i].set_colorkey((240,240,240))

def textgenforaction(variables,base,opacity):
    return [
    f"{variables[0]}{floor(base.omega*10)/10}{variables[1]}",
    f"{variables[2]}{floor(base.w*10)/10}{variables[3]}",
    f"{variables[4]}{base.r}{variables[5]}",
    f"{variables[6]}{base.color.r}{variables[7]}",
    f"{variables[8]}{base.color.g}{variables[9]}",
    f"{variables[10]}{base.color.b}{variables[11]}",
    f"{variables[12]}{base.color.opacity}{variables[13]}",
    f"{variables[14]}{base.shapes[0]}{variables[15]}",
    f"{variables[16]}{base.shapes[1]}{variables[17]}",
    f"{variables[18]}{base.shapes[2]}{variables[19]}",
    f"{variables[20]}{opacity}{variables[21]}",
    f"{variables[22]}{base.angle}{variables[23]}",
    f"{variables[24]}"
]

def esaytext(text="missing text", size=20, color=(0,0,0), pos=(0,0), font=deafaultfont, surface=None):
    if surface == None:
        surface = pygame.display.get_surface()
    textsurface = font.render(text, True, color)
    surface.blit(textsurface, pos)

def easyimg(img, pos=(0,0), surface=None):
    if surface == None:
        surface = pygame.display.get_surface()
    surface.blit(img, pos)
    