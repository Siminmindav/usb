def ui1(overlay, screen, spinners, event, pygame, images, font, nyelv, base, sh, sw, textgenforaction, math, clock, os):



    #background
    overlay.fill((170, 220, 255, vars['opacity']))
    screen.blit(overlay, (0, 0))


    #draw layer
    if vars["central"] == 0:
        for s in spinners:
            if vars["pause"] == -1:
                s.update()
            if vars["centerless"] == 1:
                s.drawcenterless(screen)
            else:
                s.draw(screen)
            s.interaction(event)
    elif vars["central"] == 1:
        for s in spinners:
            if spinners.index(s) == 0:
                if vars["pause"] == -1:
                    s.update()
                if vars["centerless"] == 1:
                    s.drawcenterless(screen)
                else:
                    s.draw(screen)
                s.interaction(event)
            else:
                s.ox = spinners[0].x
                s.oy = spinners[0].y
                if vars["pause"] == -1:
                    s.update()
                if vars["centerless"] == 1:
                    s.drawcenterless(screen)
                else:
                    s.draw(screen)
                s.interaction(event)
    else:
        for s in spinners:
            if spinners.index(s) == 0:
                if vars["pause"] == -1:
                    s.update()
                if vars["centerless"] == 1:
                    s.drawcenterless(screen)
                else:
                    s.draw(screen)
                s.interaction(event)
            else:
                s.ox = spinners[spinners.index(s)-1].x
                s.oy = spinners[spinners.index(s)-1].y
                if vars["pause"] == -1:
                    s.update()
                if vars["centerless"] == 1:
                    s.drawcenterless(screen)
                else:
                    s.draw(screen)
                s.interaction(event)

    #ui layer
    screen.blit(images["performance"], (0,0))
    if vars["performance"] == 1:
        if vars["developer ui"] == 1:
            pygame.draw.rect(screen,(200,200,200),(50,50,400,300))
            pygame.draw.rect(screen,(0,0,0),(50,50,400,300),5)

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