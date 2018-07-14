class Settings:

    def __init__(self):
    #Screen
        self.screen_width = 1000#1200
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 2

    #Bullets
        self.bullet_speed_factor = 1#45
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 1

    #Alien
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.fleet_drop_speed = 5


    #Ship
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

    #How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #Settings that change throughout the time

        self.ship_speed_factor = self.score_scale
        self.bullet_speed_factor = 3
        self.alien_points = 10

        self.alien_speed_factor = 2
        #fleet_direction of 1 represents right -1 represents left
        self.fleet_direction = -1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.aliens_points = int(self.alien_points * self.score_scale)

        print(self.alien_points)



