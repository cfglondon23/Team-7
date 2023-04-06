import pyrebase
import json
from typing import Union

config = pyrebase.initialize_app(json.load(open('fb/fbconfig.json')))
database = config.database()

def add_xp(email: str, xpvalue: int):
    database.child("User").child(email).set(xpvalue)

def get_xp(email: str) -> Union[int,str]:
    user = database.child("User").child(email).get().val()
    if not user:
        return None
    else:
        return user