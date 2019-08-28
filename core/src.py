from lib import common
from interface import user,bank,store


logger=common.load_logging_config('user')
user_auth={'username':None}

def register():
    while True:
        username=input('请输入注册用户名：')
        pwd=input('请输入注册密码：')
        flag,msg=user.register_interface(username,pwd)
        if flag:
            print(msg)
            logger.info(msg)
            break
        else:
            print(msg)

def login():
    count=0
    while count<3:
        username=input('请输入登陆用户名：')
        pwd=input('请输入登陆密码：')
        flag,msg,level=user.login_interface(username,pwd,count)

        if level==2:
            print(msg)
            logger.info(msg)
            count+=1
        elif level==1:
            print(msg)
            logger.info(msg)
            user_auth['username']=username
            break
        else:
            print(msg)
            logger.info(msg)

@common.login_auth
def check_balance():
    username=user_auth['username']
    balance=bank.check_balance_interface(username)
    msg=f'{username}余额为{balance}元'
    print(msg)
    logger.info(msg)

@common.login_auth
def withdraw():
    while True:
        username=user_auth['username']
        money=input('请输入需要取款的金额').strip()
        if not money.isdigit():
            print('请输入正确金额')
            continue
        else:
            money=int(money)
            flag,msg=bank.withdraw_interface(username,money)
            if flag:
                print(msg)
                logger.info(msg)
                break
            else:
                print(msg)
                logger.info(msg)

@common.login_auth
def repay():
    while True:
        username=user_auth['username']
        money=input('请输入还款金额')
        if not money.isdigit():
            print('请输入正确金额')
            continue
        else:
            money=int(money)
            flag,msg=bank.repay_interface(username,money)
            if flag:
                print(msg)
                logger.info(msg)
                break

@common.login_auth
def transfer():
    from_username=user_auth['username']
    to_username=input('请输入转入账号')
    flag,msg=user.check_username_interface(to_username)
    if flag:
        money=input('请输入转账金额：')
        if not money.isdigit():
            print('请输入正确金额')
        else:
            money=int(money)
            flag1,msg1=bank.transfer_interface(from_username,to_username,money)
            if flag1:
                print(msg1)
                logger.info(msg1)
            else:
                print(msg1)
                logger.info(msg1)
    else:
        print(msg)

@common.login_auth
def shopping():
    username=user_auth['username']
    while True:
        msg=store.shopping_interface(username)
        print(msg)
        logger.info(msg)
        choice=input('按q退出购物')
        if choice=='q':
            break

@common.login_auth
def shopping_cart():
    while True:
        username=user_auth['username']
        choice = input('按y完成支付，按n清空购物车,按q退出')
        if choice=='q':
            break
        else:
            msg=store.shopping_cart_interface(username,choice)
            print(msg)
            logger.info(msg)

@common.login_auth
def check_flow():
    username=user_auth['username']
    msg=bank.check_flow_interface(username)
    print(msg)
    logger.info(f'{username}查看流水')

@common.login_auth
def logout():
    username=user_auth['username']
    user_auth['username']=None
    msg=f'{username}已经注销'
    print(msg)
    logger.info(msg)

FUNC_MSG='''
1:注册
2:登陆
3:查看余额
4:取款
5:还款
6:转账
7:购物
8:购物车
9:查看流水
10:注销
q:退出
'''

while True:
    print(FUNC_MSG)
    func_dic={'1':register,'2':login,'3':check_balance,'4':withdraw,'5':repay,'6':transfer,'7':shopping
              ,'8':shopping_cart,'9':check_flow,'10':logout}
    choice=input('请输入需要的功能编号：')
    if choice=='q':
        break
    else:
        func_dic[choice]()






