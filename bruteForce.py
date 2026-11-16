numbers = [15,34,60,70,94,20,11]

target = eval(input("Enter the number to search for: "))

for number in numbers:
    if number == target:
        print(number)
        break
else:
    print("Number not found")

"""Simple Code demo to illustrate bruteforce algorithm"""