import configparser
from email.policy import default

class ConfigManager(configparser.ConfigParser):
    def __init__(self, config_file):
        configparser.ConfigParser.__init__(self)

        self.read(config_file)

        # Set defaults
        self.defaults = {
            'width' : 3000,
            'height' : 1000,
            'starting_asteroids' : 10,
            'spaceship_width': 48,
            'spaceship_height': 48,
            'spaceship_mass': 10,
            'small_asteroid_width': 44,
            'small_asteroid_height': 36,
            'small_asteroid_mass': 6,
            'big_asteroid_width': 68,
            'big_asteroid_height': 60,
            'big_asteroid_mass': 10,
        }

    def safe_get(self, section, option):
        return self.get(section, option, fallback = self.defaults[option])