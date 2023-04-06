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

def get_all_xp() -> list[str, int]:
    """ Gets all users + their xp

    Returns:
        list[str, int]: email, xp
    """
    xp_by_user = {}
    users = database.child("User").get().val()
    
    if not users:
        return None
    
    for user in users:
        xp = database.child("User").child(user).get().val()
        xp_by_user[user] = xp
    
    return xp_by_user
    

