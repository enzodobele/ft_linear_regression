from utils import estimate_price, save_theta, parse_csv

def train(mileages, prices, learning_rate=0.01, iterations=100000):
    theta0, theta1 = 0, 0
    i = 0
    error = 0
    m = len(mileages)
    while i < iterations:
        sum_error_theta0, sum_error_theta1 = 0, 0
        for mileage, price in zip(mileages, prices):
            error = estimate_price(theta0, theta1, mileage) - price
            sum_error_theta0 += error
            sum_error_theta1 += error * mileage
        tmp_theta0 = learning_rate * (sum_error_theta0 / m)
        tmp_theta1 = learning_rate * (sum_error_theta1 / m)
        theta0 = theta0 - tmp_theta0
        theta1 = theta1 - tmp_theta1
        i += 1
    return theta0, theta1

def normalisation(values):
    min_value = values[0]
    max_value = values[0]
    mileages_normalize = []
    for value in values:
        if min_value > value:
            min_value = value
        if max_value < value:
            max_value = value
    for value in values:
        mileages_normalize.append((value - min_value) / (max_value - min_value))
    return mileages_normalize, min_value, max_value



def main():
    mileages, prices = parse_csv("data.csv")
    mileage_norm, km_min, km_max = normalisation(mileages)
    theta0_norm, theta1_norm = train(mileage_norm, prices)
    theta1 = theta1_norm / (km_max - km_min)
    theta0 = theta0_norm - theta1_norm * km_min / (km_max - km_min)
    save_theta("theta.csv" ,theta0, theta1)

if __name__ == "__main__":
    main()
