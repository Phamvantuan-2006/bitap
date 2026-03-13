print("Celsius  Fahrenheit")
for c in range(0,11):
    f = 9/5*c + 32
    print(f"{c:7} {f:10.2f}")

print("\nFahrenheit  Celsius")
for f in range(32,43):
    c = 5/9*(f-32)
    print(f"{f:10} {c:8.2f}")
