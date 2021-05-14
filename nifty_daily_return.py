# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:10:35 2021

@author: Yash_Gaur
"""
import pandas as pd
import matplotlib as plt
link="C:/Users/y9829/Desktop/mayank rasu/nifty_data.csv"

df=pd.read_csv(link)
print(df.head())
df_close=pd.DataFrame(df,columns=["Close"])
daily_return=df_close.pct_change()
daily_return=daily_return.dropna()
daily_cum_return= (daily_return +1 ).cumprod()


plt.pyplot.plot( daily_return)
plt.pyplot.plot(daily_cum_return)

