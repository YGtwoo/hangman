import configparser
import os


class Config(object):

    def create_config(self, path):
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.add_section("Name_points")
        config.set("Settings", "directory", "")
        config.set("Name_points", "name", "")
        config.set("Name_points", "points", "")

        with open(path, "w") as config_file:
            config.write(config_file)

    def get_config(self, path):
        if not os.path.exists(path):
            self.create_config(path)
        config = configparser.ConfigParser()
        config.read(path)
        return config

    def change_config(self, path, section, setting, value):
        config = self.get_config(path)
        config.set(section, setting, value)
        with open(path, "w") as config_file:
            config.write(config_file)

    def get_setting(self, path, section, setting):
        config = self.get_config(path)
        value = config.get(section, setting)
        return value
