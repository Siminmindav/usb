import pygame, math, functions
from functions import onrect

class spinner:
    def __init__(self,ox, oy, ow, oh, x, y, w, h, color, angle, omega,r, shapes=[1,0,0,1]):
        self.move = 0
        self.shapes = shapes # rect, circle, line
        self.r = r
        self.ox = ox
        self.oy = oy
        self.ow = ow
        self.oh = oh
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = self.color(*color)
        self.angle = angle
        self.omega = omega

    class color:
        def __init__(self, r, g, b, opacity):
            self.r = r
            self.g = g
            self.b = b
            self.opacity = opacity

    def update(self):
        self.angle += self.omega
        self.angle %= 360
        self.x = self.ox + self.r * math.cos(math.radians(self.angle))
        self.y = self.oy + self.r * math.sin(math.radians(self.angle))
    
    def draw(self, screen, sw, sh):
        if self.shapes[3] and onrect(0, 0, sw + 100, sh + 100, self.ox, self.oy, self.ow, self.oh):
            pygame.draw.rect(screen,(255,0,0),(self.ox-self.ow/2, self.oy-self.oh/2,self.ow, self.oh))
        if onrect(0, 0, sw, sh, self.x, self.y, self.w, self.h):
            if self.shapes[0]:
                overlay = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
                overlay.fill((self.color.r, self.color.g, self.color.b, self.color.opacity))
                screen.blit(overlay, (self.x-self.w/2, self.y-self.h/2))
            if self.shapes[1]:
                overlay = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
                pygame.draw.circle(overlay, (self.color.r, self.color.g, self.color.b, self.color.opacity), (self.w//2, self.h//2), self.w//2)
                screen.blit(overlay, (self.x-self.w/2, self.y-self.h/2))
        if self.shapes[2]:
            pygame.draw.line(screen, (self.color.r, self.color.g, self.color.b, self.color.opacity), (self.ox, self.oy), (self.x, self.y), self.w)

    def drawcenterless(self, screen, sw, sh):
        if onrect(0, 0, sw , sh, self.x, self.y, self.w, self.h):
            if self.shapes[0]:
                overlay = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
                overlay.fill((self.color.r, self.color.g, self.color.b, self.color.opacity))
                screen.blit(overlay, (self.x-self.w/2, self.y-self.h/2))
            if self.shapes[1]:
                overlay = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
                pygame.draw.circle(overlay, (self.color.r, self.color.g, self.color.b, self.color.opacity), (self.w//2, self.h//2), self.w//2)
                screen.blit(overlay, (self.x-self.w/2, self.y-self.h/2))
        if self.shapes[2]:
            pygame.draw.line(screen, (self.color.r, self.color.g, self.color.b, self.color.opacity), (self.ox, self.oy), (self.x, self.y), self.w)

    def interaction(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if functions.on(self.ox-self.ow/2, self.oy-self.oh/2, self.ow, self.oh):
                self.move = 1
        if event.type == pygame.MOUSEBUTTONUP:
            self.move = 0
        if self.move:
            self.ox, self.oy = pygame.mouse.get_pos()

