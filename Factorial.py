number = int(input("Enter Your Number For Calculate The Factorial Of It: "))

Factorial = 1

for i in range(1, number+1):
    Factorial *= i
    
print(Factorial)