import sys
import maze_generator as maze
import yaml
import twitter_api
from datetime import date

try:
    with open("config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)
except FileNotFoundError:
    print("No se encuentra el fichero config.yaml. Por favor, renombre config-example.yaml a config.yaml")

# TODO: comprobar si están todas las configuraciones necesarias seteadas en el config.yaml

message = ""
time = ""
if "--time" in sys.argv:
    index_time = sys.argv.index("--time")
    if len(sys.argv) > index_time + 1:
        time = sys.argv[index_time + 1]
        today = date.today().strftime("%A").lower()
        messageOptions = config["messages"][time]
        message = messageOptions["generic_text"] + " " + messageOptions[today]
    else:
        print("No time provided. The message will be blank")
else:
    print("No time provided. The message will be blank")

maze_img = maze.generate(config["width"], config["height"], config["cell_size"], config["credits"], time)
# maze_img.show()
twitter_api.publish(message, maze_img, config["twitter"])
