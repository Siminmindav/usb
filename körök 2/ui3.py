import pygame
from functions import on, images

def ui3():
    screen2 =pygame.display.set_mode((400, 400))
    pygame.display.set_caption("settings")
    clock2 = pygame.time.Clock()
    run = True
    sure = 1
    font = pygame.font.SysFont("arial", 20)
    nyelv = ""

    while run:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("music/1.mp3")
            pygame.mixer.music.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if on(168, 353, 55, 35):
                    run = False
                elif on(20, 90, 150, 75):
                    nyelv = "english"
                    sure = 1
                elif on(230, 90, 150, 75):
                    nyelv = "español"
                    sure = 1
                elif on(20, 220, 150, 75):
                    nyelv = "magyar"
                    sure = 1
                elif on(230, 220, 150, 75):
                    nyelv = "русский"
                    sure = 1

        screen2.fill((0,0,0))

        if sure:
            pygame.draw.rect(screen2,(255,255,255),(168,353,55,35),5)
            screen2.blit(font.render(nyelv,True,(255,255,255)),(80,360))
            screen2.blit(font.render("OK",True,(255,255,255)),(180,360))

        screen2.blit(font.render("Válassz egy nyelvet! / Choose a language!",True,(255,255,255)),(10,10))
        screen2.blit(font.render("¡Eliges idioma! / Выберите язык!",True,(255,255,255)),(55,40))
        screen2.blit(images["english"],(20,90))
        screen2.blit(font.render("english",True,(255,255,255)),(65,160))
        screen2.blit(images["español"],(230,90))
        screen2.blit(font.render("español",True,(255,255,255)),(270,160))
        screen2.blit(images["magyar"],(20,220))
        screen2.blit(font.render("magyar",True,(255,255,255)),(60,290))
        screen2.blit(images["русский"],(230,220))
        screen2.blit(font.render("русский",True,(255,255,255)),(270,290))

        pygame.display.flip()
        clock2.tick(60)
    
    return nyelv