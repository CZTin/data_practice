import matplotlib.pyplot as plt

from random_walk import Randomwalk

#只要程序处于活动状态，就不断漫步
while True:
	#创建一个Randomwalk实例，并将其包含的点都绘制出来
	rw = Randomwalk()
	rw.fill_walk()

	#给点着色
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
	plt.show()
	#print(range(rw.num_points))

	keep_running = input("Walk again? (y/n): ")
	if keep_running =='n':
		break
