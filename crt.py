import pygame

def make_crt_overlay(width, height, line_gap=3, line_alpha=40, vignette_strength=160):
    """
    Returns a Surface to blit over the finished frame each tick.
    - line_gap:         pixels between each scanline
    - line_alpha:       0-255 opacity of scanlines (40 = subtle, 80 = heavy)
    - vignette_strength:0-255 darkness at screen edges
    """
    surf = pygame.Surface((width, height), pygame.SRCALPHA)

# ── scanlines ────────────────────────────────────────────────────────────
    for y in range(0, height, line_gap):
        pygame.draw.line(surf, (0, 0, 0, line_alpha), (0, y), (width, y))

    # ── vignette (dark oval gradient around the edges) ────────────────────
    vignette = pygame.Surface((width, height), pygame.SRCALPHA)
    cx, cy   = width // 2, height // 2
    steps    = 50
    for i in range(steps, 0, -1):
        t      = i / steps                        # 1.0 at edge, 0 at centre
        alpha  = int(vignette_strength * (t ** 2.2))
        colour = (0, 0, 0, alpha)
        rx     = int(cx * (1 - i / steps * 0.0) + cx * i / steps)
        ry     = int(cy * (1 - i / steps * 0.0) + cy * i / steps)
        rect   = pygame.Rect(0, 0, width - i * (width // steps),
                                   height - i * (height // steps))
        rect.center = (cx, cy)
        pygame.draw.ellipse(vignette, colour, rect, 2)

    surf.blit(vignette, (0, 0))
    return surf