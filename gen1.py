#csv from https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6
import pandas as pd
import matplotlib.pyplot as plt
#read csv into datafrom
df = pd.read_csv("pokemon.csv")
#create a boolean mask True if pokemon is not mega
mask =  ~df['Name'].str.contains('Mega ')
#remove mega evolutions
df = df[mask]
#slice to only be GEN 1
gen1 = df.iloc[0:151]
gen1.groupby(['Type 1', 'Type 2']).size().plot(kind='bar')



