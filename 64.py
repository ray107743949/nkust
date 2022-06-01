number1 = int(input("number1:"))
number2 = int(input("number2:"))

prime_number1 = False
prime_number2 = False

if number1 - number2 == 2 or number2 - number1 == 2 :
    for i in range(2,number1):
        x = number1 % i
        if x == 0 :
            prime_number1 = True
            break
    for i in range(2,number2):
        x = number2 % i
        if x == 0 :
            prime_number2 = True
            break
    if not(prime_number1 and prime_number2) :
        print("y")
    else:
        print("n")
else:
    print("n")