from tvDatafeed import TvDatafeed, Interval
import pandas_ta as ta
from coinex.coinex import CoinEx
import time

def moving():
    a =tv.get_hist(symbol='DOGEUSDT' , interval=Interval.in_30_minute , exchange='coinex' , n_bars=50)
    blue = ta.sma(close=a['close'] , length=8 )
    yellow = ta.sma(close=a['close'], length=14)
    print('blue',list(blue)[-1],'\nyellow', list(yellow)[-1])
    return list(blue)[-1] , list(yellow)[-1]




while True:
    try:
        print('start')
        b , y = moving()
        if b > y :
            info = coinex.balance_info()
            if 'USDT' in list(info):
                print('buy')
                count = info['USDT']['available']
                coinex.order_market(market='DOGEUSDT' , type='buy' , amount=float(count))
        elif y > b  :
            info = coinex.balance_info()
            if 'DOGE' in list(info):
                print('sell')
                count = info['DOGE']['available']
                coinex.order_market(market='DOGEUSDT' , type='buy' , amount=float(count))
    except:
        pass


    time.sleep(30)

