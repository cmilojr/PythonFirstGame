import pygame
import game_functions as gf
from settings import Settings
from pygame.sprite import Group
from ship import Ship
#from alien import Alien
from game_stats import GameStats
from button import Bottom



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    #alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    bg_color = ai_settings.bg_color
    gf.create_fleet(ai_settings, screen, ship, aliens)
    play_button = Bottom(ai_settings,screen, "PLAY")
    while True:
        #update postions to draw a new screen
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

        bullets.update()
        if stats.game_active:
            # update positon of the ship
            ship.update()
            # delete bullets from game
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        #check player input
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)

        screen.fill(bg_color)
        ship.blitme()
        pygame.display.flip()


run_game()
