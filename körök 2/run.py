#**********spirál körök 2.0***********
#
#to do:
#-optimalizálás: Creating surfaces every frame 
#-több példa
#-paulus fordítása
#-felvállalhattó zene
#-tutorial
#
#*************************************

import pygame, math, random, sys, pickle, os
from spinner import *
from ui2 import ui2
from ui3 import ui3
from functions import on, images, onf, textgenforaction
import példák 
sys.path.append("lang")

pygame.init()

DEBUG = False

if not DEBUG:
    nyelv = ui3()
else:
    nyelv = "magyar"

if nyelv == "english":
    import textEN as nyelv
if nyelv == "español":
    import textES as nyelv
if nyelv == "magyar":
    import textHU as nyelv
if nyelv == "русский":
    import textRU as nyelv

#ui4 tutorial

if not DEBUG:
    sw, sh, fullscreen = ui2(nyelv.textlist)
else:
    sw, sh, fullscreen = 1500, 1500, False

screen = pygame.display.set_mode((sw,sh))
if fullscreen:
    pygame.display.toggle_fullscreen()
pygame.display.set_caption(nyelv.caption)
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 20)
overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

zenék = ["music/chop.mp3", "music/chop2.mp3", "music/chop3.mp3", "music/chop4.mp3", "music/chop5.mp3", "music/chop6.mp3", "music/chop7.mp3", "music/chop8.mp3", "music/chop9.mp3", ]
run = True
vars = {
    'opacity' : 25,
    'action' : 0,
    'crease' : 0,
    'pause' : -1,
    "developer ui" : -1,
    "show frames" : 1,
    "settings" : -1,
    "centerless" : 1,
    "central" : 0,
    "playmusic" : 1,
    "musicnumber" : 0,
    "info" : -1,
    "example" : 0,
    "saving" : -1,
    "importing" : -1,
    "minimum show" : 1,
    "selected file" : "",
    "performance" : 1,
    "erase" : -1,
    "trashing" : -1,
    "leaving" : -1
}
mousepos = [0,0]
base = spinner(400, 400, 20, 20,   600, 400, 20, 20, [0, 0, 0, 255], 0, 2, 200, [0,1,0,1])
spinners = [
#spinner(400, 400, 20, 20,   600, 400, 20, 20, (0, 0, 0, 255), 0, 2, 200, (0,1,0,1))
]

#példák debug
if DEBUG:
    pass

pygame.mixer.music.stop()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Hasta la vista!")
            run = False
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            #print(pygame.key.name(event.key))
            if vars["saving"] == -1:
                if pygame.key.name(event.key) == "space":
                    spinners.append(spinner(base.ox,base.oy,base.ow,base.oh,base.x,base.y,base.w,base.h,(base.color.r,base.color.g,base.color.b,base.color.opacity),base.angle,base.omega,base.r,[base.shapes[0],base.shapes[1],base.shapes[2],base.shapes[3]]))
                elif pygame.key.name(event.key) == "backspace":
                    if spinners:
                        spinners.pop()
            else:
                if on(60,100,380,50):
                    if pygame.key.name(event.key) == "backspace":
                        if vars["selected file"]:
                            vars["selected file"] = vars["selected file"][:-1]
                    else:
                        vars["selected file"] += event.unicode
            if pygame.key.name(event.key) == "escape":
                vars["leaving"] *= -1

            if vars["leaving"] == 1:
                if pygame.key.name(event.key) == "return":
                    print("Hasta la vista!")
                    run = False
                    pygame.quit()
                    sys.exit()

        elif event.type == pygame.MOUSEBUTTONUP:
            vars["crease"] = 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:#left
                mousepos = pygame.mouse.get_pos()

                if onf(0,0,10,10, mousepos):
                    print("performance")
                    vars["performance"] *= -1

                if vars["leaving"] == 1:
                    if onf(100,250,50,50, mousepos):
                        print("yes")
                        print("Hasta la vista!")
                        run = False
                        pygame.quit()
                        sys.exit()
                    if onf(350,250,50,50, mousepos):
                        print("no")
                        vars["leaving"] = -1
                        
                if vars["performance"] == 1:
                    if onf(5,sh-115,50,50, mousepos):
                        print("increase")
                        vars["crease"] = 1
                    if onf(65,sh-115,50,50, mousepos):
                        print("red")
                        vars["action"] = 3
                    if onf(125,sh-115,50,50, mousepos):
                        print("green")
                        vars["action"] = 4
                    if onf(185,sh-115,50,50, mousepos):
                        print("blue")
                        vars["action"] = 5
                    if onf(245,sh-115,50,50, mousepos):
                        print("rectangle")
                        vars["action"] = 7
                        if base.shapes[0]:
                            base.shapes[0] = 0
                        else:
                            base.shapes[0] =  1
                    if onf(305,sh-115,50,50, mousepos):
                        print("circle")
                        vars["action"] = 8
                        if base.shapes[1]:
                            base.shapes[1] = 0
                        else:
                            base.shapes[1] =  1                   
                    if onf(365,sh-115,50,50, mousepos):
                        print("line")
                        vars["action"] = 9
                        if base.shapes[2]:
                            base.shapes[2] = 0
                        else:
                            base.shapes[2] =  1                    
                        
                    if onf(5,sh-55,50,50, mousepos):
                        print("decrease")
                        vars["crease"] = -1
                    if onf(65,sh-55,50,50, mousepos):
                        print("speed")
                        vars["action"] = 0
                    if onf(125,sh-55,50,50, mousepos):
                        print("size")
                        vars["action"] = 1
                    if onf(185,sh-55,50,50, mousepos):
                        print("distance")
                        vars["action"] = 2
                    if onf(245,sh-55,50,50, mousepos):
                        print("opacity")
                        vars["action"] = 6
                    if onf(305,sh-55,50,50, mousepos):
                        print("backgroundopacity")
                        vars["action"] = 10
                    if onf(365,sh-55,50,50, mousepos):
                        print("rotate")
                        vars["action"] = 11
                    if onf(425,sh-55,50,50, mousepos):
                        print("reset")
                        base = spinner(400, 400, 20, 20,   600, 400, 20, 20, [0, 0, 0, 255], 0, 2, 200, [0,1,0,1])

                    if vars["settings"] == 1:
                        if onf(sw-180,110,50,50, mousepos):
                            print("save")
                            vars["saving"] *= -1
                        if onf(sw-180,165,50,50, mousepos):
                            print("show T")
                            vars["centerless"] *= -1
                        if onf(sw-180,220,50,50, mousepos):
                            print("music T")
                            vars["playmusic"] *= -1
                        if onf(sw-180,275,50,50, mousepos):
                            print("centric T")
                            vars["central"] += 1
                            vars["central"] %= 3
                        if onf(sw-180,330,50,50, mousepos):
                            print("frame T")
                            vars["show frames"] *= -1
                        if onf(sw-180,385,50,50, mousepos):
                            print("heart")
                            vars["developer ui"] *= -1

                        if onf(sw-125,110,50,50, mousepos):
                            print("import")
                            vars["importing"] *= -1
                        if onf(sw-125,165,50,50, mousepos):
                            print("erase")
                            vars["erase"] *= -1
                        if onf(sw-125,220,50,50, mousepos):
                            print("play T")
                            vars["pause"] *= -1
                        if onf(sw-125,275,50,50, mousepos):
                            print("book")
                            vars["example"] += 1
                            vars["example"] %= 3
                            if vars["example"] == 0:
                                példák.pl1(spinners,spinner)
                            elif vars["example"] == 1:
                                példák.pl2(spinners,spinner)
                            elif vars["example"] == 2:
                                példák.pl3(spinners,spinner)
                        if onf(sw-125,330,50,50, mousepos):
                            print("info")
                            vars["info"] *= -1
                        if onf(sw-125,385,50,50, mousepos):
                            print("exit")
                            vars["leaving"] *= -1

                    if onf(sw-55,5,50,50, mousepos):
                        print("trash")
                        vars["trashing"] *= -1
                    if onf(sw-55,165,50,50, mousepos):
                        print("settings")
                        vars["settings"] *= -1
                    if onf(sw-55,sh-115,50,50, mousepos):
                        print("add")
                        spinners.append(spinner(base.ox,base.oy,base.ow,base.oh,base.x,base.y,base.w,base.h,(base.color.r,base.color.g,base.color.b,base.color.opacity),base.angle,base.omega,base.r,[base.shapes[0],base.shapes[1],base.shapes[2],base.shapes[3]]))
                    if onf(sw-55,sh-55,50,50, mousepos):
                        print("remove")
                        if spinners:
                            spinners.pop()

                    if vars["trashing"] == 1:
                        if onf(100,250,50,50, mousepos):
                            print("yes")
                            spinners = []
                            vars["trashing"] = -1
                        if onf(350,250,50,50, mousepos):
                            print("no")
                            vars["trashing"] = -1

                    if vars["importing"] == 1:
                        if onf(390,60,50,50, mousepos):
                            print("increase")
                            vars["minimum show"] -= 1
                        if onf(390,110,50,50, mousepos):
                            print("decrease")
                            vars["minimum show"] += 1
                        if onf(390,165,50,50, mousepos):
                            if vars["selected file"]:
                                with open(f"saves/{vars['selected file']}", "rb") as f:
                                    for v in pickle.load(f):
                                        spinners.append(v)
                            vars["importing"] = -1
                            vars["selected file"] = ""
                        i = 0
                        for f in os.listdir("saves"):
                            if vars["minimum show"] <= i and (60+(i-vars["minimum show"])*25) < 250:
                                if onf(60,60+(i-vars["minimum show"])*25,300,25,mousepos):
                                    print(f)
                                    vars["selected file"] = f
                            i += 1
                        
                    if vars["saving"] == 1:
                        if onf(390,165,50,50, mousepos):
                            print("ok")
                            if vars["selected file"]:
                                with open(f"saves/{vars['selected file']}", "wb") as f:
                                    pickle.dump(spinners, f)
                            vars["saving"] = -1

                    if vars["erase"] == 1:
                        for i in spinners:
                            if onf(i.ox-i.ow/2, i.oy-i.oh/2,i.ow,i.oh, mousepos):
                                spinners.pop(spinners.index(i))

                    
            if vars["performance"] == 1:  
                if event.button == 2:#middle click
                    vars['action'] += 1
                    vars['action'] %= 13 
                if event.button == 3:#right
                    pass
                if event.button == 4:#up
                    if vars['action'] == 0: base.omega += 0.1
                    if vars['action'] == 1:
                        base.w += 1
                        base.h += 1
                    if vars['action'] == 2: base.r += 1
                    if vars['action'] == 3:
                        base.color.r += 1
                        base.color.r %= 256
                    if vars['action'] == 4:
                        base.color.g += 1
                        base.color.g %= 256
                    if vars['action'] == 5:
                        base.color.b += 1
                        base.color.b %= 256
                    if vars['action'] == 6:
                        base.color.opacity += 1
                        base.color.opacity %= 256
                    if vars['action'] == 7: base.shapes[0] = 1
                    if vars['action'] == 8: base.shapes[1] = 1
                    if vars['action'] == 9: base.shapes[2] = 1
                    if vars['action'] == 10: 
                        vars['opacity'] += 1
                        vars['opacity'] %= 256
                    if vars['action'] == 11:
                        base.angle += 1
                        base.angle %= 360

                if event.button == 5:#down
                    if vars['action'] == 0: base.omega -= 0.1
                    if vars['action'] == 1:
                        if base.w > 1 and base.h > 0:
                            base.w -= 1
                            base.h -= 1
                    if vars['action'] == 2:
                        if base.r > 1:
                            base.r -= 1
                    if vars['action'] == 3:
                        base.color.r -= 1
                        base.color.r %= 256
                    if vars['action'] == 4:
                        base.color.g -= 1
                        base.color.g %= 256
                    if vars['action'] == 5:
                        base.color.b -= 1
                        base.color.b %= 256
                    if vars['action'] == 6:
                        base.color.opacity -= 1
                        base.color.opacity %= 256            
                    if vars['action'] == 7: base.shapes[0] = 0
                    if vars['action'] == 8: base.shapes[1] = 0
                    if vars['action'] == 9: base.shapes[2] = 0
                    if vars['action'] == 10:
                        vars['opacity'] -= 1
                        vars['opacity'] %= 256
                    if vars['action'] == 11:
                        base.angle -= 1
                        base.angle %= 360

    if vars["crease"] != 0 and vars["performance"] == 1:
        if vars['action'] == 0: base.omega += 0.1 * vars["crease"]
        if vars['action'] == 1:
            base.w += 1 * vars["crease"]
            base.h += 1 * vars["crease"]
            if not base.w:
                base.w = 1
                base.h = 1
        if vars['action'] == 2:
            base.r += 1 * vars["crease"]
            if not base.r:
                base.r = 1
        if vars['action'] == 3:
            base.color.r += 1 * vars["crease"]
            base.color.r %= 256
        if vars['action'] == 4:
            base.color.g += 1 * vars["crease"]
            base.color.g %= 256
        if vars['action'] == 5:
            base.color.b += 1 * vars["crease"]
            base.color.b %= 256
        if vars['action'] == 6:
            base.color.opacity += 1 * vars["crease"]
            base.color.opacity %= 256
        if vars['action'] == 7:
            if base.shapes[0]:
                base.shapes[0] = 0
            else:
                base.shapes[0] =  1
        if vars['action'] == 8:
            if base.shapes[1]:
                base.shapes[1] = 0
            else:
                base.shapes[1] =  1 
        if vars['action'] == 9:
            if base.shapes[2]:
                base.shapes[2] = 0
            else:
                base.shapes[2] =  1
        if vars['action'] == 10: 
            vars['opacity'] += 1 * vars["crease"]
            vars['opacity'] %= 256
        if vars['action'] == 11:
            base.angle += 1 * vars["crease"]
            base.angle %= 360



    if vars["playmusic"] == -1:
        pygame.mixer.music.stop()
    else:
        if not pygame.mixer.music.get_busy():
            if vars["musicnumber"] > len(zenék)-1:
                vars["musicnumber"] = 0
            pygame.mixer.music.load(zenék[vars["musicnumber"]])
            pygame.mixer.music.play()
            vars["musicnumber"] += 1



    #background
    overlay.fill((170, 220, 255, vars['opacity']))
    screen.blit(overlay, (0, 0))


    #draw layer
    if vars["central"] == 0:
        for s in spinners:
            if vars["pause"] == -1:
                s.update()
            if vars["centerless"] == 1:
                s.drawcenterless(screen, sw, sh)
            else:
                s.draw(screen, sw, sh)
            s.interaction(event)
    elif vars["central"] == 1:
        for s in spinners:
            if spinners.index(s) == 0:
                if vars["pause"] == -1:
                    s.update()
                if vars["centerless"] == 1:
                    s.drawcenterless(screen, sw, sh)
                else:
                    s.draw(screen, sw, sh)
                s.interaction(event)
            else:
                s.ox = spinners[0].x
                s.oy = spinners[0].y
                if vars["pause"] == -1:
                    s.update()
                if vars["centerless"] == 1:
                    s.drawcenterless(screen, sw, sh)
                else:
                    s.draw(screen, sw, sh)
                s.interaction(event)
    else:
        for s in spinners:
            if spinners.index(s) == 0:
                if vars["pause"] == -1:
                    s.update()
                if vars["centerless"] == 1:
                    s.drawcenterless(screen, sw, sh)
                else:
                    s.draw(screen, sw, sh)
                s.interaction(event)
            else:
                s.ox = spinners[spinners.index(s)-1].x
                s.oy = spinners[spinners.index(s)-1].y
                if vars["pause"] == -1:
                    s.update()
                if vars["centerless"] == 1:
                    s.drawcenterless(screen, sw, sh)
                else:
                    s.draw(screen, sw, sh)
                s.interaction(event)

    #ui layer
    if vars["leaving"] == 1:
        pygame.draw.rect(screen,(200,200,200),(50,50,400,300))
        pygame.draw.rect(screen,(0,0,0),(50,50,400,300),5)
        screen.blit(font.render(nyelv.leaving[0],True,(0,0,0)),(60,60))
        screen.blit(images["checkmark"],(100,250))
        screen.blit(images["x"],(350,250))

    screen.blit(images["performance"], (0,0))
    if vars["performance"] == 1:
        if vars["developer ui"] == 1:
            pygame.draw.rect(screen,(200,200,200),(50,50,400,300))
            pygame.draw.rect(screen,(0,0,0),(50,50,400,300),5)
            pygame.draw.rect(screen,(200,200,200),(50,50,400,300))
            pygame.draw.rect(screen,(0,0,0),(50,50,400,300),5)
            screen.blit(font.render(nyelv.developer[0],True,(0,0,0)),(60,60))
            screen.blit(font.render(nyelv.developer[1],True,(0,0,0)),(60,90))
            screen.blit(font.render(nyelv.developer[2],True,(0,0,0)),(60,120))
            screen.blit(font.render(nyelv.developer[3],True,(0,0,0)),(60,150))
            screen.blit(font.render(nyelv.developer[4],True,(0,0,0)),(60,180))
            screen.blit(font.render(nyelv.developer[5],True,(0,0,0)),(60,210))
            screen.blit(font.render(nyelv.developer[6],True,(0,0,0)),(60,240))
            screen.blit(font.render(nyelv.developer[7],True,(0,0,0)),(60,270))
            screen.blit(font.render(nyelv.developer[8],True,(0,0,0)),(60,300))

        if vars["trashing"] == 1:
            pygame.draw.rect(screen,(200,200,200),(50,50,400,300))
            pygame.draw.rect(screen,(0,0,0),(50,50,400,300),5)
            screen.blit(font.render(nyelv.trashing[0],True,(0,0,0)),(60,60))
            screen.blit(images["checkmark"],(100,250))
            screen.blit(images["x"],(350,250))

        if vars["importing"] == 1:
            pygame.draw.rect(screen,(200,200,200),(50,50,400,300))
            pygame.draw.rect(screen,(0,0,0),(50,50,400,300),5)
            pygame.draw.rect(screen,(0,0,0),(50,275,400,75),5)
            screen.blit(font.render(nyelv.savings[0],True,(0,0,0)),(60,285))#
            screen.blit(font.render(vars["selected file"],True,(0,0,0)),(60,315))
            screen.blit(images["increase"],(390,60))
            screen.blit(images["decrease"],(390,110))
            pygame.draw.rect(screen,(0,0,0),(390,165,50,50),5)
            screen.blit(font.render("OK",True,(0,0,0)),(400,180))
            i = 0
            for f in os.listdir("saves"):
                if vars["minimum show"] <= i and (60+(i-vars["minimum show"])*25) < 250:
                    screen.blit(font.render(f,True,(0,0,0)),(60,60+(i-vars["minimum show"])*25))
                i += 1

        if vars["saving"] == 1:
            pygame.draw.rect(screen,(200,200,200),(50,50,400,175))
            pygame.draw.rect(screen,(0,0,0),(50,50,400,175),5)
            screen.blit(font.render(nyelv.savings[1],True,(0,0,0)),(60,60))
            pygame.draw.rect(screen,(0,0,0),(60,100,380,50),5)
            screen.blit(font.render(vars["selected file"],True,(0,0,0)),(70,115))
            pygame.draw.rect(screen,(0,0,0),(390,165,50,50),5)
            screen.blit(font.render("OK",True,(0,0,0)),(400,180))


        if  vars["show frames"] == 1:
            pygame.draw.rect(screen,(200,200,200),(-5,sh-150,490,155))
            pygame.draw.rect(screen,(0,0,0),(-5,sh-150,490,155),5)

            if vars["settings"] == 1:
                pygame.draw.rect(screen,(200,200,200),(sw-190,100,125,345))
                pygame.draw.rect(screen,(0,0,0),(sw-190,100,125,345),5)

        screen.blit(images["increase"],(5,sh-115))
        screen.blit(images["red"],(65,sh-115))
        screen.blit(images["green"],(125,sh-115))
        screen.blit(images["blue"],(185,sh-115))
        screen.blit(images["rectangle"],(245,sh-115))
        screen.blit(images["circle"],(305,sh-115))
        screen.blit(images["line"],(365,sh-115))
        if base.shapes[0]:
            overlay2 = pygame.Surface((25,25), pygame.SRCALPHA)
            overlay2.fill((base.color.r, base.color.g, base.color.b, base.color.opacity))
            screen.blit(overlay2, (450, sh-90))
        if base.shapes[1]:
            overlay2 = pygame.Surface((25,25), pygame.SRCALPHA)
            pygame.draw.circle(overlay2, (base.color.r, base.color.g, base.color.b, base.color.opacity), (12.5,12.5), 12.5)
            screen.blit(overlay2, (425, sh-115))
        if base.shapes[2]:
            pygame.draw.line(screen, (base.color.r, base.color.g, base.color.b, base.color.opacity), (425, sh-70), (475, sh-115), 5)

        screen.blit(images["decrease"],(5,sh-55))
        screen.blit(images["speed"],(65,sh-55))
        screen.blit(images["size"],(125,sh-55))
        screen.blit(images["distance"],(185,sh-55))
        screen.blit(images["opacity"],(245,sh-55))
        screen.blit(images["backgroundopacity"],(305,sh-55))
        screen.blit(images["rotate"],(365,sh-55))
        screen.blit(images["reset"],(425,sh-55))


        screen.blit(images["trash"], (sw-55,5))
        screen.blit(images["settings"], (sw-55,165))
        screen.blit(images["add"], (sw-55,sh-115))
        screen.blit(images["remove"], (sw-55,sh-55))
        #screen.blit(images["checkmark"], (sw-110,5))
        #screen.blit(images["x"], (sw-165,5))

        if vars["settings"] == 1:
            screen.blit(images["save"], (sw-180,110))
            if vars["centerless"] == 1:
                screen.blit(images["dontshow"], (sw-180,165))
            else:
                screen.blit(images["show"], (sw-180,165))
            if vars["playmusic"] == 1:
                screen.blit(images["musicplaying"], (sw-180,220))
            else:
                screen.blit(images["mute"], (sw-180,220))
            if vars["central"] == 0:
                screen.blit(images["monocentral"],(sw-180,275))
            if vars["central"] == 1:
                screen.blit(images["dicentral"],(sw-180,275))
            if vars["central"] == 2:
                screen.blit(images["policentral"],(sw-180,275))
            if vars["show frames"] == 1:
                screen.blit(images["framedui"], (sw-180,330))
            else:
                screen.blit(images["unframedui"], (sw-180,330))
            screen.blit(images["heart"], (sw-180,385))

            screen.blit(images["import"], (sw-125,110))
            if vars["erase"] == 1:
                pygame.draw.rect(screen,(255,0,0),(sw-125,165,50,50))
            screen.blit(images["eraser"], (sw-125,165)) 
            if vars["pause"] == -1:
                screen.blit(images["play"], (sw-125,220))
            else:
                screen.blit(images["stop"], (sw-125,220))
            screen.blit(images["book"], (sw-125,275))
            screen.blit(images["info"], (sw-125,330))
            screen.blit(images["exit"], (sw-125,385))

        screen.blit(font.render(f"{textgenforaction(nyelv.variables,base,vars['opacity'])[vars['action']]}",True,(0,0,0)),(10,sh-140))
        if vars["info"] == 1:
            screen.blit(font.render(f"{math.floor(clock.get_fps()*10)/10} fps",True,(0,0,0)),(400,sh-140))

    pygame.display.flip()
    clock.tick(60)
