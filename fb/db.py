import pyrebase
import json

config = pyrebase.initialize_app(json.load(open('fb/fbconfig.json')))
database = config.database()


