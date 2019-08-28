from db import db_handler

def check_balance_interface(username):
    user_dic=db_handler.read_json(username)
    return user_dic['balance']

def withdraw_interface(username,money):
    user_dic=db_handler.read_json(username)
    if user_dic['balance']>=1.05*money:
        user_dic['balance']-=1.05*money
        db_handler.save_json(username,user_dic)
        user_dic['flow'].append(f'{username}成功取现{money}元')
        db_handler.save_json(username,user_dic)
        return True,f'{username}成功取现{money}元'
    else:
        return False,f'{username}余额不足'


def repay_interface(username,money):
    user_dic=db_handler.read_json(username)
    user_dic['balance']+=money
    db_handler.save_json(username,user_dic)
    user_dic['flow'].append(f'{username}成功还款{money}元')
    return True,f'{username}成功还款{money}元'

def transfer_interface(from_username,to_username,money):
    from_user_dic=db_handler.read_json(from_username)
    to_username_dic=db_handler.read_json(to_username)
    if from_user_dic['balance']>=money:
        from_user_dic['balance']-=money
        to_username_dic['balance']+=money
        db_handler.save_json(from_username,from_user_dic)
        db_handler.save_json(to_username,to_username_dic)
        from_user_dic['flow'].append(f'{from_username}成功向{to_username}转账{money}元')
        return True,f'{from_username}成功向{to_username}转账{money}元'
    else:
        to_username_dic['flow'].append(f'{from_username}余额不足，转账失败')
        return  False,f'{from_username}余额不足，转账失败'

def check_flow_interface(username):
    user_dic=db_handler.read_json(username)
    print(user_dic['flow'])
    return user_dic['flow']

