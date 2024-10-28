import matplotlib.pyplot as plt

exercise = []
fhand = open("StudentExercise.csv")
next(fhand)
for line in fhand:
	words = line.split(",")
	num = words[0]
	if num != "":
		num = float(num)
		exercise.append(num)
print(exercise)
bins = len(exercise)
fig, ax = plt.subplots()
ax.hist(exercise, bins = bins)
ax.set(xlabel = 'Hours', title = 'How many hours of exercise')
plt.show()

def average(ls):
    if not ls:
        return 0
    return sum(ls) / len(ls)

def prop_above(ls):
    avg = average(ls)
    if not ls:
        return 0
    count_above = sum(1 for x in ls if x > avg)
    return count_above / len(ls)

def median(ls):
    if not ls:
        return 0
    sorted_ls = sorted(ls)
    n = len(sorted_ls)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_ls[mid - 1] + sorted_ls[mid]) / 2
    else:
        return sorted_ls[mid]

average(exercise)
prop_above(exercise)
median(exercise)

