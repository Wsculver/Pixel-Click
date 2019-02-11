import pygame
import random
import time
from os import path
import pathlib
import os, stat

pygame.init()

gamedata_folder = "./gamedata"
save_file = path.join(gamedata_folder, "savedata.txt")
unlocked_wall_skins = path.join(gamedata_folder, "wallskins.txt")
unlocked_spawner_skins = path.join(gamedata_folder, "spawnerskins.txt")
unlocked_dot_skins = path.join(gamedata_folder, "dotskins.txt")
unlocked_background_skins = path.join(gamedata_folder, "backgroundskins.txt")
images = "./images"
wall_imgs = path.join(images, "walls")
spawner_imgs = path.join(images, "spawners")
dot_imgs = path.join(images, "dots")
background_imgs = path.join(images, "backgrounds")
sounds = "./sounds"

if not os.path.exists(gamedata_folder):
    pathlib.Path(gamedata_folder).mkdir(parents=True, exist_ok=True)

if not os.path.exists(save_file):
    data = ['0\n', 'standard\n', 'blue\n', 'white\n', 'black\n', '0\n']
    with open(save_file, 'w') as file:
        file.writelines(data)
    os.chmod(save_file, stat.S_IREAD)

if not os.path.exists(unlocked_wall_skins):
    wall_skin_data = ['standard\n']
    with open(unlocked_wall_skins, 'w') as file:
        file.writelines(wall_skin_data)
    os.chmod(unlocked_wall_skins, stat.S_IREAD)

if not os.path.exists(unlocked_spawner_skins):
    spawner_skin_data = ['blue\n']
    with open(unlocked_spawner_skins, 'w') as file:
        file.writelines(spawner_skin_data)
    os.chmod(unlocked_spawner_skins, stat.S_IREAD)

if not os.path.exists(unlocked_dot_skins):
    dot_skin_data = ['white\n']
    with open(unlocked_dot_skins, 'w') as file:
        file.writelines(dot_skin_data)
    os.chmod(unlocked_dot_skins, stat.S_IREAD)

if not os.path.exists(unlocked_background_skins):
    background_skin_data = ['black\n']
    with open(unlocked_background_skins, 'w') as file:
        file.writelines(background_skin_data)
    os.chmod(unlocked_background_skins, stat.S_IREAD)

with open(save_file, 'r') as file:
    data = file.readlines()

with open(unlocked_wall_skins, 'r') as file:
    wall_skin_data = file.readlines()

with open(unlocked_spawner_skins, 'r') as file:
    spawner_skin_data = file.readlines()

with open(unlocked_dot_skins, 'r') as file:
    dot_skin_data = file.readlines()

with open(unlocked_background_skins, 'r') as file:
    background_skin_data = file.readlines()

wall_skin_dict = {"standard\n": [[path.join(wall_imgs, "standardh0.png"), path.join(wall_imgs, "standardh1.png"), path.join(wall_imgs, "standardh2.png"), path.join(wall_imgs, "standardh3.png"),
                                  path.join(wall_imgs, "standardh4.png"), path.join(wall_imgs, "standardh5.png")],
                                 [path.join(wall_imgs, "standardv0.png"), path.join(wall_imgs, "standardv1.png"), path.join(wall_imgs, "standardv2.png"), path.join(wall_imgs, "standardv3.png"),
                                  path.join(wall_imgs, "standardv4.png"), path.join(wall_imgs, "standardv5.png")]],
                  "neon\n": [[path.join(wall_imgs, "neonh0.png"), path.join(wall_imgs, "neonh1.png"), path.join(wall_imgs, "neonh2.png"), path.join(wall_imgs, "neonh3.png"),
                                  path.join(wall_imgs, "neonh4.png"), path.join(wall_imgs, "neonh5.png")],
                                 [path.join(wall_imgs, "neonv0.png"), path.join(wall_imgs, "neonv1.png"), path.join(wall_imgs, "neonv2.png"), path.join(wall_imgs, "neonv3.png"),
                                  path.join(wall_imgs, "neonv4.png"), path.join(wall_imgs, "neonv5.png")]],
                  "checkered\n": [[path.join(wall_imgs, "checkeredh0.png"), path.join(wall_imgs, "checkeredh1.png"), path.join(wall_imgs, "checkeredh2.png"), path.join(wall_imgs, "checkeredh3.png"),
                                  path.join(wall_imgs, "checkeredh4.png"), path.join(wall_imgs, "checkeredh5.png")],
                                 [path.join(wall_imgs, "checkeredv0.png"), path.join(wall_imgs, "checkeredv1.png"), path.join(wall_imgs, "checkeredv2.png"), path.join(wall_imgs, "checkeredv3.png"),
                                  path.join(wall_imgs, "checkeredv4.png"), path.join(wall_imgs, "checkeredv5.png")]],
                  "quilt\n": [[path.join(wall_imgs, "quilth0.png"), path.join(wall_imgs, "quilth1.png"), path.join(wall_imgs, "quilth2.png"), path.join(wall_imgs, "quilth3.png"),
                                  path.join(wall_imgs, "quilth4.png"), path.join(wall_imgs, "quilth5.png")],
                                 [path.join(wall_imgs, "quiltv0.png"), path.join(wall_imgs, "quiltv1.png"), path.join(wall_imgs, "quiltv2.png"), path.join(wall_imgs, "quiltv3.png"),
                                  path.join(wall_imgs, "quiltv4.png"), path.join(wall_imgs, "quiltv5.png")]],
                  "blue\n": [[path.join(wall_imgs, "blueh0.png"), path.join(wall_imgs, "blueh1.png"), path.join(wall_imgs, "blueh2.png"), path.join(wall_imgs, "blueh3.png"),
                                  path.join(wall_imgs, "blueh4.png"), path.join(wall_imgs, "blueh5.png")],
                                 [path.join(wall_imgs, "bluev0.png"), path.join(wall_imgs, "bluev1.png"), path.join(wall_imgs, "bluev2.png"), path.join(wall_imgs, "bluev3.png"),
                                  path.join(wall_imgs, "bluev4.png"), path.join(wall_imgs, "bluev5.png")]]}

spawner_skin_dict = {"blue\n": path.join(spawner_imgs, "bluespawner.png"), "green\n": path.join(spawner_imgs, "greenspawner.png"), "red\n": path.join(spawner_imgs, "redspawner.png"),
                     "white\n": path.join(spawner_imgs, "whitespawner.png"), "chessboard\n": path.join(spawner_imgs, "chessboardspawner.png")}

dot_skin_dict = {"white\n": path.join(dot_imgs, "whitedot.png"), "blue\n": path.join(dot_imgs, "bluedot.png"), "purple\n": path.join(dot_imgs, "purpledot.png"),
                 "smileyface\n": path.join(dot_imgs, "smileyfacedot.png"), "rainbow\n": path.join(dot_imgs, "rainbowdot.png")}

background_skin_dict = {"black\n": path.join(background_imgs, "blackbackground.png"), "gray\n": path.join(background_imgs, "graybackground.png"),
                        "sky\n": path.join(background_imgs, "skybackground.png"),
                        "space\n": path.join(background_imgs, "spacebackground.png"), "robot\n": path.join(background_imgs, "robotbackground.png")}

pygame.mixer.music.load(path.join(sounds, "Pixel-Drama.wav"))
pygame.mixer.music.set_volume(.4)
coin_pickup_sound = pygame.mixer.Sound(path.join(sounds, "coinpickup.wav"))
game_over_sound = pygame.mixer.Sound(path.join(sounds, "game-over.wav"))
click_sound = pygame.mixer.Sound(path.join(sounds, "click.wav"))
dot_kill_sound = pygame.mixer.Sound(path.join(sounds, "dot-kill.wav"))
damage_sound = pygame.mixer.Sound(path.join(sounds, "damage.wav"))
pygame.mixer.Sound.set_volume(damage_sound, .4)
purchase_skin_sound = pygame.mixer.Sound(path.join(sounds, "purchase-skin.wav"))
level_up_sound = pygame.mixer.Sound(path.join(sounds, "level-up.wav"))

FPS = 60

score_color = (255, 255, 255)
coin_color = (255, 219, 40)
coin_img = path.join(dot_imgs, "coin.png")
button_color = (35, 244, 255)
button_hover_color = (35, 185, 255)
button_text_color = (0, 0, 0)
skin_unlcok_popup_color = (235, 235, 235)

high_score = int(data[0])
wall_skin = data[1]
spawner_skin = data[2]
dot_skin = data[3]
background_skin = data[4]
coins = int(data[5])

infoObject = pygame.display.Info()
window = pygame.display.set_mode((int(infoObject.current_w/1.2), int(infoObject.current_h/1.2)), pygame.FULLSCREEN)
WIDTH = window.get_width()
HEIGHT = window.get_height()
width_multiplier = .000625*WIDTH
height_multiplier = .001111111111111*HEIGHT
pygame.display.set_caption("Pixel Click")
clock = pygame.time.Clock()
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000)

dot_x = WIDTH/2
dot_y = HEIGHT/2

yes_button_x = WIDTH/2 - (230*width_multiplier)
yes_button_y = HEIGHT/2 + (50*height_multiplier)
no_button_x = WIDTH/2 + (90*width_multiplier)
no_button_y = HEIGHT/2 + (50*height_multiplier)
preview_button_x = WIDTH/2 - (70*width_multiplier)
preview_button_y = HEIGHT/2 + (50*height_multiplier)

all_sprites = pygame.sprite.Group()
dot_list = pygame.sprite.Group()
coin_list = pygame.sprite.Group()
spawner_list = pygame.sprite.Group()
demo_sprites = pygame.sprite.Group()
demo_dot_list = pygame.sprite.Group()
demo_spawner_list = pygame.sprite.Group()

background_image = pygame.transform.scale(pygame.image.load(background_skin_dict[background_skin]).convert(), (WIDTH, HEIGHT))
background_rect = background_image.get_rect()
dot_image = pygame.transform.scale(pygame.image.load(dot_skin_dict[dot_skin]).convert(), (int(width_multiplier*10), int(height_multiplier*10)))
dot_rect = dot_image.get_rect()
spawner_image = pygame.transform.scale(pygame.image.load(spawner_skin_dict[spawner_skin]).convert(), (int(width_multiplier*50), int(height_multiplier*50)))
spawner_rect = spawner_image.get_rect()
h_wall_dimentions = (int(WIDTH - (width_multiplier*40)), int(height_multiplier * 20))
h_wall_images = [pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][0]), h_wall_dimentions),
                 pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][1]), h_wall_dimentions),
                 pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][2]), h_wall_dimentions),
                 pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][3]), h_wall_dimentions),
                 pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][4]), h_wall_dimentions),
                 pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][5]), h_wall_dimentions)]
v_wall_dimentions = (int(width_multiplier*20), int(HEIGHT - (height_multiplier*38)))
v_wall_images = [pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][0]), v_wall_dimentions),
                 pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][1]), v_wall_dimentions),
                 pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][2]), v_wall_dimentions),
                 pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][3]), v_wall_dimentions),
                 pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][4]), v_wall_dimentions),
                 pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][5]), v_wall_dimentions)]

coin_image = pygame.transform.scale(pygame.image.load(coin_img), (int(width_multiplier * 20), int(height_multiplier * 20)))
coin_rect = coin_image.get_rect()

i = 1
level_time = 0
game_time = 0
level = 1
score = 0

paused = False

class Spawner(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spawner_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        window.blit(self.image, self.rect)
        self.width = width_multiplier*50
        self.height = height_multiplier*50

    def update(self):
        if level >= 5:
            self.width += .01*width_multiplier * level
            self.height += .01*height_multiplier * level
            self.image = pygame.transform.scale(self.image, (int(self.width), int(self.height)))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 2, HEIGHT / 2)
            window.blit(self.image, self.rect)

class TopLeftCorner(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(spawner_image, (int(width_multiplier * 20), int(height_multiplier * 20)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        window.blit(self.image, self.rect)

class TopRightCorner(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(spawner_image, (int(width_multiplier * 20), int(height_multiplier * 20)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (WIDTH - (width_multiplier*20), 0)
        window.blit(self.image, self.rect)

class BottomLeftCorner(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(spawner_image, (int(width_multiplier * 20), int(height_multiplier * 20)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, HEIGHT - (height_multiplier*20))
        window.blit(self.image, self.rect)

class BottomRightCorner(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(spawner_image, (int(width_multiplier * 20), int(height_multiplier * 20)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (WIDTH - (width_multiplier * 20), HEIGHT - (height_multiplier * 20))
        window.blit(self.image, self.rect)

class TopWall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = h_wall_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, height_multiplier*10)
        window.blit(self.image, self.rect)
        self.damage_level = 0

    def damage(self):
        if self.damage_level == 0:
            self.image = h_wall_images[1]
        elif self.damage_level == 1:
            self.image = h_wall_images[2]
        elif self.damage_level == 2:
            self.image = h_wall_images[3]
        elif self.damage_level == 3:
            self.image = h_wall_images[4]
        elif self.damage_level == 4:
            self.image = h_wall_images[5]
        elif self.damage_level == 5:
            game_over()
        self.damage_level += 1

class BottomWall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = h_wall_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT-(height_multiplier*10))
        window.blit(self.image, self.rect)
        self.damage_level = 0

    def damage(self):
        if self.damage_level == 0:
            self.image = h_wall_images[1]
        elif self.damage_level == 1:
            self.image = h_wall_images[2]
        elif self.damage_level == 2:
            self.image = h_wall_images[3]
        elif self.damage_level == 3:
            self.image = h_wall_images[4]
        elif self.damage_level == 4:
            self.image = h_wall_images[5]
        elif self.damage_level == 5:
            game_over()
        self.damage_level += 1

class LeftWall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = v_wall_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (width_multiplier*10, HEIGHT/2)
        window.blit(self.image, self.rect)
        self.damage_level = 0

    def damage(self):
        if self.damage_level == 0:
            self.image = v_wall_images[1]
        elif self.damage_level == 1:
            self.image = v_wall_images[2]
        elif self.damage_level == 2:
            self.image = v_wall_images[3]
        elif self.damage_level == 3:
            self.image = v_wall_images[4]
        elif self.damage_level == 4:
            self.image = v_wall_images[5]
        elif self.damage_level == 5:
            game_over()
        self.damage_level += 1

class RightWall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = v_wall_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH-(width_multiplier*10), HEIGHT/2)
        window.blit(self.image, self.rect)
        self.damage_level = 0

    def damage(self):
        if self.damage_level == 0:
            self.image = v_wall_images[1]
        elif self.damage_level == 1:
            self.image = v_wall_images[2]
        elif self.damage_level == 2:
            self.image = v_wall_images[3]
        elif self.damage_level == 3:
            self.image = v_wall_images[4]
        elif self.damage_level == 4:
            self.image = v_wall_images[5]
        elif self.damage_level == 5:
            game_over()
        self.damage_level += 1

class DemoWall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(v_wall_images[0], (int(width_multiplier*20), int(height_multiplier*100)))
        self.rect = self.image.get_rect()
        self.rect.center = (width_multiplier*250, height_multiplier*740)
        window.blit(self.image, self.rect)
        self.damage_level = 0

    def damage(self):
        if self.damage_level == 0:
            self.image = pygame.transform.scale(v_wall_images[1], (int(width_multiplier*20), int(height_multiplier*100)))
        elif self.damage_level == 1:
            self.image = pygame.transform.scale(v_wall_images[2], (int(width_multiplier*20), int(height_multiplier*100)))
        elif self.damage_level == 2:
            self.image = pygame.transform.scale(v_wall_images[3], (int(width_multiplier*20), int(height_multiplier*100)))
        elif self.damage_level == 3:
            self.image = pygame.transform.scale(v_wall_images[4], (int(width_multiplier*20), int(height_multiplier*100)))
        elif self.damage_level == 4:
            self.image = pygame.transform.scale(v_wall_images[5], (int(width_multiplier*20), int(height_multiplier*100)))
        elif self.damage_level == 5:
            self.image = pygame.transform.scale(v_wall_images[0], (int(width_multiplier * 20), int(height_multiplier * 100)))
            self.damage_level = 0
        self.damage_level += 1

class DemoDot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = dot_image
        self.rect = self.image.get_rect()
        self.rect.center = (width_multiplier*550, height_multiplier*740)
        window.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= 2

class DemoSpawner(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spawner_image
        self.rect = self.image.get_rect()
        self.rect.center = (width_multiplier*550, height_multiplier*740)
        window.blit(self.image, self.rect)

class Dot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = width_multiplier*10
        self.height = height_multiplier*10
        self.buffer = width_multiplier*2
        self.image = dot_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        window.blit(self.image, self.rect)
        self.speed_x = random.uniform(width_multiplier, width_multiplier*2) if level < 3 else width_multiplier
        self.speed_y = random.uniform(height_multiplier, height_multiplier*2) if level < 3 else height_multiplier
        self.sign_x = 0
        self.sign_y = 0
        while self.sign_x == 0 and self.sign_y == 0:
            self.sign_x = random.randint(-1, 1)
            self.sign_y = random.randint(-1, 1)

    def update(self):
        if level <= 4:
            self.rect.x += self.sign_x * self.speed_x * level
            self.rect.y += self.sign_y * self.speed_y * level
        else:
            self.rect.x += self.sign_x * self.speed_x * 4
            self.rect.y += self.sign_y * self.speed_y * 4

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = width_multiplier*20
        self.height = height_multiplier*20
        self.buffer = width_multiplier*2
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speed_x = random.uniform(width_multiplier, width_multiplier*2) if level < 3 else width_multiplier
        self.speed_y = random.uniform(height_multiplier, height_multiplier*2) if level < 3 else height_multiplier
        self.sign_x = 0
        self.sign_y = 0
        while self.sign_x == 0 and self.sign_y == 0:
            self.sign_x = random.randint(-1, 1)
            self.sign_y = random.randint(-1, 1)

    def update(self):
        if level <= 4:
            self.rect.x += self.sign_x * self.speed_x * level
            self.rect.y += self.sign_y * self.speed_y * level
        else:
            self.rect.x += self.sign_x * self.speed_x * 4
            self.rect.y += self.sign_y * self.speed_y * 4

def write_text(text, font, font_size, color, position, x, y):
    text_surface = pygame.font.Font(font, int(height_multiplier*font_size)).render(text, True, color)
    text_surf, text_rect = text_surface, text_surface.get_rect()
    if position == "center":
        text_rect.center = (x, y)
    elif position == "topleft":
        text_rect.topleft = (x, y)
    elif position == "topright":
        text_rect.topright = (x, y)
    elif position == "bottomright":
        text_rect.bottomright = (x, y)
    elif position == "bottomleft":
        text_rect.bottomleft = (x, y)
    window.blit(text_surf, text_rect)

def game_over():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(game_over_sound)
    for sprite in all_sprites:
        sprite.kill()

    write_text("GAME OVER", "freesansbold.ttf", 150, (255, 0, 0), "center", WIDTH/2, HEIGHT/2 - (height_multiplier*250))
    pygame.display.update()

    time.sleep(2)

    write_text("Play Again?", "freesansbold.ttf", 150, coin_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier * 100))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play", button_text_color, WIDTH / 2 - (width_multiplier * 200), HEIGHT / 2 + (height_multiplier * 70), 150, 75, button_color, button_hover_color, game_loop)
        button("Menu", button_text_color, WIDTH / 2 + (width_multiplier * 80), HEIGHT / 2 + (height_multiplier * 70), 150, 75, button_color, button_hover_color, start_menu)

        pygame.display.update()

def dot_spawn():
    if random.randint(1, 50) == 1:
        coin = Coin()
        all_sprites.add(coin)
        coin_list.add(coin)
    else:
        dot = Dot()
        all_sprites.add(dot)
        dot_list.add(dot)

def button(text, text_color,  x, y, w, h, base_color, hover_color, action=None, action_args=None, text_size=30):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    w *= width_multiplier
    h *= height_multiplier

    if x + w > mouse_pos[0] > x and y + h > mouse_pos[1] > y:
        pygame.draw.rect(window, hover_color, (x, y, w, h))
        if click[0] == 1 and action is not None:
            time.sleep(.07)
            if action == skin_shop or action == skin_click or action == equip_skin or action == preview_skin:
                action(*action_args)
            else:
                if text == "Menu":
                    pygame.mixer.music.play(-1)
                action()
    else:
        pygame.draw.rect(window, base_color, (x, y, w, h))

    write_text(text, "freesansbold.ttf", int(height_multiplier*text_size), text_color, 'center', x + (w/2), y + (h/2))

def button_layout(active_text, active_location, click, skin_type, text1="", text2="", text3="", text4="", text5=""):
    text_location_dict = {text1: [70, 385], text2: [370, 385], text3: [670, 385], text4: [970, 385], text5: [1270, 385]}

    if click:
        for text in text_location_dict:
            if text != active_text:
                button(text, button_text_color, width_multiplier*text_location_dict[text][0], height_multiplier*text_location_dict[text][1], 250, 125, button_color, button_color)
            else:
                button(active_text, button_text_color, width_multiplier*active_location[0], height_multiplier*active_location[1], active_location[2], active_location[3], button_hover_color,
                       button_hover_color)
    else:
        for text in text_location_dict:
            if text != active_text:
                button(text, button_text_color, width_multiplier*text_location_dict[text][0], height_multiplier*text_location_dict[text][1], 250, 125, button_color, button_hover_color,
                       skin_click, (skin_type, (text.lower()).replace(" ", "")))
            else:
                button(active_text, button_text_color, width_multiplier*active_location[0], height_multiplier*active_location[1], active_location[2], active_location[3], button_hover_color,
                       button_hover_color)


def game_quit():
    os.chmod(save_file, stat.S_IWRITE)
    pygame.quit()
    quit()

def unpause():
    global paused
    pygame.mixer.music.unpause()
    paused = False

def pause():
    pygame.mixer.music.pause()
    write_text("Paused", "freesansbold.ttf", 150, score_color, 'center', WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", button_text_color, WIDTH/2 - (width_multiplier*200), HEIGHT/2 + (height_multiplier*70), 150, 75, button_color, button_hover_color, unpause)
        button("Menu", button_text_color, WIDTH/2 + (width_multiplier*80), HEIGHT/2 + (height_multiplier*70), 150, 75, button_color, button_hover_color, start_menu)

        pygame.display.update()

def intro():
    done = False
    y = 0
    n = -1
    while not done:
        clock.tick(FPS)

        keys = pygame.key.get_pressed()

        if 1 in keys:
            pygame.mixer.music.play(-1)
            start_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == CLOCKTICK:
                n += 1

        if n >= 4:
            done = True
            pygame.mixer.music.play(-1)
            start_menu()
        else:
            window.blit(background_image, background_rect)
            write_text("Pixel Click", "freesansbold.ttf", 150, score_color, 'center', WIDTH / 2, HEIGHT / 2)
            if n == 0:
                button("Play", button_text_color, WIDTH / 2 - (width_multiplier * 382), height_multiplier * 550, 350,
                       60, button_color, button_color)
            elif n == 1:
                button("Play", button_text_color, WIDTH / 2 - (width_multiplier * 382), height_multiplier * 550, 350,
                       60, button_color, button_color)
                button("Shop", button_text_color, WIDTH / 2 + (width_multiplier * 40), height_multiplier * 550, 350, 60,
                       button_color, button_color)
            elif n == 2:
                button("Play", button_text_color, WIDTH / 2 - (width_multiplier * 382), height_multiplier * 550, 350,
                       60, button_color, button_color)
                button("Shop", button_text_color, WIDTH / 2 + (width_multiplier * 40), height_multiplier * 550, 350, 60,
                       button_color, button_color)
                button("How To Play", button_text_color, WIDTH / 2 - (width_multiplier * 382), height_multiplier * 650,
                       350, 60, button_color, button_color)
            elif n == 3:
                button("Play", button_text_color, WIDTH / 2 - (width_multiplier * 382), height_multiplier * 550, 350,
                       60, button_color, button_color)
                button("Shop", button_text_color, WIDTH / 2 + (width_multiplier * 40), height_multiplier * 550, 350, 60,
                       button_color, button_color)
                button("How To Play", button_text_color, WIDTH / 2 - (width_multiplier * 382), height_multiplier * 650,
                       350, 60, button_color, button_color)
                button("Quit", button_text_color, WIDTH / 2 + (width_multiplier * 40), height_multiplier * 650, 350, 60,
                       button_color, button_color)
            window.blit(dot_image, (WIDTH / 4, y))
            window.blit(dot_image, (WIDTH - (WIDTH / 4), y - 100))
            window.blit(dot_image, (WIDTH / 2, y - 200))
            window.blit(dot_image, (WIDTH / 3, y - 300))
            window.blit(dot_image, (WIDTH - (WIDTH / 3), y - 400))
            window.blit(dot_image, (WIDTH / 6, y - 500))
            window.blit(dot_image, (WIDTH / 10, y - 600))
            window.blit(dot_image, (WIDTH - (WIDTH / 6), y - 150))
            window.blit(dot_image, (WIDTH - (WIDTH / 10), y - 250))
            window.blit(dot_image, (WIDTH - (WIDTH / 15), y - 350))

            window.blit(dot_image, (WIDTH / 4, y - 700))
            window.blit(dot_image, (WIDTH - (WIDTH / 4), y - 800))
            window.blit(dot_image, (WIDTH / 2, y - 900))
            window.blit(dot_image, (WIDTH / 3, y - 1000))
            window.blit(dot_image, (WIDTH - (WIDTH / 3), y - 1100))
            window.blit(dot_image, (WIDTH / 6, y - 1200))
            window.blit(dot_image, (WIDTH / 10, y - 1300))
            window.blit(dot_image, (WIDTH - (WIDTH / 6), y - 850))
            window.blit(dot_image, (WIDTH - (WIDTH / 10), y - 950))
            window.blit(dot_image, (WIDTH - (WIDTH / 15), y - 1050))

            window.blit(dot_image, (WIDTH / 4, y - 1400))
            window.blit(dot_image, (WIDTH - (WIDTH / 4), y - 1500))
            window.blit(dot_image, (WIDTH / 2, y - 1600))
            window.blit(dot_image, (WIDTH / 3, y - 1700))
            window.blit(dot_image, (WIDTH - (WIDTH / 3), y - 1800))
            window.blit(dot_image, (WIDTH / 6, y - 1900))
            window.blit(dot_image, (WIDTH / 10, y - 2000))
            window.blit(dot_image, (WIDTH - (WIDTH / 6), y - 1550))
            window.blit(dot_image, (WIDTH - (WIDTH / 10), y - 1650))
            window.blit(dot_image, (WIDTH - (WIDTH / 15), y - 1750))
            pygame.display.update()
            y += height_multiplier * 10
            if y >= HEIGHT+1200:
                y = 700

    pygame.display.update()

def start_menu():
    time.sleep(.15)
    y = 600

    for sprite in all_sprites:
        sprite.kill()

    create_basic_sprites()

    high_score = int(data[0])
    coins = int(data[5])

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.blit(background_image, background_rect)
        write_text("Pixel Click", "freesansbold.ttf", 150, score_color, 'center', WIDTH/2, HEIGHT/2)
        write_text(("Coins: %d" % coins), "freesansbold.ttf", 30, coin_color, "topleft", width_multiplier*25, (HEIGHT - (height_multiplier*52)))
        write_text(("High Score: %d" % high_score), "freesansbold.ttf", 30, score_color, "topright", (WIDTH - (width_multiplier*25)), (HEIGHT - (height_multiplier*52)))

        button("Play", button_text_color, WIDTH/2 - (width_multiplier*382), height_multiplier*550, 350, 60, button_color, button_hover_color, game_loop)
        button("How To Play", button_text_color, WIDTH/2 - (width_multiplier*382), height_multiplier*650, 350, 60, button_color, button_hover_color, how_to_play)
        button("Shop", button_text_color, WIDTH/2 + (width_multiplier*40), height_multiplier*550, 350, 60, button_color, button_hover_color, shop)
        button("Quit", button_text_color, WIDTH/2 + (width_multiplier*40), height_multiplier*650, 350, 60, button_color, button_hover_color, game_quit)

        all_sprites.update()
        all_sprites.draw(window)

        window.blit(dot_image, (WIDTH / 4, y))
        window.blit(dot_image, (WIDTH - (WIDTH / 4), y - 100))
        window.blit(dot_image, (WIDTH / 2, y - 200))
        window.blit(dot_image, (WIDTH / 3, y - 300))
        window.blit(dot_image, (WIDTH - (WIDTH / 3), y - 400))
        window.blit(dot_image, (WIDTH / 6, y - 500))
        window.blit(dot_image, (WIDTH / 10, y - 600))
        window.blit(dot_image, (WIDTH - (WIDTH / 6), y - 150))
        window.blit(dot_image, (WIDTH - (WIDTH / 10), y - 250))
        window.blit(dot_image, (WIDTH - (WIDTH / 15), y - 350))

        window.blit(dot_image, (WIDTH / 4, y - 700))
        window.blit(dot_image, (WIDTH - (WIDTH / 4), y - 800))
        window.blit(dot_image, (WIDTH / 2, y - 900))
        window.blit(dot_image, (WIDTH / 3, y - 1000))
        window.blit(dot_image, (WIDTH - (WIDTH / 3), y - 1100))
        window.blit(dot_image, (WIDTH / 6, y - 1200))
        window.blit(dot_image, (WIDTH / 10, y - 1300))
        window.blit(dot_image, (WIDTH - (WIDTH / 6), y - 850))
        window.blit(dot_image, (WIDTH - (WIDTH / 10), y - 950))
        window.blit(dot_image, (WIDTH - (WIDTH / 15), y - 1050))

        window.blit(dot_image, (WIDTH / 4, y - 1400))
        window.blit(dot_image, (WIDTH - (WIDTH / 4), y - 1500))
        window.blit(dot_image, (WIDTH / 2, y - 1600))
        window.blit(dot_image, (WIDTH / 3, y - 1700))
        window.blit(dot_image, (WIDTH - (WIDTH / 3), y - 1800))
        window.blit(dot_image, (WIDTH / 6, y - 1900))
        window.blit(dot_image, (WIDTH / 10, y - 2000))
        window.blit(dot_image, (WIDTH - (WIDTH / 6), y - 1550))
        window.blit(dot_image, (WIDTH - (WIDTH / 10), y - 1650))
        window.blit(dot_image, (WIDTH - (WIDTH / 15), y - 1750))
        pygame.display.update()
        y += height_multiplier * 10
        if y >= HEIGHT + 1200:
            y = 700

        pygame.display.update()

def how_to_play():
    demo_wall = DemoWall()
    demo_sprites.add(demo_wall)
    demo_dot = DemoDot()
    demo_sprites.add(demo_dot)
    demo_dot_list.add(demo_dot)
    demo_spawner = DemoSpawner()
    demo_spawner_list.add(demo_spawner)
    demo_spawner_list.update()
    create_basic_sprites()
    i = 1

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == CLOCKTICK:
                if i > 3:
                    demo_dot = DemoDot()
                    demo_sprites.add(demo_dot)
                    demo_dot_list.add(demo_dot)
                    i = 1
                i += 1

        for dot in demo_dot_list:
            if dot.rect.x < demo_wall.rect.x + 20:
                dot.kill()
                demo_wall.damage()

        window.blit(background_image, background_rect)
        write_text("How To Play", "freesansbold.ttf", 75, score_color, 'topleft', width_multiplier*25, height_multiplier*30)

        write_text("Key", "freesansbold.ttf", 40, score_color, 'topleft', width_multiplier*110, height_multiplier*130)
        window.blit(spawner_image, (width_multiplier * 160, height_multiplier * 190))
        write_text("Spawner: This spawns dots for you to destroy", "freesansbold.ttf", 20, score_color, 'topleft', width_multiplier*240, height_multiplier*205)
        window.blit(dot_image, (width_multiplier*180, height_multiplier* 265))
        write_text("Dot: This is what you are supposed to destroy", "freesansbold.ttf", 20, score_color, 'topleft', width_multiplier*240, height_multiplier*262)
        window.blit(coin_image, (width_multiplier * 175, height_multiplier * 305))
        write_text("Coin: This can be collected and used to unlock in game content", "freesansbold.ttf", 20, score_color, 'topleft', width_multiplier*240, height_multiplier*307)
        window.blit(pygame.transform.scale(h_wall_images[0], (int(width_multiplier*50), int(height_multiplier*20))), (width_multiplier * 160, height_multiplier * 350))
        write_text("Wall: These are the game boarders", "freesansbold.ttf", 20, score_color, 'topleft', width_multiplier*240, height_multiplier*352)

        write_text("How To Play", "freesansbold.ttf", 40, score_color, 'topleft', width_multiplier*110, height_multiplier*405)
        window.blit(dot_image, (width_multiplier*180, height_multiplier*465))
        write_text("Move your mouse and hover over the dots and coins to destroy them and add to your score (no clicking required)", "freesansbold.ttf", 20, score_color, 'topleft',
                   width_multiplier*240, height_multiplier*462)
        window.blit(dot_image, (width_multiplier*180, height_multiplier*505))
        write_text("The spawner spawns dots in random directions so be careful!", "freesansbold.ttf", 20, score_color, 'topleft', width_multiplier*240, height_multiplier*502)
        window.blit(dot_image, (width_multiplier*180, height_multiplier*545))
        write_text("Don't let the dots touch the walls or else they will take damage and eventually lead to a game over after 6 hits", "freesansbold.ttf", 20, score_color, 'topleft',
                   width_multiplier*240, height_multiplier*542)
        window.blit(dot_image, (width_multiplier * 180, height_multiplier * 585))
        write_text("As time goes on, the levels increase and the game gets harder so survive as long as you can", "freesansbold.ttf", 20, score_color, 'topleft',
                   width_multiplier*240, height_multiplier*582)

        write_text("Buttons", "freesansbold.ttf", 40, score_color, 'topleft', width_multiplier * 860, height_multiplier * 130)
        window.blit(dot_image, (width_multiplier * 930, height_multiplier * 190))
        write_text("Space/Escape: Pause", "freesansbold.ttf", 20, score_color, 'topleft', width_multiplier*990, height_multiplier*187)

        write_text("Tips", "freesansbold.ttf", 40, score_color, 'topleft', width_multiplier * 860, height_multiplier * 230)
        window.blit(dot_image, (width_multiplier * 930, height_multiplier * 290))
        write_text("Place your cursor ahead of where the dots are traveling", "freesansbold.ttf", 20, score_color, 'topleft', width_multiplier * 990, height_multiplier * 287)

        write_text("William's High Score", "freesansbold.ttf", 40, score_color, 'topleft', width_multiplier * 860, height_multiplier * 630)
        window.blit(dot_image, (width_multiplier * 930, height_multiplier * 690))
        write_text("287 (Can you beat it?)", "freesansbold.ttf", 30, score_color, 'topleft', width_multiplier * 990, height_multiplier * 682)

        write_text("Demo Of A Wall Taking Damage", "freesansbold.ttf", 40, score_color, 'topleft', width_multiplier*110, height_multiplier*630)

        button("Back", button_text_color, width_multiplier*25, (HEIGHT - (height_multiplier*75)), 100, 50, button_color, button_hover_color, start_menu)

        all_sprites.update()
        demo_sprites.update()
        demo_spawner_list.update()
        all_sprites.draw(window)
        demo_sprites.draw(window)
        demo_spawner_list.draw(window)
        pygame.display.update()

def shop():
    time.sleep(.15)
    create_basic_sprites()

    coins = int(data[5])

    shop_screen = True
    while shop_screen:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.blit(background_image, background_rect)
        write_text("Shop", "freesansbold.ttf", 75, score_color, 'topleft', width_multiplier*25, height_multiplier*20)
        write_text(("Coins: %d" % coins), "freesansbold.ttf", 30, coin_color, "topright", (WIDTH - (width_multiplier*25)), (HEIGHT - (height_multiplier*52)))

        button("Back", button_text_color, width_multiplier*25, (HEIGHT - (height_multiplier*75)), 100, 50, button_color, button_hover_color, start_menu)
        button("Wall Skins", button_text_color, width_multiplier*210, HEIGHT/2 - (height_multiplier*62), 250, 125, button_color, button_hover_color, skin_shop, 'w')
        button("Spawner Skins", button_text_color, width_multiplier*510, HEIGHT/2 - (height_multiplier*62), 250, 125, button_color, button_hover_color, skin_shop, 's')
        button("Dot Skins", button_text_color, width_multiplier*810, HEIGHT/2 - (height_multiplier*62), 250, 125, button_color, button_hover_color, skin_shop, 'd')
        button("Backgrounds", button_text_color, width_multiplier*1110, HEIGHT/2 - height_multiplier*62, 250, 125, button_color, button_hover_color, skin_shop, 'b')

        all_sprites.update()
        all_sprites.draw(window)
        pygame.display.update()

def skin_shop(skin_type):
    create_basic_sprites()

    coins = int(data[5])

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.blit(background_image, background_rect)
        write_text(("Coins: %d" % coins), "freesansbold.ttf", 30, coin_color, "topright", (WIDTH - (width_multiplier*25)), (HEIGHT - (height_multiplier*52)))

        button("Back", button_text_color, width_multiplier*25, (HEIGHT - (height_multiplier*75)), 100, 50, button_color, button_hover_color, shop)

        if skin_type == 'w':
            write_text("Wall Skins", "freesansbold.ttf", 75, score_color, 'topleft', width_multiplier*25, height_multiplier*20)
            if data[1] == 'standard\n':
                button_layout("Standard", [70, 385, 250, 125], False, "w", "Standard", "Neon", "Checkered", "Quilt", "Blue")
            elif data[1] == 'neon\n':
                button_layout("Neon", [370, 385, 250, 125], False, "w", "Standard", "Neon", "Checkered", "Quilt", "Blue")
            elif data[1] == 'checkered\n':
                button_layout("Checkered", [670, 385, 250, 125], False, "w", "Standard", "Neon", "Checkered", "Quilt", "Blue")
            elif data[1] == 'quilt\n':
                button_layout("Quilt", [970, 385, 250, 125], False, "w", "Standard", "Neon", "Checkered", "Quilt", "Blue")
            elif data[1] == 'blue\n':
                button_layout("Blue", [1270, 385, 250, 125], False, "w", "Standard", "Neon", "Checkered", "Quilt", "Blue")
        elif skin_type == 's':
            write_text("Spawner Skins", "freesansbold.ttf", 75, score_color, 'topleft', width_multiplier*25, height_multiplier*20)
            if data[2] == 'blue\n':
                button_layout("Blue", [70, 385, 250, 125], False, "s", "Blue", "Green", "Red", "White", "Chess Board")
            elif data[2] == 'green\n':
                button_layout("Green", [370, 385, 250, 125], False, "s", "Blue", "Green", "Red", "White", "Chess Board")
            elif data[2] == 'red\n':
                button_layout("Red", [670, 385, 250, 125], False, "s", "Blue", "Green", "Red", "White", "Chess Board")
            elif data[2] == 'white\n':
                button_layout("White", [970, 385, 250, 125], False, "s", "Blue", "Green", "Red", "White", "Chess Board")
            elif data[2] == 'chessboard\n':
                button_layout("Chess Board", [1270, 385, 250, 125], False, "s", "Blue", "Green", "Red", "White", "Chess Board")
        elif skin_type == 'd':
            write_text("Dot Skins", "freesansbold.ttf", 75, score_color, 'topleft', width_multiplier*25, height_multiplier*20)
            if data[3] == 'white\n':
                button_layout("White", [70, 385, 250, 125], False, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
            elif data[3] == 'blue\n':
                button_layout("Blue", [370, 385, 250, 125], False, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
            elif data[3] == 'purple\n':
                button_layout("Purple", [670, 385, 250, 125], False, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
            elif data[3] == 'smileyface\n':
                button_layout("Smiley Face", [970, 385, 250, 125], False, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
            elif data[3] == 'rainbow\n':
                button_layout("Rainbow", [1270, 385, 250, 125], False, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
        elif skin_type == 'b':
            write_text("Backgrounds", "freesansbold.ttf", 75, score_color, 'topleft', width_multiplier*25, height_multiplier*20)
            if data[4] == 'black\n':
                button_layout("Black", [70, 385, 250, 125], False, "b", "Black", "Gray", "Sky", "Space", "Robot")
            elif data[4] == 'gray\n':
                button_layout("Gray", [370, 385, 250, 125], False, "b", "Black", "Gray", "Sky", "Space", "Robot")
            elif data[4] == 'sky\n':
                button_layout("Sky", [670, 385, 250, 125], False, "b", "Black", "Gray", "Sky", "Space", "Robot")
            elif data[4] == 'space\n':
                button_layout("Space", [970, 385, 250, 125], False, "b", "Black", "Gray", "Sky", "Space", "Robot")
            elif data[4] == 'robot\n':
                button_layout("Robot", [1270, 385, 250, 125], False, "b", "Black", "Gray", "Sky", "Space", "Robot")

        all_sprites.update()
        all_sprites.draw(window)
        pygame.display.update()

def skin_click(skin_type, skin):
    create_basic_sprites()

    coins = int(data[5])

    if skin_type == 'w':
        write_text("Wall Skins", "freesansbold.ttf", 75, score_color, 'topleft', width_multiplier * 25, height_multiplier * 20)
    elif skin_type == 's':
        write_text("Spawner Skins", "freesansbold.ttf", 75, score_color, 'topleft', width_multiplier * 25,height_multiplier * 20)
    elif skin_type == 'd':
        write_text("Dot Skins", "freesansbold.ttf", 75, score_color, 'topleft', width_multiplier * 25, height_multiplier * 20)
    elif skin_type == 'b':
        write_text("Backgrounds", "freesansbold.ttf", 75, score_color, 'topleft', width_multiplier * 25, height_multiplier * 20)

    write_text(("Coins: %d" % coins), "freesansbold.ttf", 30, coin_color, "topright", (WIDTH - (width_multiplier * 25)), (HEIGHT - (height_multiplier * 52)))

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Back", button_text_color, width_multiplier*25, (HEIGHT - (height_multiplier*75)), 100, 50, button_color, button_color)

        if skin != "":
            if skin_type == 'w':
                if skin == 'standard':
                    if data[1] == 'neon\n':
                        button_layout("Neon", [370, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'checkered\n':
                        button_layout("Checkered", [670, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'quilt\n':
                        button_layout("Quilt", [970, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'blue\n':
                        button_layout("Blue", [1270, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    write_text("Equip Standard Wall Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('w', 'standard', 0))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'w')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('w', 'standard'))
                elif skin == 'neon':
                    if data[1] == 'standard\n':
                        button_layout("Standard", [70, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'checkered\n':
                        button_layout("Checkered", [670, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'quilt\n':
                        button_layout("Quilt", [970, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'blue\n':
                        button_layout("Blue", [1270, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'neon\n' in wall_skin_data:
                        write_text("Equip Neon Wall Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                    else:
                        write_text("Unlock Neon Wall Skin", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("For 10 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('w', 'neon', 10))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'w')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('w', 'neon'))
                elif skin == 'checkered':
                    if data[1] == 'standard\n':
                        button_layout("Standard", [70, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'neon\n':
                        button_layout("Neon", [370, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'quilt\n':
                        button_layout("Quilt", [970, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'blue\n':
                        button_layout("Blue", [1270, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'checkered\n' in wall_skin_data:
                        write_text("Equip Checkered Wall Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                    else:
                        write_text("Unlock Checkered Wall Skin", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("For 20 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('w', 'checkered', 20))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'w')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('w', 'checkered'))
                elif skin == 'quilt':
                    if data[1] == 'standard\n':
                        button_layout("Standard", [70, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'neon\n':
                        button_layout("Neon", [370, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'checkered\n':
                        button_layout("Checkered", [670, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'blue\n':
                        button_layout("Blue", [1270, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'quilt\n' in wall_skin_data:
                        write_text("Equip Quilt Wall Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                    else:
                        write_text("Unlock Quilt Wall Skin", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("For 30 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('w', 'quilt', 30))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'w')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('w', 'quilt'))
                elif skin == 'blue':
                    if data[1] == 'standard\n':
                        button_layout("Standard", [70, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'neon\n':
                        button_layout("Neon", [370, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'checkered\n':
                        button_layout("Checkered", [670, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")
                    elif data[1] == 'quilt\n':
                        button_layout("Quilt", [970, 385, 250, 125], True, "", "Standard", "Neon", "Checkered", "Quilt", "Blue")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'blue\n' in wall_skin_data:
                        write_text("Equip Blue Wall Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                    else:
                        write_text("Unlock Blue Wall Skin", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("For 50 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('w', 'blue', 50))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'w')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('w', 'blue'))
            elif skin_type == 's':
                if skin == 'blue':
                    if data[2] == 'green\n':
                        button_layout("Green", [370, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'red\n':
                        button_layout("Red", [670, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'white\n':
                        button_layout("White", [970, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'chessboard\n':
                        button_layout("Chess Board", [1270, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    write_text("Equip Blue Spawner", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                    write_text("Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('s', 'blue', 0))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 's')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('s', 'blue'))
                elif skin == 'green':
                    if data[2] == 'blue\n':
                        button_layout("Blue", [70, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'red\n':
                        button_layout("Red", [670, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'white\n':
                        button_layout("White", [970, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'chessboard\n':
                        button_layout("Chess Board", [1270, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'green\n' in spawner_skin_data:
                        write_text("Equip Green Spawner", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))
                    else:
                        write_text("Unlock Green Spawner", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin for 5 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('s', 'green', 5))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 's')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('s', 'green'))
                elif skin == 'red':
                    if data[2] == 'blue\n':
                        button_layout("Blue", [70, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'green\n':
                        button_layout("Green", [370, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'white\n':
                        button_layout("White", [970, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'chessboard\n':
                        button_layout("Chess Board", [1270, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'red\n' in spawner_skin_data:
                        write_text("Equip Red Spawner", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))
                    else:
                        write_text("Unlock Red Spawner", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin for 10 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('s', 'red', 10))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 's')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('s', 'red'))
                elif skin == 'white':
                    if data[2] == 'blue\n':
                        button_layout("Blue", [70, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'green\n':
                        button_layout("Green", [370, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'red\n':
                        button_layout("Red", [670, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'chessboard\n':
                        button_layout("Chess Board", [1270, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'white\n' in spawner_skin_data:
                        write_text("Equip White Spawner", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))
                    else:
                        write_text("Unlock White Spawner", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin for 25 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('s', 'white', 25))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 's')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('s', 'white'))
                elif skin == 'chessboard':
                    if data[2] == 'blue\n':
                        button_layout("Blue", [70, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'green\n':
                        button_layout("Green", [370, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'red\n':
                        button_layout("Red", [670, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")
                    elif data[2] == 'white\n':
                        button_layout("White", [970, 385, 250, 125], True, "", "Blue", "Green", "Red", "White", "Chess Board")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'chessboard\n' in spawner_skin_data:
                        write_text("Equip Chess Board", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Spawner Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))
                    else:
                        write_text("Unlock Chess Board Spawner", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin for 50 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('s', 'chessboard', 50))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 's')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('s', 'chessboard'))
            elif skin_type == 'd':
                if skin == 'white':
                    if data[3] == 'blue\n':
                        button_layout("Blue", [370, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'purple\n':
                        button_layout("Purple", [670, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'smileyface\n':
                        button_layout("Smiley Face", [970, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'rainbow\n':
                        button_layout("Rainbow", [1270, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    write_text("Equip White Dot", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                    write_text("Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('d', 'white', 0))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'd')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('d', 'white'))
                elif skin == 'blue':
                    if data[3] == 'white\n':
                        button_layout("White", [70, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'purple\n':
                        button_layout("Purple", [670, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'smileyface\n':
                        button_layout("Smiley Face", [970, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'rainbow\n':
                        button_layout("Rainbow", [1270, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'blue\n' in dot_skin_data:
                        write_text("Equip Blue Dot", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))
                    else:
                        write_text("Unlock Blue Dot", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin for 10 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('d', 'blue', 10))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'd')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('d', 'blue'))
                elif skin == 'purple':
                    if data[3] == 'white\n':
                        button_layout("White", [70, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'blue\n':
                        button_layout("Blue", [370, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'smileyface\n':
                        button_layout("Smiley Face", [970, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'rainbow\n':
                        button_layout("Rainbow", [1270, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'purple\n' in dot_skin_data:
                        write_text("Equip Purple Dot", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))
                    else:
                        write_text("Unlock Purple Dot", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin for 20 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('d', 'purple', 20))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'd')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('d', 'purple'))
                elif skin == 'smileyface':
                    if data[3] == 'white\n':
                        button_layout("White", [70, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'blue\n':
                        button_layout("Blue", [370, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'purple\n':
                        button_layout("Purple", [670, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'rainbow\n':
                        button_layout("Rainbow", [1270, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'smileyface\n' in dot_skin_data:
                        write_text("Equip Smiley Face Dot", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))
                    else:
                        write_text("Unlock Smiley Face Dot", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin for 30 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('d', 'smileyface', 30))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'd')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('d', 'smileyface'))
                elif skin == 'rainbow':
                    if data[3] == 'white\n':
                        button_layout("White", [70, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'blue\n':
                        button_layout("Blue", [370, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'purple\n':
                        button_layout("Purple", [670, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")
                    elif data[3] == 'smileyface\n':
                        button_layout("Smiley Face", [970, 385, 250, 125], True, "d", "White", "Blue", "Purple", "Smiley Face", "Rainbow")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'rainbow\n' in dot_skin_data:
                        write_text("Equip Rainbow Dot", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))
                    else:
                        write_text("Unlock Rainbow Dot", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Skin for 50 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('d', 'rainbow', 50))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'd')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('d', 'rainbow'))
            elif skin_type == 'b':
                if skin == 'black':
                    if data[4] == 'gray\n':
                        button_layout("Gray", [370, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'sky\n':
                        button_layout("Sky", [670, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'space\n':
                        button_layout("Space", [970, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'robot\n':
                        button_layout("Robot", [1270, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    write_text("Equip Black", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                    write_text("Background?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('b', 'black', 0))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'b')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('b', 'black'))
                elif skin == 'gray':
                    if data[4] == 'black\n':
                        button_layout("Black", [70, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'sky\n':
                        button_layout("Sky", [670, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'space\n':
                        button_layout("Space", [970, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'robot\n':
                        button_layout("Robot", [1270, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'gray\n' in background_skin_data:
                        write_text("Equip Gray", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Background?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))
                    else:
                        write_text("Unlock Gray", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Background For 5 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('b', 'gray', 5))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'b')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('b', 'gray'))
                elif skin == 'sky':
                    if data[4] == 'black\n':
                        button_layout("Black", [70, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'gray\n':
                        button_layout("Gray", [370, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'space\n':
                        button_layout("Space", [970, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'robot\n':
                        button_layout("Robot", [1270, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'sky\n' in background_skin_data:
                        write_text("Equip Sky", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Background?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))
                    else:
                        write_text("Unlock Sky", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Background For 25 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('b', 'sky', 25))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'b')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('b', 'sky'))
                elif skin == 'space':
                    if data[4] == 'black\n':
                        button_layout("Black", [70, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'gray\n':
                        button_layout("Gray", [370, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'sky\n':
                        button_layout("Sky", [670, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'robot\n':
                        button_layout("Robot", [1270, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'space\n' in background_skin_data:
                        write_text("Equip Space", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Background?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))
                    else:
                        write_text("Unlock Space", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Background For 50 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('b', 'space', 50))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'b')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('b', 'space'))
                elif skin == 'robot':
                    if data[4] == 'black\n':
                        button_layout("Black", [70, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'gray\n':
                        button_layout("Gray", [370, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'sky\n':
                        button_layout("Sky", [670, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")
                    elif data[4] == 'space\n':
                        button_layout("Space", [970, 385, 250, 125], True, "", "Black", "Gray", "Sky", "Space", "Robot")

                    pygame.draw.rect(window, skin_unlcok_popup_color, (WIDTH / 2 - (width_multiplier * 250),
                                                                       HEIGHT / 2 - (height_multiplier * 150),
                                                                       width_multiplier * 500,
                                                                       height_multiplier * 300))
                    if 'robot\n' in background_skin_data:
                        write_text("Equip Robot", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Background?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))
                    else:
                        write_text("Unlock Robot", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*100))
                        write_text("Background For 100 Coins?", "freesansbold.ttf", 30, button_text_color, "center", WIDTH / 2, HEIGHT / 2 - (height_multiplier*50))

                    button("Yes", button_text_color, yes_button_x, yes_button_y, 140, 50, button_color, button_hover_color, equip_skin, ('b', 'robot', 100))
                    button("No", button_text_color, no_button_x, no_button_y, 140, 50, button_color, button_hover_color, skin_shop, 'b')
                    button("Preview", button_text_color, preview_button_x, preview_button_y, 140, 50, button_color, button_hover_color, preview_skin, ('b', 'robot'))
        else:
            skin_shop(skin_type)

        pygame.display.update()

def preview_skin(skin_type, skin):
    skin = skin + '\n'
    y = HEIGHT/2 - 5
    damage_n = 0

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if skin_type == 'b':
            preview_background_image = pygame.transform.scale(pygame.image.load(background_skin_dict[skin]), (WIDTH, HEIGHT))
            window.blit(preview_background_image, background_rect)
        else:
            window.blit(background_image, background_rect)

        if skin_type == 'w':
            preview_h_wall_images = [
                pygame.transform.scale(pygame.image.load(wall_skin_dict[skin][0][0]), h_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[skin][0][1]), h_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[skin][0][2]), h_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[skin][0][3]), h_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[skin][0][4]), h_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[skin][0][5]), h_wall_dimentions)]
            preview_v_wall_images = [
                pygame.transform.scale(pygame.image.load(wall_skin_dict[skin][1][0]), v_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[skin][1][1]), v_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[skin][1][2]), v_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[skin][1][3]), v_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[skin][1][4]), v_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[skin][1][5]), v_wall_dimentions)]
            window.blit(preview_h_wall_images[damage_n], (width_multiplier*20, 0, WIDTH - (width_multiplier*40), height_multiplier*20))
            window.blit(preview_h_wall_images[0], (width_multiplier*20, HEIGHT - (height_multiplier*20), WIDTH - (width_multiplier*40), height_multiplier*20))
            window.blit(preview_v_wall_images[0], (0, height_multiplier*20, width_multiplier*20, HEIGHT - (height_multiplier*38)))
            window.blit(preview_v_wall_images[0], (WIDTH - (width_multiplier*20), height_multiplier*20, width_multiplier*20, HEIGHT - (height_multiplier*39)))
        else:
            window.blit(h_wall_images[damage_n], (width_multiplier * 20, 0, WIDTH - (width_multiplier * 40), height_multiplier * 20))
            window.blit(h_wall_images[0], (width_multiplier * 20, HEIGHT - (height_multiplier * 20), WIDTH - (width_multiplier * 40), height_multiplier * 20))
            window.blit(v_wall_images[0], (0, height_multiplier * 20, width_multiplier * 20, HEIGHT - (height_multiplier * 38)))
            window.blit(v_wall_images[0], (WIDTH - (width_multiplier * 20), height_multiplier * 20, width_multiplier * 20, HEIGHT - (height_multiplier * 39)))

        if skin_type == 'd':
            if y <= height_multiplier*20:
                pygame.mixer.Sound.play(damage_sound)
                y = HEIGHT/2 - (height_multiplier*5)
                damage_n += 1
            if damage_n == 6:
                damage_n = 0
            else:
                preview_dot_image = pygame.transform.scale(pygame.image.load(dot_skin_dict[skin]), (int(width_multiplier*10), int(height_multiplier*10)))
                window.blit(preview_dot_image, (WIDTH / 2 - (width_multiplier*5), y))
                y -= height_multiplier*5
        else:
            if y <= height_multiplier*20:
                pygame.mixer.Sound.play(damage_sound)
                y = HEIGHT/2 - (height_multiplier*5)
                damage_n += 1
            if damage_n == 6:
                damage_n = 0
            else:
                window.blit(dot_image, (WIDTH / 2 - (width_multiplier*5), y))
                y -= height_multiplier*5

        if skin_type == 's':
            preview_spawner_image = pygame.transform.scale(pygame.image.load(spawner_skin_dict[skin]), (int(width_multiplier*50), int(height_multiplier*50)))
            window.blit(preview_spawner_image, (WIDTH/2 - (width_multiplier * 25), HEIGHT/2 - (height_multiplier*25)))
            corner_image = pygame.transform.scale(preview_spawner_image, (int(width_multiplier * 20), int(height_multiplier * 20)))
            window.blit(corner_image, (0, 0))
            window.blit(corner_image, (WIDTH - (width_multiplier * 20), 0))
            window.blit(corner_image, (0, HEIGHT - (height_multiplier * 20)))
            window.blit(corner_image, (WIDTH - (width_multiplier * 20), HEIGHT - (height_multiplier * 20)))
        else:
            window.blit(spawner_image, (WIDTH / 2 - (width_multiplier * 25), HEIGHT / 2 - (height_multiplier * 25)))
            corner_image = pygame.transform.scale(spawner_image, (int(width_multiplier * 20), int(height_multiplier * 20)))
            window.blit(corner_image, (0, 0))
            window.blit(corner_image, (WIDTH - (width_multiplier * 20), 0))
            window.blit(corner_image, (0, HEIGHT - (height_multiplier * 20)))
            window.blit(corner_image, (WIDTH - (width_multiplier * 20), HEIGHT - (height_multiplier * 20)))

        button("Exit Preview", button_text_color, width_multiplier*25, (HEIGHT - (height_multiplier*75)), 200, 50, button_color, button_hover_color, skin_shop, skin_type)

        pygame.display.update()

def equip_skin(skin_type, skin, price):
    if skin_type == 'w':
        if '%s\n' % skin in wall_skin_data:
            data[1] = '%s\n' % skin
            os.chmod(save_file, stat.S_IWRITE)
            with open(save_file, 'w') as file:
                file.writelines(data)
            os.chmod(save_file, stat.S_IREAD)
            global wall_skin
            wall_skin = data[1]
            global h_wall_images
            h_wall_images = [
                pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][0]), h_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][1]), h_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][2]), h_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][3]), h_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][4]), h_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][5]), h_wall_dimentions)]
            global v_wall_images
            v_wall_images = [
                pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][0]), v_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][1]), v_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][2]), v_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][3]), v_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][4]), v_wall_dimentions),
                pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][5]), v_wall_dimentions)]
            pygame.mixer.Sound.play(level_up_sound)
        else:
            if int(data[5]) >= price:
                wall_skin_data.append('%s\n' % skin)
                os.chmod(unlocked_wall_skins, stat.S_IWRITE)
                with open(unlocked_wall_skins, 'w') as file:
                    file.writelines(wall_skin_data)
                os.chmod(unlocked_wall_skins, stat.S_IREAD)
                coins = int(data[5])
                coins -= price
                data[5] = str(coins)
                data[1] = '%s\n' % skin
                os.chmod(save_file, stat.S_IWRITE)
                with open(save_file, 'w') as file:
                    file.writelines(data)
                os.chmod(save_file, stat.S_IREAD)
                wall_skin = data[1]
                h_wall_images = [
                    pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][0]), h_wall_dimentions),
                    pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][1]), h_wall_dimentions),
                    pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][2]), h_wall_dimentions),
                    pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][3]), h_wall_dimentions),
                    pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][4]), h_wall_dimentions),
                    pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][0][5]), h_wall_dimentions)]
                v_wall_images = [
                    pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][0]), v_wall_dimentions),
                    pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][1]), v_wall_dimentions),
                    pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][2]), v_wall_dimentions),
                    pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][3]), v_wall_dimentions),
                    pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][4]), v_wall_dimentions),
                    pygame.transform.scale(pygame.image.load(wall_skin_dict[wall_skin][1][5]), v_wall_dimentions)]
                pygame.mixer.Sound.play(purchase_skin_sound)
    elif skin_type == 's':
        if '%s\n' % skin in spawner_skin_data:
            data[2] = '%s\n' % skin
            os.chmod(save_file, stat.S_IWRITE)
            with open(save_file, 'w') as file:
                file.writelines(data)
            os.chmod(save_file, stat.S_IREAD)
            global spawner_skin
            spawner_skin = data[2]
            global spawner_image
            spawner_image = pygame.transform.scale(pygame.image.load(spawner_skin_dict[spawner_skin]).convert(), (int(width_multiplier*50), int(height_multiplier*50)))
            pygame.mixer.Sound.play(level_up_sound)
        else:
            if int(data[5]) >= price:
                spawner_skin_data.append('%s\n' % skin)
                os.chmod(unlocked_spawner_skins, stat.S_IWRITE)
                with open(unlocked_spawner_skins, 'w') as file:
                    file.writelines(spawner_skin_data)
                os.chmod(unlocked_spawner_skins, stat.S_IREAD)
                coins = int(data[5])
                coins -= price
                data[5] = str(coins)
                data[2] = '%s\n' % skin
                os.chmod(save_file, stat.S_IWRITE)
                with open(save_file, 'w') as file:
                    file.writelines(data)
                os.chmod(save_file, stat.S_IREAD)
                spawner_skin = data[2]
                spawner_image = pygame.transform.scale(pygame.image.load(spawner_skin_dict[spawner_skin]).convert(), (int(width_multiplier * 50), int(height_multiplier * 50)))
                pygame.mixer.Sound.play(purchase_skin_sound)
    elif skin_type == 'd':
        if '%s\n' % skin in dot_skin_data:
            data[3] = '%s\n' % skin
            os.chmod(save_file, stat.S_IWRITE)
            with open(save_file, 'w') as file:
                file.writelines(data)
            os.chmod(save_file, stat.S_IREAD)
            global dot_skin
            dot_skin = data[3]
            global dot_image
            dot_image = pygame.transform.scale(pygame.image.load(dot_skin_dict[dot_skin]).convert(), (int(width_multiplier * 10), int(height_multiplier * 10)))
            pygame.mixer.Sound.play(level_up_sound)
        else:
            if int(data[5]) >= price:
                dot_skin_data.append('%s\n' % skin)
                os.chmod(unlocked_dot_skins, stat.S_IWRITE)
                with open(unlocked_dot_skins, 'w') as file:
                    file.writelines(dot_skin_data)
                os.chmod(unlocked_dot_skins, stat.S_IREAD)
                coins = int(data[5])
                coins -= price
                data[5] = str(coins)
                data[3] = '%s\n' % skin
                os.chmod(save_file, stat.S_IWRITE)
                with open(save_file, 'w') as file:
                    file.writelines(data)
                os.chmod(save_file, stat.S_IREAD)
                dot_skin = data[3]
                dot_image = pygame.transform.scale(pygame.image.load(dot_skin_dict[dot_skin]).convert(), (int(width_multiplier * 10), int(height_multiplier * 10)))
                pygame.mixer.Sound.play(purchase_skin_sound)
    elif skin_type == 'b':
        if '%s\n' % skin in background_skin_data:
            data[4] = '%s\n' % skin
            os.chmod(save_file, stat.S_IWRITE)
            with open(save_file, 'w') as file:
                file.writelines(data)
            os.chmod(save_file, stat.S_IREAD)
            global background_skin
            background_skin = data[4]
            global background_image
            background_image = pygame.transform.scale(pygame.image.load(background_skin_dict[background_skin]).convert(), (WIDTH, HEIGHT))
            pygame.mixer.Sound.play(level_up_sound)
        else:
            if int(data[5]) >= price:
                background_skin_data.append('%s\n' % skin)
                os.chmod(unlocked_background_skins, stat.S_IWRITE)
                with open(unlocked_background_skins, 'w') as file:
                    file.writelines(background_skin_data)
                os.chmod(unlocked_background_skins, stat.S_IREAD)
                coins = int(data[5])
                coins -= price
                data[5] = str(coins)
                data[4] = '%s\n' % skin
                os.chmod(save_file, stat.S_IWRITE)
                with open(save_file, 'w') as file:
                    file.writelines(data)
                os.chmod(save_file, stat.S_IREAD)
                background_skin = data[4]
                background_image = pygame.transform.scale(pygame.image.load(background_skin_dict[background_skin]).convert(), (WIDTH, HEIGHT))
                pygame.mixer.Sound.play(purchase_skin_sound)
    skin_shop(skin_type)

def create_basic_sprites():
    top_left_corner = TopLeftCorner()
    all_sprites.add(top_left_corner)
    top_right_corner = TopRightCorner()
    all_sprites.add(top_right_corner)
    bottom_left_corner = BottomLeftCorner()
    all_sprites.add(bottom_left_corner)
    bottom_right_corner = BottomRightCorner()
    all_sprites.add(bottom_right_corner)
    top_wall = TopWall()
    all_sprites.add(top_wall)
    bottom_wall = BottomWall()
    all_sprites.add(bottom_wall)
    left_wall = LeftWall()
    all_sprites.add(left_wall)
    right_wall = RightWall()
    all_sprites.add(right_wall)

    all_sprites.update()
    window.blit(background_image, background_rect)
    all_sprites.draw(window)
    pygame.display.update()

def game_loop():
    global i
    i = 1
    global level_time
    level_time = -4
    global game_time
    game_time = -5
    global level
    level = 1
    global score
    score = 0
    high_score = int(data[0])
    global wall_skin
    wall_skin = data[1]
    coins = int(data[5])

    pygame.mixer.music.stop()

    time_to_start = 5

    spawner = Spawner()
    all_sprites.add(spawner)
    spawner_list.add(spawner)
    top_left_corner = TopLeftCorner()
    all_sprites.add(top_left_corner)
    top_right_corner = TopRightCorner()
    all_sprites.add(top_right_corner)
    bottom_left_corner = BottomLeftCorner()
    all_sprites.add(bottom_left_corner)
    bottom_right_corner = BottomRightCorner()
    all_sprites.add(bottom_right_corner)
    top_wall = TopWall()
    all_sprites.add(top_wall)
    bottom_wall = BottomWall()
    all_sprites.add(bottom_wall)
    left_wall = LeftWall()
    all_sprites.add(left_wall)
    right_wall = RightWall()
    all_sprites.add(right_wall)

    while time_to_start > 0:
        all_sprites.update()
        window.blit(background_image, background_rect)
        all_sprites.draw(window)
        spawner_list.draw(window)

        write_text("Score: 0", "freesansbold.ttf", 30, score_color, "topleft", width_multiplier * 25,
                   HEIGHT - (height_multiplier * 80))
        write_text("Coins: %d" % coins, "freesansbold.ttf", 30, coin_color, "topleft", width_multiplier * 25,
                   HEIGHT - (height_multiplier * 52))
        write_text("Time: 0", "freesansbold.ttf", 30, score_color, "topleft", width_multiplier * 25,
                   height_multiplier * 25)
        write_text("Level: 1", "freesansbold.ttf", 30, score_color, "topright", WIDTH - (width_multiplier * 25),
                   height_multiplier * 25)
        write_text("High Score: %d" % high_score, "freesansbold.ttf", 30, score_color, "topright",
                   WIDTH - (width_multiplier * 25), (HEIGHT - (height_multiplier * 52)))
        write_text("GAME STARTS IN: %d" % time_to_start, "freesansbold.ttf", 125, score_color, "center", WIDTH / 2,
                   HEIGHT / 2)

        pygame.display.update()
        time_to_start -= 1
        pygame.mixer.Sound.play(click_sound)
        time.sleep(1)

    pygame.mixer.music.play(-1)

    run = True

    while run:
        clock.tick(FPS)

        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if keys[pygame.K_ESCAPE] or keys[pygame.K_SPACE]:
            global paused
            paused = True
            pause()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == CLOCKTICK:
                if i > (3/(level if level > 2 else 1)) and game_time >= 0:
                    dot_spawn()
                    i = 1
                if level_time >= 60:
                    pygame.mixer.Sound.play(level_up_sound)
                    level_time = 0
                    level += 1
                i += 1
                level_time += 1
                game_time += 1
                high_score = int(data[0])

        for dot in dot_list:
            if dot.rect.y < top_wall.rect.y + 20:
                pygame.mixer.Sound.play(damage_sound)
                dot.kill()
                top_wall.damage()
            if dot.rect.y + dot.height > bottom_wall.rect.y:
                pygame.mixer.Sound.play(damage_sound)
                dot.kill()
                bottom_wall.damage()
            if dot.rect.x < left_wall.rect.x + 20:
                pygame.mixer.Sound.play(damage_sound)
                dot.kill()
                left_wall.damage()
            if dot.rect.x + dot.width > right_wall.rect.x:
                pygame.mixer.Sound.play(damage_sound)
                dot.kill()
                right_wall.damage()
            if (dot.rect.x + dot.width + dot.buffer > mouse_pos[0] > dot.rect.x - dot.buffer) and \
                    (dot.rect.y + dot.height + dot.buffer > mouse_pos[1] > dot.rect.y - dot.buffer) and \
                    (mouse_pos[0] > spawner.rect.x + spawner.width or mouse_pos[0] < spawner.rect.x or mouse_pos[1] > spawner.rect.y + spawner.height or mouse_pos[1] < spawner.rect.y):
                pygame.mixer.Sound.play(dot_kill_sound)
                dot.kill()
                score += 1
                if score > high_score:
                    high_score = score
                    data[0] = '%s\n' % str(high_score)

        for coin in coin_list:
            if coin.rect.y < top_wall.rect.y + 20:
                pygame.mixer.Sound.play(damage_sound)
                coin.kill()
                top_wall.damage()
            if coin.rect.y + coin.height > bottom_wall.rect.y:
                pygame.mixer.Sound.play(damage_sound)
                coin.kill()
                bottom_wall.damage()
            if coin.rect.x < left_wall.rect.x + 20:
                pygame.mixer.Sound.play(damage_sound)
                coin.kill()
                left_wall.damage()
            if coin.rect.x + coin.width > right_wall.rect.x:
                pygame.mixer.Sound.play(damage_sound)
                coin.kill()
                right_wall.damage()
            if (coin.rect.x + coin.width + coin.buffer > mouse_pos[0] > coin.rect.x - coin.buffer) and \
                    (coin.rect.y + coin.height + coin.buffer > mouse_pos[1] > coin.rect.y - coin.buffer) and \
                    (mouse_pos[0] > spawner.rect.x + spawner.width or mouse_pos[0] < spawner.rect.x or mouse_pos[1] > spawner.rect.y + spawner.height or mouse_pos[1] < spawner.rect.y):
                pygame.mixer.Sound.play(coin_pickup_sound)
                coin.kill()
                score += 1
                coins += 1
                data[5] = '%s\n' % str(coins)
                if score > high_score:
                    high_score = score
                    data[0] = '%s\n' % str(high_score)

        all_sprites.update()
        window.blit(background_image, background_rect)
        all_sprites.draw(window)
        spawner_list.draw(window)

        write_text(("Score: %d" % score), "freesansbold.ttf", 30, score_color, "topleft", width_multiplier*25, (HEIGHT - (height_multiplier*80)))
        write_text(("Coins: %d" % coins), "freesansbold.ttf", 30, coin_color, "topleft", width_multiplier*25, (HEIGHT - (height_multiplier*52)))
        write_text(("Time: %d" % game_time), "freesansbold.ttf", 30, score_color, "topleft", width_multiplier*25, height_multiplier*25)
        write_text(("Level: %d" % level), "freesansbold.ttf", 30, score_color, "topright", (WIDTH - (width_multiplier*25)), height_multiplier*25)
        write_text(("High Score: %d" % high_score), "freesansbold.ttf", 30, score_color, "topright", (WIDTH - (width_multiplier*25)), (HEIGHT - (height_multiplier*52)))

        os.chmod(save_file, stat.S_IWRITE)
        with open(save_file, 'w') as file:
            file.writelines(data)
        os.chmod(save_file, stat.S_IREAD)

        pygame.display.update()

intro()
pygame.quit()
quit()