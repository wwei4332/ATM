from db import db_handler
from lib import common

def shopping_interface(username):
    df=db_handler.read_excel()
    common.goods_visualize(df)
    product_list=df.columns.to_list()
    print(product_list)
    for i in enumerate(product_list):
        print(i)
    choice=input('请输入产品编号:')
    if not choice.isdigit():
        print('请输入正确的编号')
    else:
        choice=int(choice)
        if choice not in range(5):
            print('产品不存在')

        else:
            amount=input('请输入需要购买的数量：')
            if not amount.isdigit():
                print('请输入正确的数量')

            else:
                amount=int(amount)
                if amount>df.loc['数量',product_list[choice]]:
                    print('库存不足')

                else:
                    df.loc['数量',product_list[choice]]-=amount


                    user_dic=db_handler.read_json(username)
                    user_dic['shopping_cart'].append([{'商品名':product_list[choice]},
                                                      {'价格':int(df.loc['价格',product_list[choice]])},
                                                      {'数量':amount}])
                    db_handler.save_json(username,user_dic)
                    db_handler.save_excel(df)
                    return f'{product_list[choice]}数量{amount}成功加入购物车'

def shopping_cart_interface(username,choice):
    user_dic=db_handler.read_json(username)
    for i in enumerate(user_dic['shopping_cart']):
        print(i)

    if choice=='y':
       cost=user_dic['shopping_cart'][0][2]['价格']*user_dic['shopping_cart'][0][3]['数量']
       if cost>=user_dic['balance']:
           return f'{username}余额不足，支付失败'
       else:
           user_dic['balance']-=cost
           db_handler.save_json(username,user_dic)
           return f'{username}支付成功，花费{cost}元'
    elif choice=='n':
        user_dic['shopping_cart'].clear()
        db_handler.save_json(username,user_dic)
        return '{username}清空购物车成功'










    