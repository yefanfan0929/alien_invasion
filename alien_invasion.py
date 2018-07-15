#-*- coding:utf-8 -*-
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	play_button = Button(ai_settings,screen,"Play")
	f = open('D:/python/alien_invasion/high_score.txt', 'r+')
	stats = GameStats(f,ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	gf.create_fleet(ai_settings,screen,ship,aliens)
	alien = Alien(ai_settings,screen)

	while True:
		gf.check_events(f,ai_settings,screen,stats,sb,play_button,ship,aliens,
			bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
		print(len(bullets))
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
			play_button)
run_game()
