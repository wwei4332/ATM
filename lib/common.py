import logging
import logging.config
from conf import settings



import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def load_logging_config(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger=logging.getLogger(name)
    return logger


def goods_visualize(df):
    font=FontProperties(fname='D:\STXINWEI.TTF')
    goods_columns=df.columns.to_list()
    goods_amount=df.loc['数量',:].to_list()
    goods_price=df.loc['价格',:].to_list()
    amount_index=range(len(goods_amount))
    price_index=range(len(goods_price))
    fig=plt.figure()

    ax1=fig.add_subplot(121)

    ax1.bar(price_index,goods_price,color='red')
    ax1.set_title('价格表', fontproperties=font)
    plt.xticks(price_index,goods_columns,fontproperties=font,rotation=45)

    ax2 = fig.add_subplot(122)
    ax2.bar(amount_index,goods_amount,color='black')
    ax2.set_title('库存表', fontproperties=font)
    plt.xticks(amount_index,goods_columns,fontproperties=font,rotation=45)


    plt.suptitle('商品信息',fontproperties=font,fontsize=15,weight='bold')
    plt.show()

def login_auth(func):
    from core import src
    def wrapper(*args,**kwargs):
        if not src.user_auth.get('username'):
            res=src.login()
            func(*args, **kwargs)
            return res
        else:
            func(*args,**kwargs)
    return wrapper

