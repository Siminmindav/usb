import pygame
from functions import on

def ui2(textlist):
    screen2 =pygame.display.set_mode((400, 400))
    pygame.display.set_caption("settings")
    clock2 = pygame.time.Clock()
    run = True
    fullscreen = 0
    sure = 0
    font = pygame.font.SysFont("arial", 20)
    text = ""

    

    while run:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("music/1.mp3")
            pygame.mixer.music.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if on(13, 114, 90, 35):
                    screen_width = 800
                    screen_height = 800
                    sure = 1
                    fullscreen = 0
                elif on(13, 164, 90, 35):
                    screen_width = 700
                    screen_height = 700
                    sure = 1
                    fullscreen = 0
                elif on(13, 214, 99, 35):
                    screen_width, screen_height = pygame.display.get_desktop_sizes()[0]
                    fullscreen = 1
                    sure = 1
                elif on(168, 353, 55, 35):
                    run = False

            if event.type == pygame.KEYDOWN:
                if on(243, 114, 90, 35):
                    if pygame.key.name(event.key) == "backspace":
                        if textlist[7][0]:
                            textlist[7][0] = textlist[7][0][:-1]
                    elif event.unicode.isdigit():
                        textlist[7][0] += event.unicode
                elif on(243, 164, 90, 35):
                    if pygame.key.name(event.key) == "backspace":
                        if textlist[9][0]:
                            textlist[9][0] = textlist[9][0][:-1]
                    elif event.unicode.isdigit():
                        textlist[9][0] += event.unicode
                if textlist[7][0] and textlist[9][0]:
                    sure = 1
                    fullscreen = 0
                    screen_width = int(textlist[7][0])
                    screen_height = int(textlist[9][0])

        screen2.fill((0, 0, 0))

        for t, p, r in textlist:
            if not r == 0:
                pygame.draw.rect(screen2,(255,255,255),r,5)
            screen2.blit(font.render(t,True,(255,255,255)),p)
        
        if sure:
            pygame.draw.rect(screen2,(255,255,255),(168,353,55,35),5)
            screen2.blit(font.render(f"{screen_width}x{screen_height}",True,(255,255,255)),(20,360))
            screen2.blit(font.render("OK",True,(255,255,255)),(180,360))
            
        pygame.display.flip()
        clock2.tick(60)
    
    return screen_width, screen_height, fullscreen