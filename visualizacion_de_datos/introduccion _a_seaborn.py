import seaborn as sns

import matplotlib.pyplot as plt

#datos

data= [7,8,5,6,9,10,6,8,5]

#crear una grafico de caja

sns.boxplot(data=data)

#agregar titulo
plt.title("grafico de caja")

#mostar el grafico

plt.show()



