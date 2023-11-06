temperature = float(input("Enter the current temperature (in Celsius): "))

if temperature < 0:
    print("It's freezing! Wear a heavy coat.")
elif 0 <= temperature < 10:
    print("It's cold. Dress warmly.")
else:
    print("It's a comfortable temperature.")
