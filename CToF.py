# PROGRAM to convert c to f
def temp(degree_celsius: float):
    # degreeCelsius = float(input("Enter temp in c: "))
    farenHeit = 1.8 * degree_celsius - 32
    return farenHeit


print("Temp in f: ", temp(float(input('Enter temperature in degree celsius:'))))
