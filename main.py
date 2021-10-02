import maze_generator as maze
import yaml
import twitter_api

try:
    with open("config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)
except FileNotFoundError:
    print("No se encuentra el fichero config.yaml. Por favor, renombre config-example.yaml a config.yaml")

# TODO: comprobar si están todas las configuraciones necesarias seteadas en el config.yaml

maze_img = maze.generate(config["width"], config["height"], config["credits"])
# maze_img.show()
twitter_api.publish(maze_img, config["twitter"])
