from statistics import mean
from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt

style.use("fivethirtyeight")

# x values
xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
# y values
ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)


def best_fit_slope_and_intercept(xs, ys):
    m = ((mean(xs) * mean(ys)) - mean(xs * ys)) / (
        (mean(xs) * mean(xs)) - mean(xs * xs)
    )
    b = mean(ys) - (m * mean(xs))
    return m, b


# difference between regression line and actual ys
def squared_error(ys_original, ys_line):
    return sum((ys_line - ys_original) ** 2)


# find r^2 value
def coefficient_of_determination(ys_original, ys_line):
    y_mean_line = [mean(ys_original) for y in ys_original]
    squared_error_regr = squared_error(ys_original, ys_line)
    squared_error_y_mean = squared_error(ys_original, y_mean_line)
    return 1 - (squared_error_regr / squared_error_y_mean)


m, b = best_fit_slope_and_intercept(xs, ys)

# create regression line of y values based on all xs
# equivalent to:
# 	for x in xs:
# 		regression_line.append((m * x) + b)
regression_line = [(m * x) + b for x in xs]

# predict y where x = 8
predict_x = 8
predict_y = (m * predict_x) + b

r_squared = coefficient_of_determination(ys, regression_line)

print(f"m: {m}")
print(f"b: {b}")
print(f"R^2: {r_squared}")

plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, color="GREEN")
plt.plot(xs, regression_line)
plt.show()
