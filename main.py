# main file that loads the other files and starts the bot

import json
import pokebot

config = json.load(open('config.json'))

bot = pokebot(config['TOKEN'])


