# TS

from dateutil.parser import parse 
from functools import reduce
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

# Reading and renaming columns

brent_df = pd.read_excel("btd-5y.xlsx", parse_dates=['Date'])
unl87_df = pd.read_excel("unl87-5y.xlsx", parse_dates=['Date'])
ulsd_df  = pd.read_excel("ulsd-5y.xlsx", parse_dates=['Date'])
fo01_df  = pd.read_excel("fo01-5y.xlsx", parse_dates=['Date'])
fo03_df  = pd.read_excel("fo3-5y.xlsx", parse_dates=['Date'])

brent_df.rename({'Close(BFO-E)': 'brent'}, axis=1, inplace=True)
unl87_df.rename({'Close(RU-USG)': 'unl87'}, axis=1, inplace=True)
ulsd_df.rename({'Close(ULSD-USG)': 'ulsd'}, axis=1, inplace=True)
fo01_df.rename({'Close(FO1-H-USG)': 'fo01'}, axis=1, inplace=True)
fo03_df.rename({'Close(FO3-USG)': 'fo03'}, axis=1, inplace=True)

# Convert unl87 and ulsd from USc/gal to USD/bbl
unl87_df['unl87'] = 0.42 * unl87_df['unl87']
ulsd_df['ulsd'] = 0.42 * ulsd_df['ulsd']

# Single dataframe
dataframes = [brent_df, unl87_df, ulsd_df, fo01_df, fo03_df]
df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Date'], how='outer'), dataframes)

# Plotting
#df_merged[['brent', 'unl87', 'ulsd', 'fo01', 'fo03']].plot()
#plt.show()


df_merged['year'] = [d.year for d in df_merged['Date']]
df_merged['month'] = [d.strftime('%b') for d in df_merged['Date']]

years = df_merged['year'].unique()
month = df_merged['month'].unique()

df_m_y = df_merged.groupby(['year', 'month']).mean()
df_m_y.reset_index(inplace=True)
#print(years)
#print(df_m_y.head(20))

#plt.figure(figsize=(16,12), dpi=80)
print(df_m_y[['year', 'month', 'brent']])