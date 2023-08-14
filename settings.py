class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""

        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        

        # Bullets settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right -1 represents left
        self.fleet_direction = 1

        # Ships settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Starts settings
        self.stars_enable = 20

        # How quickly the game speeds up
        self.speedup_scale = 1.5

        # How quickly the alient point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    
    def initialize_dynamic_settings(self):
        """initialize settings that change throughput the game."""
        self.ship_speed = 1.1
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        # Scoring
        self.alien_points = 50

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increments the speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points += int(self.alien_points * self.score_scale)
        