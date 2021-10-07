import sys
import maze_generator as maze
import yaml
import twitter_api
from datetime import date

try:
    with open("config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)
except FileNotFoundError:
    print("config.yaml file not found. Please, copy config-example.yaml to config.yaml")
    sys.exit()

# Checking the config file and setting default values for width, height and cell_size if not provided or are incorrect.
width = config["width"] if "width" in config and 2 <= config["width"] <= 400 else 10
height = config["height"] if "height" in config and 2 <= config["height"] <= 400 else 10
cell_size = config["cell_size"] if "cell_size" in config and config["cell_size"] >= 10 else 20
credits_txt = config["credits"] if "credits" in config else ""
twitter = config["twitter"] if "twitter" in config else None
if twitter is not None:
    if "api_key" not in twitter:
        twitter = None
    if "api_key_secret" not in twitter:
        twitter = None
    if "access_token" not in twitter:
        twitter = None
    if "access_token_secret" not in twitter:
        twitter = None
if twitter is None:
    print("No api keys for Twitter provided. Please, check the config file.")

message = ""
time = ""
if "--time" in sys.argv:
    index_time = sys.argv.index("--time")
    if len(sys.argv) > index_time + 1:
        time = sys.argv[index_time + 1]
        today = date.today().strftime("%A").lower()
        if "messages" in config:
            messages = config["messages"]
            if messages is not None and time in messages:
                messageOptions = messages[time]
                if messageOptions is not None:
                    if "generic_text" in messageOptions:
                        message = messageOptions["generic_text"]
                    else:
                        print(f"No {time} generic_text provided")
                    if today in messageOptions:
                        message += " " + messageOptions[today]
                    else:
                        print(f"No {time} - {today} text provided")
                else:
                    print(f"No messages for {time} provided")
            else:
                print(f"No messages for {time} provided")
        else:
            print("No messages options provided")
    else:
        print("No time provided. The message will be blank")
else:
    print("No time provided. The message will be blank")

maze_img = maze.generate(width, height, cell_size, credits_txt, time)
# maze_img.show()
if twitter is not None:
    twitter_api.publish(message, maze_img, config["twitter"])
