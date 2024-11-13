import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        loca = (0, 0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = event.pos
                    if loca[0] <= mouse[0] <= loca[0]+32 and loca[1] <= mouse[1] <= loca[1] + 32:
                        random_x = random.randrange(1,20)
                        random_y = random.randint(1,16)
                        loca = (random_x * 32.25, random_y * 32.25)
            screen.fill("teal")
            size = 32
            for i in range(21):
                pygame.draw.line(screen, "black", (size, 0), (size, 512))
                pygame.draw.line(screen, "black", (0, size), (640, size))
                size += 32
            screen.blit(mole_image, mole_image.get_rect(topleft=loca))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
