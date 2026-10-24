import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT =500,400
MOVEMENT_SPEED = 5
FONT_SIZE = 60

pygame.init()

bg_image = pygame.transform.scale(pygame.image.load("bg.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("Arial", FONT_SIZE)


class Sprite(pygame.sprite.Sprite):
    def __init__(self,color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.x_change = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.y_change = max(min(self.rect.y+  y_change, SCREEN_HEIGHT - self.rect.height), 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Petfood collection game")

all_sprites = pygame.sprite.Group()

Pet1 = Sprite(pygame.Color("brown"), 40, 40)
Pet1.rect.x = 30
Pet1.rect.y = 180

all_sprites.add(Pet1)

Petfood = Sprite(pygame.Color("orange"), 30, 30)
Petfood.rect.x = random.randint(100, SCREEN_WIDTH - Petfood.rect.width)
Petfood.rect.y = random.randint(0, SCREEN_HEIGHT - Petfood.rect.height)

all_sprites.add(Petfood)

running = True
food_collected = 0

Clock = pygame.time.Clock()

while not running:
    for event in pygame.get():
        if event.type == quit:
            running = False

        if not food_collected:
            keys = pygame.key.get_pressed()

            x_change = keys[pygame.k_RIGHT]- keys[pygame.K_LEFT]*MOVEMENT_SPEED
            y_change = keys[pygame.K_UP] - keys[pygame.K_DOWN]*MOVEMENT_SPEED

            Pet1.move(x_change, y_change)

        if Pet1.rect.colliderect(Petfood.rect):
            all_sprites.remove(Petfood)
            food_collected = True

        screen.blit(bg_image, (0, 0))
        all_sprites.draw(screen)

        if food_collected == True:
            text = font.render("food collected", pygame.Color("Black"))

            text_x = (SCREEN_WIDTH - text.get_width())//2
            text_y = (SCREEN_HEIGHT - text.get_height())//2

            screen.blit(text, (text_y, text_x))
        pygame.display.flip()
        Clock.tick(60)
pygame.quit()