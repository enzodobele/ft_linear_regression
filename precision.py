from utils import estimate_price, load_theta, parse_csv

def precision():
    mileages, prices = parse_csv("data.csv")
    theta0, theta1 = load_theta("theta.csv")
    sum_error, error = 0, 0
    for mileage, price in zip(mileages, prices):
        error = estimate_price(theta0, theta1, mileage)
        sum_error += abs(error - price)
    mae = sum_error / len(mileages)
    print(f"The model is off by {mae:.2f}€ on average.")

def main():
    precision()

if __name__ == "__main__":
    main()
