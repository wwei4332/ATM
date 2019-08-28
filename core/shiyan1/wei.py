
from core import hanshu
from core.shiyan2 import shen
def login_auth(func):
    def wrapper():
        if shen.dic.get('username'):
            print(2)
        else:
            func()
    return wrapper

@login_auth



