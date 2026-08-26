import  matplotlib.pyplot   as plt
from    utils import parse_csv, load_theta, estimate_price


mileages, prices = parse_csv("data.csv")
theta0, theta1 = load_theta("theta.csv")

plt.scatter(mileages, prices)
plt.plot([min(mileages), max(mileages)], [estimate_price(theta0, theta1, min(mileages)), estimate_price(theta0, theta1, max(mileages))])

plt.xlabel("Mileage (km)")
plt.ylabel("Price (€)")
plt.title("ft_linear_regression")
plt.legend(["Actual prices", "Regression line"])

plt.savefig("ft_linear_regression.png")