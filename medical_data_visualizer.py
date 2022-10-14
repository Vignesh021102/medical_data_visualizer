import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set()

df = pd.read_csv('medical_examination.csv')

BMI = df['weight']/((df['height']/100) **2)

df['overweight'] = np.where(BMI>25,1,0)

df['cholesterol'] = np.where(df['cholesterol']>1,1,0)
df['gluc'] = np.where(df['gluc']>1,1,0)

df = df[(df['ap_lo']<=df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))&(df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]


# Draw Categorical Plot
def draw_cat_plot(): 
  catLabel = ['active','alco','cholesterol','gluc','overweight','smoke']
  catLabdf = pd.DataFrame({'cardio':[],'variable':[],'value':[],'total':[]})
  len = 0
  for i in range(0,2):
      for j in catLabel:
          for k in range(0,2):
              num = df[((df['cardio'] == 1 )&(df[j] == k))][j].count()
              catLabdf.loc[len]  = {'cardio':i,'variable':j,'value':k,'total':num}
              len+=1
  catLabdf.to_csv('./catplotData.csv')
  grid = sns.catplot(data=catLabdf,col='cardio',kind='bar',x='variable',y='total',hue='value')
  fig = grid.fig
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
  
  corr  = df.corr()
  mask = np.triu(np.ones_like(corr,dtype ='bool'))
  fig,ax = plt.subplots(1,1,figsize=(8,8))
  sns.heatmap(ax = ax,data = corr,mask = mask,annot=True,annot_kws = {'size':8},fmt='.1f',center = 0,linewidths=0.005,square=True)

  fig.savefig('heatmap.png')
  return fig
