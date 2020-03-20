from configparser import ConfigParser
from mongoengine import *

config = ConfigParser()

config['settings'] = {
    'username': "arun",
    'pwd': '618618618'
}

with open('./dev.ini', 'w') as f:
    config.write(f)
