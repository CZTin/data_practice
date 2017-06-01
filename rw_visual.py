import matplotlib.pyplot as plt

from random_walk import Randomwalk
#创建一个Randomwalk实例，并将其包含的点都绘制出来
rw = Randomwalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
