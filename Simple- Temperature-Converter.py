def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    celsius = float(input("Enter temperature in Celsius: "))
    
    print(f"{celsius}°C = {celsius_to_fahrenheit(celsius)}°F")
    

if __name__ == "__main__":
    main()
