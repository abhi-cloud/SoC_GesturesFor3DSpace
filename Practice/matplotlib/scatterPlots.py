import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data3.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c=ratio, cmap='summer', edgecolor='black', linewidth=1, alpha=0.7)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike ratio')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('View Count')
plt.ylabel('Total Likes')
plt.title('YouTube Videos\' trends')
plt.legend()

plt.show()