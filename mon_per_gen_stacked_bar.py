#lets try a stacked bar of total pokemon by generation
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Pokemon.csv')

x = ['All Generations']

arr = np.array(df['Generation'].value_counts())
arr1 = np.array(arr[0])
arr2 = np.array(arr[1])
arr3= np.array(arr[2])
arr4 = np.array(arr[3])
arr5 = np.array(arr[4])
arr6 = np.array(arr[5])

plt.bar(x, arr1, color='red')
plt.bar(x, arr2, bottom=arr1, color='orange')
plt.bar(x, arr3, bottom=arr1+arr2,color='yellow')
plt.bar(x, arr4, bottom=arr1+arr2+arr3,color='green') 
plt.bar(x,arr5,bottom=arr1+arr2+arr3+arr4,color='blue')
plt.bar(x,arr6,bottom=arr1+arr2+arr3+arr4+arr5,color='indigo')
plt.legend(["Gen 1", "Gen 2", "Gen 3", "Gen 4","Gen 5","Gen 6"])
plt.show()

