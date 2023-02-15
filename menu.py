import pygame
from ld_img import load_image


class Buttonify(pygame.sprite.Sprite):
    def __init__(self, img, coords, screen, button_group):
        super().__init__(button_group)
        self.image = load_image(img)
        self.image = pygame.transform.scale(self.image, (250, 70))
        self.rect = self.image.get_rect().move(*coords)
        screen.blit(self.image, coords)

    def check_click(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())


def start_screen(screen, WIDTH, HEIGHT, clock, FPS):
    intro_text = ['В ОДИНОЧКУ', 'ПО СЕТИ', 'НАСТРОЙКИ']
    button_group = pygame.sprite.Group()

    screen.fill((54, 54, 54))
    font = pygame.font.Font(None, 40)
    font_b_solo = font.render(intro_text[0], True, (255, 255, 255))
    font_b_duo = font.render(intro_text[1], True, (255, 255, 255))
    font_b_sett = font.render(intro_text[2], True, (255, 255, 255))

    b_solo = Buttonify('button.png', (525, 400), screen, button_group)
    b_duo = Buttonify('button.png', (525, 500), screen, button_group)
    b_settings = Buttonify('button.png', (525, 600), screen, button_group)
    screen.blit(font_b_solo, (555, 425))
    screen.blit(font_b_duo, (585, 525))
    screen.blit(font_b_sett, (560, 620))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for n, i in enumerate(button_group):
                    if i.check_click():
                        if n == 0:
                            return 'solo'
                        elif n == 1:
                            return 'duo'
                        elif n == 2:
                            return 'settings'
        pygame.display.flip()
        clock.tick(FPS)
