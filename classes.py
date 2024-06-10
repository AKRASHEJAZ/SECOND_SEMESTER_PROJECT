import pygame
import os

pygame.init()

class Hero :

    def __init__(self, window  , position ,  image = "idle.png"):
        self.Is_Visible = True
        self.Position = position
        self.Pos_x ,self.Pos_y = self.Position
        self.Image = pygame.image.load( os.path.join( "assets",f"{image}"))
        self.Idle = self.Image
        self.Window = window
        self.Image = pygame.transform.scale(self.Image, (40, 40))
        self.rect = self.Image.get_rect()
        self.Up = [pygame.image.load(os.path.join("character_anims_up", "hero_up_1.png")),
                   pygame.image.load(os.path.join("character_anims_up", "hero_up_2.png")),
                   pygame.image.load(os.path.join("character_anims_up", "hero_up_3.png")),
                   pygame.image.load(os.path.join("character_anims_up", "hero_up_4.png")),
                   pygame.image.load(os.path.join("character_anims_up", "hero_up_5.png")),
                   pygame.image.load(os.path.join("character_anims_up", "hero_up_6.png")),
                   pygame.image.load(os.path.join("character_anims_up", "hero_up_7.png")),
                   pygame.image.load(os.path.join("character_anims_up", "hero_up_8.png")),
                   pygame.image.load(os.path.join("character_anims_up", "hero_up_9.png"))
                ]

        self.Down = [pygame.image.load(os.path.join("character_anims_down", "down_ (1).png")),
                   pygame.image.load(os.path.join("character_anims_down", "down_ (2).png")),
                   pygame.image.load(os.path.join("character_anims_down", "down_ (3).png")),
                   pygame.image.load(os.path.join("character_anims_down", "down_ (4).png")),
                   pygame.image.load(os.path.join("character_anims_down", "down_ (5).png")),
                   pygame.image.load(os.path.join("character_anims_down", "down_ (6).png")),
                   pygame.image.load(os.path.join("character_anims_down", "down_ (7).png")),
                   pygame.image.load(os.path.join("character_anims_down", "down_ (8).png")),
                   pygame.image.load(os.path.join("character_anims_down", "down_ (9).png"))
                   ]

        self.Left = [pygame.image.load(os.path.join("character_anims_left", "left_ 1.png")),
                     pygame.image.load(os.path.join("character_anims_left", "left_ 2.png")),
                     pygame.image.load(os.path.join("character_anims_left", "left_ 3.png")),
                     pygame.image.load(os.path.join("character_anims_left", "left_ 4.png")),
                     pygame.image.load(os.path.join("character_anims_left", "left_ 5.png")),
                     pygame.image.load(os.path.join("character_anims_left", "left_ 6.png")),
                     pygame.image.load(os.path.join("character_anims_left", "left_ 7.png")),
                     pygame.image.load(os.path.join("character_anims_left", "left_ 8.png")),
                     pygame.image.load(os.path.join("character_anims_left", "left_ 9.png"))
                     ]

        self.Right = [pygame.image.load(os.path.join("character_anims_right", "right_1.png")),
                   pygame.image.load(os.path.join("character_anims_right", "right_2.png")),
                   pygame.image.load(os.path.join("character_anims_right", "right_3.png")),
                   pygame.image.load(os.path.join("character_anims_right", "right_4.png")),
                   pygame.image.load(os.path.join("character_anims_right", "right_5.png")),
                   pygame.image.load(os.path.join("character_anims_right", "right_6.png")),
                   pygame.image.load(os.path.join("character_anims_right", "right_7.png")),
                   pygame.image.load(os.path.join("character_anims_right", "right_8.png")),
                   pygame.image.load(os.path.join("character_anims_right", "right_9.png"))
                   ]

        self.step = 0
    def Update(self,walls):

        self.Image = self.Idle
        next_pos_x , next_pos_y = self.Pos_x,self.Pos_y
        key = pygame.key.get_pressed()

        #COUNTING STEPS TILL 9 ONLY
        if self.step >= 9:
            self.step = 0

        #CHECKS THE KEY CONTROL FOR MOVEMENT OF CHARACTER
        if key[pygame.K_UP] :
            self.Image = self.Up[self.step]
            self.step  += 1
            next_pos_y -= 5

        elif key[pygame.K_DOWN] :
            self.Image = self.Down[self.step]
            self.step += 1
            next_pos_y += 5

        elif key[pygame.K_LEFT] :
            self.Image = self.Left[self.step]
            self.step += 1
            next_pos_x -= 5

        elif key[pygame.K_RIGHT] :
            self.Image = self.Right[self.step]
            self.step += 1
            next_pos_x += 5

        #CLAMPS HERO IN BOUNDRY
        next_pos_x = max(32, min(next_pos_x, 750))
        next_pos_y = max(32, min(next_pos_y, 550))

        #CHECKS FOR COLLISION WITH WALLS

        if (-100 <= next_pos_x <= 1600) and (-100 <= next_pos_y <= 1200):
            collision = False
            for wall in walls:
                if pygame.Rect(next_pos_x, next_pos_y, 25, 25).colliderect(
                        wall.Collide_Box):
                    collision = True
                    break
            if not collision:
                self.Pos_x, self.Pos_y = next_pos_x, next_pos_y

        #DISPLAYS CORESPPONDING CHARACTER IMAGE
        if self.Is_Visible:
            self.Image = pygame.transform.scale(self.Image,(40,40))
            self.Window.blit(self.Image,(self.Pos_x , self.Pos_y))
        else:
            self.New_Time = pygame.time.get_ticks()
            if self.New_Time - self.Damage_Time >= 500:
                self.Is_Visible = not self.Is_Visible
                self.Damage_Time = self.New_Time
    def Collision_box(self):

        self.Collide_Box = pygame.Rect(self.Pos_x , self.Pos_y ,  40, 40)

    def Is_Colliding(self,other):
        return self.Collide_Box.colliderect(other.Collide_Box)

    def Damage(self):
        self.Is_Visible = False
        self.Damage_Time = pygame.time.get_ticks()
        print(self.Health-1)

class Collectable:

    def Collect(self):
        self.Visible = False

    def Collision_box(self):

        self.Collide_Box =  self.rect.move(self.Pos_x,self.Pos_y)


class Coin(Collectable):

    def __init__(self, window, position = (400, 300), image = "coin.png"):
        self.Pos_x ,self.Pos_y = position
        self.Visible = True
        self.Window = window
        self.Image = pygame.image.load(os.path.join("assets",f"{image}"))
        self.rect = self.Image.get_rect()

    def Update(self):

        if self.Visible:
            self.Window.blit(self.Image, (self.Pos_x, self.Pos_y))
    def Collect(self):
        super().Collect()

class Key(Collectable):
    def __init__(self, window, position=(400, 300), image = 'key.png'):
        self.Pos_x, self.Pos_y = position
        self.Visible = True
        self.Window = window
        self.Image = pygame.image.load(os.path.join("assets", f"{image}"))
        self.rect = self.Image.get_rect()

    def Update(self):
        if self.Visible:
            self.Window.blit(self.Image, (self.Pos_x, self.Pos_y))

    def Collect(self):
        super().Collect()


class Wall():

    def __init__(self,window,position = (100,100),image = 'wall.png'):
        self.Pos_x ,self.Pos_y = position
        self.Image = pygame.image.load(os.path.join("assets",f'{image}'))
        self.Window = window
    def Update(self):
        self.Window.blit(self.Image, (self.Pos_x, self.Pos_y))


    def Collision_box(self):

        self.Collide_Box = pygame.draw.rect(self.Window, (255, 255, 255), (self.Pos_x, self.Pos_y, 32, 32), 1)

class Life_Heart(Collectable):
    def __init__(self, window, position=(400, 300)):
        self.Pos_x, self.Pos_y = position
        self.Visible = True
        self.Window = window
        self.Image = pygame.image.load(os.path.join("assets", "heart.png"))
        self.rect = self.Image.get_rect()

    def Update(self):
        if self.Visible:
            self.Window.blit(self.Image, (self.Pos_x, self.Pos_y))

    def Collect(self):
        super().Collect()

class Enemy:

    def __init__(self,  window , position, image = "enemy.png" ):

        self.Pos_x , self.Pos_y = position
        self.Window = window
        Img = pygame.image.load(os.path.join("assets",f"{image}"))
        self.Image = pygame.transform.scale(Img , (30,30))
        self.rect = self.Image.get_rect()
        self.Patrol_x1,self.Patrol_x2 = self.Pos_x-40,self.Pos_x+40
        self.direction = 1
        self.collide = False

    def Update(self):

        self.Window.blit(self.Image , (self.Pos_x,self.Pos_y))
        self.Patrol()

    def Collision_box(self):

        self.Collide_Box =  self.rect.move(self.Pos_x,self.Pos_y)

    def Damage_Player(self,other):

        if other.Health  > 0:
          other.Damage()

    def Patrol(self):
        if not self.collide:
            if self.direction == 1:
                self.Pos_x += 5
            else:
                self.Pos_x -= 5

        if self.Pos_x <= self.Patrol_x1 :
                self.direction = 1
        elif self.Pos_x >= self.Patrol_x2:
                self.direction = -1

    def Collide(self,walls):

        for wall in walls:
            self.collide = False
            if  self.Collide_Box.colliderect(wall.Collide_Box):

                if self.direction == 1:
                    self.Pos_x -= 5
                else:
                    self.Pos_x += 5
                self.direction = not self.direction
                self.collide = True
                break

class Chest(Collectable):

    def __init__(self, window, position=(400, 300), image = 'treasure_box.png'):
        self.Pos_x, self.Pos_y = position
        self.Visible = True
        self.Window = window
        self.Image = pygame.image.load(os.path.join("assets", f"{image}"))
        self.Image = pygame.transform.scale(self.Image,(40,40))
        self.rect = self.Image.get_rect()

    def Update(self):
        if self.Visible:
            self.Window.blit(self.Image, (self.Pos_x, self.Pos_y))

    def Collect(self,keys,Max_keys):
        if keys >= Max_keys:
            super().Collect()
            return True

