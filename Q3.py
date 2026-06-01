# Find GCD and LCM of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

small = min(a, b)
for i in range(1, small + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
lcm = (a * b) // gcd

print("GCD =", gcd)
print("LCM =", lcm)