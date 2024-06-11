import classes as cls
import level_loader as lvl
import pygame
import os
import menu
import sys
from tkinter import messagebox

def Quit():
    choice = messagebox.askyesno("QUIT","ARE YOU SURE")
    if choice:
        sys.exit(0)

def Load_level( file = "level_python.txt" ):
    Level = lvl.load_level(file)
    if Level == None:
        messagebox.showerror("ERROR", "NO LEVEL LOADED PLEASE SELECT AGAIN")
        sys.exit(1)
    return Level
def Game(GUI,Level = lvl.load_level("level_python.txt")):
    GUI.withdraw()
    if  Level == None:
        messagebox.showerror("ERROR","NO LEVEL SELECTED")
    else:
        pygame.init()
        # MAIN PROGRAM
        win = pygame.display.set_mode((800,600))

        pygame.display.set_caption("HERO RUNNING 2D")

        Logo = pygame.image.load( os.path.join( "assets","game_logo.png"))
        pygame.display.set_icon(Logo)

        Background = pygame.image.load( os.path.join( "assets","background.png"))
        Background = pygame.transform.scale(Background,(800,600))

        FPS = 30

        coins = 0
        keys = 0
        health = 3
        won = False
        fail = False

        run = True

        walls = []
        objs = []
        enemies =[]
        if not Level == None:
            try:
                clock = pygame.time.Clock()
                menu1 = menu.Menu_Widget(win)

                walls = lvl.render_level(Level,win,walls)
                objs = lvl.render_objects(Level,win,objs)
                enemies = lvl.render_enemies(Level , win , enemies)
                hero = lvl.render_Hero(Level , win)

                hero.Health = health

                last_damage_time = pygame.time.get_ticks()

                Max_keys = 0

                for obj in objs:
                    if isinstance(obj , cls.Key):
                        Max_keys += 1

                #MAIN LOOP OF GAME
                while run:
                    clock.tick(FPS)
                    win.fill((0,0,0))
                    win.blit(Background,(0,0))
                    events = pygame.event.get()

                    for event in events:

                        if event.type == pygame.QUIT:
                            run = False

                    for wall in walls :
                        wall.Update()
                        wall.Collision_box()

                    #updates hero
                    hero.Update(walls)
                    hero.Collision_box()

                    #creates and updates menu
                    menu1.Update(coins,keys,health)

                    for enemy in enemies:
                        current_time = pygame.time.get_ticks()
                        enemy.Update()
                        enemy.Collision_box()
                        enemy.Collide(walls)
                        hit = hero.Is_Colliding(enemy)
                        if hit:
                            if current_time - last_damage_time >= 1000:
                                enemy.Damage_Player(hero)
                                health -= 1
                                hero.Health = health
                                last_damage_time = current_time

                    for obj in objs:

                        obj.Update()
                        obj.Collision_box()
                        hit = hero.Is_Colliding(obj)

                        if hit:
                            if isinstance(obj, cls.Coin):
                                coins += 1
                                obj.Collect()
                                objs.remove(obj)
                            elif isinstance(obj, cls.Key):
                                keys += 1
                                obj.Collect()
                                objs.remove(obj)
                            elif isinstance(obj, cls.Life_Heart):
                                health += 1
                                hero.Health = health
                                obj.Collect()
                                objs.remove(obj)
                            if isinstance(obj, cls.Chest):
                                won = obj.Collect(keys,Max_keys)
                                if won:
                                    objs.remove(obj)


                    menu1.Update(coins,keys,health)
                    pygame.display.update()

                    if health <= 0 :
                        fail = True
                        break

                    if won:
                        break


                if fail :
                    win.fill((0,0,0))
                    Game_over = pygame.image.load(os.path.join("assets","game_over.png"))
                    Game_over = pygame.transform.scale(Game_over,(200,150))
                    win.blit(Game_over,(300,200))
                    pygame.display.update()
                    pygame.event.get()
                    pygame.time.delay(500)
                    pygame.quit()

                if won:
                    win.fill((0, 0, 0))
                    Winner = pygame.image.load(os.path.join("assets", "you_won.png"))
                    Winner = pygame.transform.scale(Winner, (800, 600))
                    win.blit(Winner, (0, 0))
                    pygame.display.update()
                    pygame.event.get()
                    pygame.time.delay(500)
                    pygame.quit()
            except:
                if not Level == None:
                    messagebox.showerror("ERROR","UNHANDELED EXCEPTION OCCURED \nPLEASE TRY AGAIN")
                pygame.quit()
    GUI.deiconify()
    pygame.quit()
