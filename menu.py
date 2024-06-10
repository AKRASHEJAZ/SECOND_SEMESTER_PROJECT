import pygame
import os

class Menu_Widget():

    def __init__(self,window):

        self.font = pygame.font.SysFont("Verdana",18 , bold = True , italic = True  )
        self.Window = window
        self.Img_coin = pygame.image.load(os.path.join("assets","coin.png"))
        self.Img_key = pygame.image.load(os.path.join("assets", "key.png"))
        self.Img_heart = pygame.image.load(os.path.join("assets", "heart.png"))

    def Update(self, coins, keys, health):

        self.Coins = coins
        self.Keys = keys
        self.Health = health
        self.Draw()

    def Draw(self):

        self.Window.blit(self.Img_coin,(650,10))
        self.Window.blit(self.Img_key, (650, 60))
        self.Window.blit(self.Img_heart, (650, 110))

        Coin_text = self.font.render(f"{self.Coins} COINS",True,(255,215,0))
        Keys_text = self.font.render(f"{self.Keys} KEYS", True, (183, 226, 240))
        Health_text = self.font.render(f"{self.Health} HEALTH", True, (255, 99, 71))

        self.Window.blit(Coin_text, (700, 20))
        self.Window.blit(Keys_text, (700, 70))
        self.Window.blit(Health_text, (700, 120))