def tocels(fahrenheit):
    celsius = ((fahrenheit -32)*5)/9
    return celsius

def tofah(celsius):
    fahn = ((celsius*9)/5) + 32
    return fahn

if __name__ == "__main__":
    for temps in range(0, 212, 40):
        print(temps, "Fahrenheit = ", round(tocels(temps), 2), "Celsius")

    for temps in range(0, 100, 20):
        print(temps, "Celsius = ", round(tofah(temps) , 2), "Fahrenheit")