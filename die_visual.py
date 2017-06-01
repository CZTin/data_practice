from die import Die
#创建一个D6（6个面的骰子的意思）
die = Die()

#投掷几次骰子，并将结果保存在列表里
results =[]
for roll_num in range(100):
	result = die.roll()
	results.append(result)

print(results)