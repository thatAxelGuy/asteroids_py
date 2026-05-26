import sys

import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from crt import make_crt_overlay

# ── Score Renderer ────────────────────────────────────────────────
def make_score_font(size=26):
    for name in ("Courier New", "Courier", "monospace"):
        font = pygame.font.SysFont(name, size, bold=True)
        if font:
            return font
    return pygame.font.Font(None, size)   # fallback

def draw_score(screen, font, score):
    label   = "SCORE"
    value   = f"{score:06d}"            # zero-padded 6-digit number
    spacing = 3                          # extra px between each character

    # Build surfaces for label and value separately so we can colour them
    label_surf = render_spaced(font, label, spacing, (0, 180, 80)) 
    value_surf = render_spaced(font, value, spacing, (0, 255, 115))   

    pad   = 18                           # distance from screen edge
    gap   = 8                            # gap between SCORE and number
    total_w = max(label_surf.get_width(), value_surf.get_width())
    x = SCREEN_WIDTH - pad - total_w

    # Stack label above value
    screen.blit(label_surf, (x + total_w - label_surf.get_width(), pad))
    screen.blit(value_surf, (x + total_w - value_surf.get_width(), pad + font.get_height() + gap))

def render_spaced(font, text, extra_px, colour):
    char_surfs = [font.render(ch, True, colour) for ch in text]
    ch_h = max(s.get_height() for s in char_surfs)
    total_w = sum(s.get_width() for s in char_surfs) + extra_px * (len(char_surfs) - 1)
    surf = pygame.Surface((total_w, ch_h), pygame.SRCALPHA)
    x = 0
    for s in char_surfs:
        surf.blit(s, (x, 0))
        x += s.get_width() + extra_px
    return surf

# ── MAIN ────────────────────────────────────────────────

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score = 0
    score_font = make_score_font(26)
    crt_overlay = make_crt_overlay(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroidfield = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids.copy():
            if asteroid.collision_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots.copy():
                if shot.collision_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    score += 50

        screen.fill(BACKGROUND_COLOR)

        for d in drawable:
            d.draw(screen)
        
        screen.blit(crt_overlay, (0, 0)) # draw CRT always on top
        
        draw_score(screen, score_font, score) # draw score on top without CRT
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        
       
        
        



if __name__ == "__main__":
    main()
