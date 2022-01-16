#csv from https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6
import pandas as pd
import matplotlib.pyplot as plt
# I want to show the amount of pokemon in each generation
df = pd.read_csv("pokemon.csv")
plt.figure(0)
chart1 = df.groupby('Generation')['#'].count().plot(kind="bar")
chart1.set_title("Pokemon Per Generation")
chart1.set_ylabel('Number of Pokemon')
chart1.set_xlabel('Game Generation')
#We will use a boolean mask to find the megas
mask = ~df['Name'].str.contains('Mega ')
no_megas = df[mask]
#lets look now that we removed megas
plt.figure(1)
chart2 = no_megas.groupby('Generation')['#'].count().plot(kind="bar") 
chart2.set_title("Pokemon Per Generation Excluding Mega Evolutions")
chart2.set_xlabel("Game Generation")
chart2.set_ylabel("Number of Pokemon")


