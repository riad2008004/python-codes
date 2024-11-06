import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv("parkinson_data_ana/person_3.csv", header=None)

t = df[0]
x = df[14]

t_mean=t[:]
x_mean=x[:]

plt.plot(t_mean,x_mean,lw=0.8)
plt.show()