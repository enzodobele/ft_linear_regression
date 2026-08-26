def estimate_price(theta0=0, theta1=0, km=0):
    return theta0 + theta1 * km

def load_theta(filepath):
    try:
        with open(filepath, "r") as file:
            text = file.read()
    except FileNotFoundError:
        return (0, 0)
    theta0_string, theta1_string = text.split("\n")
    theta0 = float(theta0_string)
    theta1 = float(theta1_string)
    return (theta0, theta1)

def save_theta(filepath, theta0, theta1):
    with open(filepath, "w") as file:
        file.write(f"{theta0}\n{theta1}")

def parse_csv(filepath):
    mileage = []
    price = []
    try:
        with open(filepath, "r") as file:
            header = file.readline()
            for ligne in file :
                colonne = ligne.split(",")
                mileage.append(float(colonne[0]))
                price.append(float(colonne[1]))
    except FileNotFoundError:
        print("couldn't find data.csv")
        return 
    return mileage, price