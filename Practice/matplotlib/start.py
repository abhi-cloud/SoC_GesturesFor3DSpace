from matplotlib import pyplot as plt

xs = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
ys1 = [342, 234, 235, 235, 124, 567, 768, 164, 109, 456, 901]

plt.plot(xs, ys1, linewidth=3, color='y', marker='.', linestyle='--', label='first')     # we can also pass hexvalues for colours

ys2 = [768, 945, 123, 453, 345, 634, 236, 217, 402, 309, 123]
plt.plot(xs, ys2, linewidth=2, color='b', marker='o', linestyle='-.', label='second')    

plt.xlabel('Ages')
plt.ylabel('Median Salary')
plt.title('Median Salary (USD) by Age')

plt.legend()
plt.grid(True)
plt.show()

# import pandas as pd
# from matplotlib import pyplot as plt

# data = pd.read_csv('data2.csv')
# ages = data['Age']
# dev_salaries = data['All_Devs']
# py_salaries = data['Python']
# js_salaries = data['JavaScript']

# print (js_salaries)

# plt.plot(ages, dev_salaries, color='#444444',
#          linestyle='--', label='All Devs')

# plt.plot(ages, py_salaries, label='Python')

# overall_median = 57287

# plt.fill_between(ages, py_salaries, dev_salaries,
#                  where=(py_salaries > dev_salaries),
#                  interpolate=True, alpha=0.25, label='Above Avg')

# plt.fill_between(ages, py_salaries, dev_salaries,
#                  where=(py_salaries <= dev_salaries),
#                  interpolate=True, color='red', alpha=0.25, label='Below Avg')

# plt.legend()

# plt.title('Median Salary (USD) by Age')
# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD)')

# plt.tight_layout()

# plt.show()