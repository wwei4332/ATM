import os
from conf import settings
from db import db_handler


def register_interface(username,pwd):
    user_path=os.path.join(settings.DB_PATH,f'{username}.json')
    if os.path.exists(user_path):
        return False,'用户已存在'
    else:
        user_dic={'username':username,'pwd':pwd,'balance':15000,'shopping_cart':[],'flow':[],'lock':0}
        flag=db_handler.save_json(username,user_dic)
        if flag:
            return True,f'{username}注册成功'

def login_interface(username,pwd,count):
    user_path = os.path.join(settings.DB_PATH, f'{username}.json')
    if os.path.exists(user_path):
        user_dic=db_handler.read_json(username)
        if pwd==user_dic['pwd']:
            if user_dic['lock'] == 1:
                return False, f'{username}账号已锁定',4
            return True,f'{username}登陆成功',1

        else:
            if count==2:
                user_dic['lock']=1
            return False,f'{username}密码错误',2

    else:
        return False,f'不存在用户{username}',3


def check_username_interface(username):
    user_path=os.path.join(settings.DB_PATH,f'{username}.json')
    if os.path.exists(user_path):
        return True,'账号存在'
    else:
        return False,f'{username}不存在'
