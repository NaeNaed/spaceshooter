
# Imports
import pygame
import random

# Initialize game engine
pygame.init()


# Window
WIDTH = 1300
HEIGHT = 700
SIZE = (WIDTH, HEIGHT)
TITLE = "Chip Invaders"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)
screen_walls = pygame.Surface(SIZE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Fonts
FONT_SM = pygame.font.Font(None, 24)
FONT_MD = pygame.font.Font(None, 32)
FONT_LG = pygame.font.Font(None, 64)
FONT_XL = pygame.font.Font("assets/fonts/spaceone.ttf", 96)

# Images
background = pygame.image.load('assets/images/chaseisugly.png')
ship_img = pygame.image.load('assets/images/epic.png')
ship_img2 = pygame.image.load('assets/images/ouchB).png')
laser_img = pygame.image.load('assets/images/hola.png')
enemy_img = pygame.image.load('assets/images/god v2.png')
enemy2_img = pygame.image.load('assets/images/simoan.png')
bomb_img = pygame.image.load('assets/images/nohablasengels.png')
bomb2_img = pygame.image.load('assets/images/what.png')
god = pygame.image.load('assets/images/howdy.png')
madgod = pygame.image.load('assets/images/madhowdy.png')
bomb3_img = pygame.image.load('assets/images/elijah.png')
background1 = pygame.image.load('assets/images/godisgood.png')
coolgamer = pygame.image.load('assets/images/coolgamer.png')
sadgamer = pygame.image.load('assets/images/sadgamer.png')

screen_walls.blit(background, [0, 0])

# Sounds
ouch = pygame.mixer.Sound('assets/sounds/ouch.ogg')
boom = pygame.mixer.Sound('assets/sounds/boom.ogg')
bang = pygame.mixer.Sound('assets/sounds/bofa.ogg')

# Stages
START = 0
PLAYING = 1
WIN = 2
LOSE = 3
stage = START

# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image, image2):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(image)
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image2 = image2
        
        self.speed = 3
        self.shield = 5

    def move_left(self):
        self.rect.x -= self.speed
        
    def move_right(self):
        self.rect.x += self.speed

    def shoot(self):
        las = Laser(laser_img)
        
        las.rect.centerx = self.rect.centerx
        las.rect.centery = self.rect.top
        
        lasers.add(las)

        bang.play()
        
    def update(self, bombs):
        hit_list = pygame.sprite.spritecollide(self, bombs, True, pygame.sprite.collide_mask)

        for hit in hit_list:
            #oof.play()
            self.shield -= 1
            player.shield -= 1

        hit_list = pygame.sprite.spritecollide(self, gamers, False)
        if len(hit_list) > 0:
            self.shield = 0
            player.shield = 0

        hit_list = pygame.sprite.spritecollide(self, slims, False)
        if len(hit_list) > 0:
            self.shield = 0
            player.shield = 0

        hit_list = pygame.sprite.spritecollide(self, mobs, False)
        if len(hit_list) > 0:
            self.shield = 0
            player.shield = 0

        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.x > 1246:
            self.rect.x = 1246

        if self.shield == 2:
            self.image = self.image2

        if self.shield == 0:
            ouch.play()
            self.kill()
    
class Laser(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 6

    def update(self):
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()
    
class Mob(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(image)
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def drop_bomb(self):
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
    
    def update(self, lasers, player):
        hit_list = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)

        if len(hit_list) > 0:
            boom.play()
            player.score += 10
            self.kill()

class SlimMan(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(image)
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def drop_bomb(self):
        bomb = Bomb(bomb2_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
    
    def update(self, lasers, player):
        hit_list = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)

        if len(hit_list) > 0:
            boom.play()
            player.score += 15
            self.kill()

class God(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image, image2):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(image)
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.shield = 250
        self.image2 = image2

    def drop_bomb(self):
        bomb = Bomb(bomb3_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
        
    def update(self, lasers, player):
        hit_list = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)

        if len(hit_list) > 0:
            self.shield -= 1

        if self.shield == 125:
            self.image = self.image2

        if self.shield == 0:
            boom.play()
            player.score += 1000000
            self.kill()
            
class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image):

        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 6

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > 700:
            self.kill()
        
class Fleet:

    def __init__(self, mobs, slims, gamers):
        self.mobs = mobs
        self.slims = slims
        self.gamers = gamers
        self.bomb_rate = 10
        self.speed = 1
        self.moving_right = True

    def move(self):
        reverse = False

        if self.moving_right:
            for m in mobs:
                m.rect.x += self.speed
                if m.rect.right >= WIDTH:
                    reverse = True
            for s in slims:
                s.rect.x += self.speed
                if s.rect.right >= WIDTH:
                    reverse = True
            for g in gamers:
                g.rect.x += self.speed
                if g.rect.right >= WIDTH:
                    reverse = True
                    
        else:
            for m in mobs:
                m.rect.x -= self.speed
                if m.rect.left <= 0:
                    reverse = True
            for s in slims:
                s.rect.x -= self.speed
                if s.rect.left <= 0:
                    reverse = True
            for g in gamers:
                g.rect.x -= self.speed
                if g.rect.left <= 0:
                    reverse = True

        if reverse:
            self.moving_right = not self.moving_right
            for m in mobs:
                m.rect.y += 32
            for s in slims:
                s.rect.y += 32
            for g in gamers:
                g.rect.y += 32

    def choose_bomber(self):
        rand = random.randrange(0, self.bomb_rate)
        all_mobs = mobs.sprites() or slims.sprites() or gamers.sprites()
        
        if len(all_mobs) > 0 and rand == 0:
            return random.choice(all_mobs)
        else:
            return None
    
    def update(self):
        self.move()

        bomber = self.choose_bomber()
        if bomber != None:
            bomber.drop_bomb()
    
def setup():
    global ship, player, mobs, slims, gamers, fleet, lasers, bombs, mob1, mob2, mob3, mob4, mob5, mob6, mob7, mob8, mob9, mob10, mob11, mob12, mob13, mob14, mob15, mob16, mob17, mob18, mob19, mob20, mob21, mob22, mob23, mob24, mob25, mob26, mob27, mob28, mob29, mob30, mob31, mob32, slim1, slim2, slim3, slim4, slim5, slim6, slim7, slim8, slim9, slim10, slim11, slim12, slim13, slim14, slim15, slim16, slim17, slim18, slim19, slim20, slim21, slim22, slim23, slim24, slim25, slim26, slim27, slim28, slim29, slim30, slim31, slim32, gamer1

    ship = Ship(634, 616, ship_img, ship_img2)
    mob1 = Mob(634, 96, enemy_img)
    mob2 = Mob(559, 96, enemy_img)
    mob3 = Mob(484, 96, enemy_img)
    mob4 = Mob(409, 96, enemy_img)
    mob5 = Mob(334, 96, enemy_img)
    mob6 = Mob(259, 96, enemy_img)
    mob7 = Mob(184, 96, enemy_img)
    mob8 = Mob(109, 96, enemy_img)
    mob9 = Mob(709, 96, enemy_img)
    mob10 = Mob(784, 96, enemy_img)
    mob11 = Mob(859, 96, enemy_img)
    mob12 = Mob(934, 96, enemy_img)
    mob13 = Mob(1009, 96, enemy_img)
    mob14 = Mob(1084, 96, enemy_img)
    mob15 = Mob(1159, 96, enemy_img)
    mob16 = Mob(1234, 96, enemy_img)
    mob17 = Mob(634, 24, enemy_img)
    mob18 = Mob(559, 24, enemy_img)
    mob19 = Mob(484, 24, enemy_img)
    mob20 = Mob(409, 24, enemy_img)
    mob21 = Mob(334, 24, enemy_img)
    mob22 = Mob(259, 24, enemy_img)
    mob23 = Mob(184, 24, enemy_img)
    mob24 = Mob(109, 24, enemy_img)
    mob25 = Mob(709, 24, enemy_img)
    mob26 = Mob(784, 24, enemy_img)
    mob27 = Mob(859, 24, enemy_img)
    mob28 = Mob(934, 24, enemy_img)
    mob29 = Mob(1009, 24, enemy_img)
    mob30 = Mob(1084, 24, enemy_img)
    mob31 = Mob(1159, 24, enemy_img)
    mob32 = Mob(1234, 24, enemy_img)
    slim1 = SlimMan(650, -364, enemy2_img)
    slim2 = SlimMan(575, -364, enemy2_img)
    slim3 = SlimMan(500, -364, enemy2_img)
    slim4 = SlimMan(425, -364, enemy2_img)
    slim5 = SlimMan(350, -364, enemy2_img)
    slim6 = SlimMan(275, -364, enemy2_img)
    slim7 = SlimMan(725, -364, enemy2_img)
    slim8 = SlimMan(800, -364, enemy2_img)
    slim9 = SlimMan(875, -364, enemy2_img)
    slim10 = SlimMan(950, -364, enemy2_img)
    slim11 = SlimMan(1025, -364, enemy2_img)
    slim12 = SlimMan(1100, -364, enemy2_img)
    slim13 = SlimMan(1175, -364, enemy2_img)
    slim14 = SlimMan(200, -364, enemy2_img)
    slim15 = SlimMan(50, -364, enemy2_img)
    slim16 = SlimMan(125, -364, enemy2_img)
    slim17 = SlimMan(650, -300, enemy2_img)
    slim18 = SlimMan(575, -300, enemy2_img)
    slim19 = SlimMan(500, -300, enemy2_img)
    slim20 = SlimMan(425, -300, enemy2_img)
    slim21 = SlimMan(350, -300, enemy2_img)
    slim22 = SlimMan(275, -300, enemy2_img)
    slim23 = SlimMan(200, -300, enemy2_img)
    slim24 = SlimMan(125, -300, enemy2_img)
    slim25 = SlimMan(50, -300, enemy2_img)
    slim26 = SlimMan(725, -300, enemy2_img)
    slim27 = SlimMan(1175, -300, enemy2_img)
    slim28 = SlimMan(800, -300, enemy2_img)
    slim29 = SlimMan(875, -300, enemy2_img)
    slim30 = SlimMan(950, -300, enemy2_img)
    slim31 = SlimMan(1025, -300, enemy2_img)
    slim32 = SlimMan(1100, -300, enemy2_img)
    gamer1 = God(450, -790, god, madgod)

    # Make sprite groups
    player = pygame.sprite.Group()
    player.add(ship)
    player.score = 0
    player.shield = 5

    lasers = pygame.sprite.Group()

    mobs = pygame.sprite.Group()
    mobs.add(mob1, mob2, mob3, mob4, mob5, mob6, mob7, mob8, mob9, mob10, mob11, mob12, mob13, mob14, mob15, mob16,
             mob17, mob18, mob19, mob20, mob21, mob22, mob23, mob24, mob25, mob26, mob27, mob28, mob29, mob30, mob31, mob32)
    
    slims = pygame.sprite.Group()
    slims.add(slim1, slim2, slim3, slim4, slim5, slim6, slim7, slim8, slim9, slim10, slim11, slim12, slim13, slim14, slim15, slim16,
              slim17, slim18, slim19, slim20, slim21, slim22, slim23, slim24, slim25, slim26, slim27, slim28, slim29, slim30, slim31, slim32)

    gamers = pygame.sprite.Group()
    gamers.add(gamer1)
    
    bombs = pygame.sprite.Group()

# Make game objects
setup()

# Game helper functions
def soundfx():
    if stage == START:
        startmusic = pygame.mixer.music.load('assets/sounds/vietnam.ogg')
    elif stage == PLAYING:
        playingmusic = pygame.mixer.music.load('assets/sounds/when.ogg')
    elif stage == WIN:
        winmusic = pygame.mixer.music.load('assets/sounds/gamersound.ogg')
    elif stage == LOSE:
        losemusic = pygame.mixer.music.load('assets/sounds/sadgamersound.ogg')


    pygame.mixer.music.play(-1)
        
def show_title_screen():
    title_text = FONT_XL.render("Chip Invaders!", 1, WHITE)
    screen.blit(background1, [0, 0])
    screen.blit(title_text, [325, 204])

def show_stats(player):
    score_text = FONT_MD.render(str(player.score), 1, WHITE)
    screen.blit(score_text, [32, 32])
    
    shield_text = FONT_MD.render(str(player.shield), 2, WHITE)
    screen.blit(shield_text, [32, 64])

def win_screen():
    title_text = FONT_XL.render("Good Job Gamer Deafeating", 1, WHITE)
    other_text = FONT_XL.render(" the Hawke!!! B)", 1, WHITE)
    more_text = FONT_XL.render("LShift to play again", 1, WHITE)
    screen.blit(coolgamer, [0,0])
    screen.blit(title_text, [25, 204])
    screen.blit(other_text, [200, 304])
    screen.blit(more_text, [250, 404])

def lose_screen():
    title_text = FONT_XL.render("sad gamer moment", 1, WHITE)
    other_text = FONT_XL.render("LShift to play again", 1, WHITE)
    screen.blit(sadgamer, [0,0])
    screen.blit(title_text, [200, 204])
    screen.blit(other_text, [165, 304])
    
# Make fleet
fleet = Fleet(mobs, slims, gamers)

# Game loop
soundfx()

done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                    setup()
                    stage = PLAYING
                    soundfx()
            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                    ship.shoot()

    if stage == PLAYING:
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            ship.move_left()
        elif pressed[pygame.K_RIGHT]:
            ship.move_right()

    if stage == WIN:
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LSHIFT]:
            stage = START

    if stage == LOSE:
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LSHIFT]:
            stage = START
            
    
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        if ship.shield == 0:
            stage = LOSE
            soundfx()
        player.update(bombs)
        lasers.update()
        mobs.update(lasers, player)
        slims.update(lasers, player)
        gamers.update(lasers, player)
        bombs.update()
        fleet.update()
        if len(mobs) == 0 and len(slims) == 0 and len(gamers) == 0:
            stage = WIN
            soundfx()
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.blit(screen_walls, [0, 0])
    lasers.draw(screen)
    bombs.draw(screen)
    player.draw(screen)
    mobs.draw(screen)
    slims.draw(screen)
    gamers.draw(screen)
    show_stats(player)

    if stage == START:
        show_title_screen()

    if stage == WIN:
        win_screen()

    if stage == LOSE:
        lose_screen()
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
