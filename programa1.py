def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Conversor de temperatura")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")

    choice = input("Elige una opcion (1 or 2): ")

    if choice == "1":
        celsius = float(input("Introduce la temperatura: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C es {fahrenheit}°F")
    elif choice == "2":
        fahrenheit = float(input("Introduce la temperatura: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F es {celsius}°C")
    else:
        print("Opcion no valida")

if __name__ == "__main__":
    main()
