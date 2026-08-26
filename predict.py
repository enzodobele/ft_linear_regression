from utils import load_theta, estimate_price 

def prediction():
    theta0, theta1 = load_theta("theta.csv")

    while True:
        try:
            km = float(input("Enter a mileage: "))
            if km < 0:
                print("Value can't be negative")
                continue
            break
        except ValueError:
            print("The value should be an number")
    
    estimatePrice = estimate_price(theta0, theta1, km)
    if estimatePrice < 0:
        print("0€")
        return
    print(f"The model prediction is {estimatePrice:.2f}€ on average.")

def main():
    prediction()

if __name__ == "__main__":
    main()