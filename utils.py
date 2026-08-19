def estimate_price(theta0=0, theta1=0, km=0):
    return theta0 + theta1 * km

def load_theta(filepath):
    try:
        with open(filepath, "r") as file:
            text = file.read()
            print(text)
    except FileNotFoundError:
        return (0, 0)
    theta0_string, theta1_string = text.split("\n")
    theta0 = float(theta0_string)
    theta1 = float(theta1_string)
    return (theta0, theta1)

def save_theta(filepath, theta0, theta1):
    with open(filepath, "w") as file:
        file.write(f"{theta0}\n{theta1}")